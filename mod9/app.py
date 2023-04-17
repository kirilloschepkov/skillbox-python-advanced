import os.path

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
root_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(root_dir, 'templates')
js_directory = os.path.join(template_folder, 'js')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(js_directory, path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
