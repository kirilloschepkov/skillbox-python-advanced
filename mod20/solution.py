from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Date, Float, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, mapper, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from flask import Flask, jsonify, abort, request
from sqlalchemy.exc import NoResultFound, MultipleResultsFound

engine = create_engine('sqlite:///python.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

app = Flask(__name__)


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f'{self.name}, {self.count}, {self.release_date}, {self.author_id}'

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Authors(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    surname = Column(String(16), nullable=False)

    def __repr__(self):
        return f'{self.name} {self.surname}'


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    surname = Column(String(16), nullable=False)
    phone = Column(String(11), nullable=False)
    email = Column(String(30), nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    def __repr__(self):
        return f'{self.name} {self.surname}, {self.phone}, {self.email}, {self.average_score}, {self.scholarship}'

    @classmethod
    def get_scholarship_students(cls):
        return session.query(Students).filter(Students.scholarship).all()

    @classmethod
    def get_students_with_higher_score(cls, score):
        return session.query(Students).filter(Students.average_score > score).all()


class ReceivingBooks(Base):
    __tablename__ = 'receiving_books'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    def __repr__(self):
        return f'{self.book_id}, {self.student_id}, {self.date_of_issue}, {self.date_of_return}'

    @hybrid_property
    def count_date_with_book(self):
        return ((self.date_of_return or datetime.now()) - self.date_of_issue).days


Base.metadata.create_all(engine)


@app.before_request
def before_request_function():
    Base.metadata.create_all(engine)


@app.route('/')
def home_page():
    return 'Home page'


@app.route('/books', methods=['GET'])
def books():
    books_req = session.query(Books).all()
    books_list = [book.to_json() for book in books_req]
    return jsonify(books_list=books_list), 200


@app.route('/debtors', methods=['GET'])
def debtors():
    debtors_req = session.query(ReceivingBooks).filter(ReceivingBooks.date_of_return is None).all()
    debtors_list = [debtor.to_json() for debtor in debtors_req if debtor.count_date_with_book > 14]
    return jsonify(debtors_list=debtors_list), 200


@app.route('/issue', methods=['POST'])
def issue():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    new_issue = ReceivingBooks(book_id=book_id,
                               student_id=student_id,
                               date_of_issue=datetime.now())
    session.add(new_issue)
    session.commit()
    return f"Книга выдана", 200


@app.route('/pass_book', methods=['POST'])
def pass_book():
    try:
        book_id = request.form.get('book_id', type=int)
        student_id = request.form.get('student_id', type=int)
        book = session.query(ReceivingBooks).filter(ReceivingBooks.book_id == book_id, ReceivingBooks.student_id == student_id).one()
        book.date_of_return = datetime.now()
        session.commit()
        return f"Книга принята"
    except NoResultFound:
        return 'Такой книги не существует'
    except MultipleResultsFound:
        return 'Таких книг несколько'


# metadata = MetaData()
# books = Table('books', metadata,
#               Column('id', Integer, primary_key=True),
#               Column('name', String(16), nullable=False),
#               Column('count', Integer),
#               Column('release_date', Date),
#               Column('author_id', Integer)
#               )
#
#
# class Book:
#     def __init__(self, name, count, release_date, author_id):
#         self.name = name
#         self.count = count
#         self.release_date = release_date
#         self.author_id = author_id
#
#     def __repr__(self):
#         return f'{self.name}, {self.count}, {self.release_date}, {self.author_id}'
#
# mapper(Book, books)
# metadata.create_all()

if __name__ == '__main__':
    app.run(debug=True)
