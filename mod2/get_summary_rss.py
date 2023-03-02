import math


def human_read_format(size: int) -> str:
    pwr = math.floor(math.log(size, 1024))
    suff = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ', 'ПБ', 'ЭБ', 'ЗБ', 'ЙБ']
    if size > 1024 ** (len(suff) - 1):
        return 'не знаю как назвать такое число :)'
    return f'{size / 1024 ** pwr:.0f}{suff[pwr]}'


def get_summary_rss(path: str) -> int:
    return sum(int(line.split()[5]) for line in open(path, 'r').readlines()[1:])


if __name__ == '__main__':
    print(human_read_format(get_summary_rss('output_file.txt')))
