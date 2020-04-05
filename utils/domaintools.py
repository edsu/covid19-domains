#!/usr/bin/env python3

import shutil
import pathlib
import requests
import datetime

url = 'https://covid-19-threat-list.domaintools.com/dt-covid-19-threat-list.csv.gz'

def download(path):
    with requests.get(url, stream=True) as r:
        with open(path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return path

def main():
    date = datetime.date.today()
    cwd = pathlib.Path(__file__).parent.absolute()
    path = (cwd / "data" / "dnstools" / date.strftime('%Y-%m-%d')).with_suffix('.csv.gz')
    download(path)

if __name__ == "__main__":
    main()
