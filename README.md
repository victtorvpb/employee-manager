# employee-manager

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/60c47316ecce4a95b0126c431c7ec3eb)](https://app.codacy.com/app/victorpb/employee-manager?utm_source=github.com&utm_medium=referral&utm_content=victtorvpb/employee-manager&utm_campaign=Badge_Grade_Settings)
[![Build Status](https://travis-ci.org/victtorvpb/employee-manager.svg?branch=master)](https://travis-ci.org/victtorvpb/employee-manager)

## Requirements
* docker
* docker-compose
* Make


## Execute project

* Run project `make start` or `docker-compose up`

* Access [http://localhost/api/v1/its_alive/](http://localhost/api/v1/its_alive/)

## Default Admin User
username: admin

password: admin

## Docs api

Access [http://localhost/docs/](http://localhost/docs/) to list documentation api

Example object to post:

```
{
    "department": "Architecture",
    "name": "Name",
    "email": "admin@admin.com",
}
```

Example url to delete

http://localhost/api/v1/employee/baabf6bd-e4cb-4d09-90d4-6181238c508c/

URL to list employee:

http://localhost/api/v1/employee/

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
