#!/usr/bin/env python3

import git
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
    path = (base / "data" / "domaintools" / date.strftime('%Y-%m-%d')).with_suffix('.csv.gz')
    download(path)
    repo = git.Repo(base)
    repo.index.add([path.as_posix()])
    repo.index.commit("Added latest DomainTools file {}".format(path))
    repo.remotes.origin.push()

if __name__ == "__main__":
    main()
