Experiments related to COVID-19 domains.

* DomainTools: https://www.domaintools.com/resources/blog/free-covid-19-threat-list-domain-risk-assessments-for-coronavirus-threats

## Setup

    git clone https://github.com/edsu/covid19-domains.git
    cd covid19-domains
    pipenv install

## Data

Many of these notebooks will write data. If you would like to get the results of
this analysis you can clone this s3 bucket to your data directory:

    aws s3 sync s3://edsu-covid19-domains data

Since DomainTools are releasing their data it's useful to set up daily data
collection and a push to an s3 bucket.

    0 12 * * * cd /home/ed/Projects/covid19-domains; /usr/local/bin/pipenv run utils/domaintools.py

