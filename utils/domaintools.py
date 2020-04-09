#!/usr/bin/env python3

import os
import boto3
import shutil
import pathlib
import requests
import datetime

base = pathlib.Path(__file__).parent.parent.absolute()
url = 'https://covid-19-threat-list.domaintools.com/dt-covid-19-threat-list.csv.gz'

def download(path):
    with requests.get(url, stream=True) as r:
        with open(path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return path

def main():
    date = datetime.date.today()
    path = date.strftime('%Y-%m-%d') + '.csv.gz'
    download(path)
    
    s3 = boto3.client('s3')
    s3.upload_file(path, 'edsu-covid19-domains', 'domaintools/{}'.format(path))
    os.remove(path)

if __name__ == "__main__":
    main()
