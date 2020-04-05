Experiments related to COVID-19 domain blacklists.

* DomainTools: https://www.domaintools.com/resources/blog/free-covid-19-threat-list-domain-risk-assessments-for-coronavirus-threats

## Setup


    git clone https://github.com/edsu/covid19-blacklists.git
    cd covid19-blacklists
    pipenv install

Since DomainTools are releasing their data it's useful to set up daily data
collection and a push to GitHub:

    0 12 * * * cd /home/ed/Projects/covid19-blacklists; /usr/local/bin/pipenv run utils/domaintools.py
