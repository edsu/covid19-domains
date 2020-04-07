Experiments related to COVID-19 domain blocklists.

* DomainTools: https://www.domaintools.com/resources/blog/free-covid-19-threat-list-domain-risk-assessments-for-coronavirus-threats

## Setup

    git clone https://github.com/edsu/covid19-blocklists.git
    cd covid19-blocklists
    pipenv install

Since DomainTools are releasing their data it's useful to set up daily data
collection and a push to GitHub:

    0 12 * * * cd /home/ed/Projects/covid19-blocklists; /usr/local/bin/pipenv run utils/domaintools.py

## MyBinder

You can also start these up live on MyBinder by clicking this link:

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/edsu/covid19-blocklists)


