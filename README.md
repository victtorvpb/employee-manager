# employee-manager

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/60c47316ecce4a95b0126c431c7ec3eb)](https://app.codacy.com/app/victorpb/employee-manager?utm_source=github.com&utm_medium=referral&utm_content=victtorvpb/employee-manager&utm_campaign=Badge_Grade_Settings)
[![Build Status](https://travis-ci.org/victtorvpb/employee-manager.svg?branch=master)](https://travis-ci.org/victtorvpb/employee-manager)

## Requirements
* docker
* docker-compose


## Execute project

* Pre populate database `python manage.py loaddata dump_free_fair.json` with data from the city hall

* Run server `python manage.py runserver`

* Access [http://localhost/api/v1/its_alive/](http://localhost/api/v1/its_alive/) to list urls api

## Docs api

Access [http://localhost/docs/](http://localhost/docs/) to list documentation api

Exemple object to post:

```
{
    "department": "Architecture",
    "name": "Name",
    "email": "admin@admin.com",
}
```

## Execute test
Execute tests and generate docs coverage in folder htmlcov
* `make start `
* `make test `

Acesse folder htmlcov to show coverage docs

## Check pep8 formatter test
* `make start `
* `make pep8 `

## Formatter formatter code
* `make start `
* `make formatter `
