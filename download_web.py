import urllib.request
import datetime
import pandas as pd
import sys
from requests import HTTPError


def download_csv():
    url = "http://namaristats.com/datatable.csv"
    date = datetime.date.today().strftime("%Y%m%d")
    savename = "lang" + date + ".csv"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    }
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', headers["User-Agent"])]
    urllib.request.install_opener(opener)
    try:
        urllib.request.urlretrieve(url, savename)
        print(savename)
        return savename
    except (OSError, HTTPError) as e:
        print("ERROR")
        sys.exit()


def read_csv(data):
    csv_lst = pd.read_csv(data).values.tolist()
    program_language = list()
    program_rep = list()

    for i in range(0, 19):
        program_language.append(csv_lst[i][0])
        program_rep.append(csv_lst[i][1])
    return program_language, program_rep


def main():
    savename = download_csv()
    program_language, program_rep = read_csv(savename)
    print(program_language)
    print(program_rep)


if __name__ == '__main__':
    main()
