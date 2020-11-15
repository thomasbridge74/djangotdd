# TDD with Django

[![Build Status](https://travis-ci.org/thomasbridge74/djangotdd.svg?branch=master)](https://travis-ci.org/thomasbridge74/djangotdd) 
[![Coverage Status](https://coveralls.io/repos/github/thomasbridge74/djangotdd/badge.svg?branch=master)](https://coveralls.io/github/thomasbridge74/djangotdd?branch=master)

This repo contains code + other configuration to develop my ability
to write unit tests for Django.

The initial commit to the repo is based on code developed from 
following the 
[Test Driven Django Development](https://test-driven-django-development.readthedocs.io/en/latest/index.html)
tutorial.

At the time of the [initial commit](https://github.com/thomasbridge74/djangotdd/releases/tag/v1.0), all tests were passing on my
local machine.

## Travis CI

To get this working with travis CI the following `.travis.yml` file was
sufficent:

```yaml
language: python
python:
  - "3.7"
install:
  - pip install -r requirements.txt
script:
  - python manage.py test
```

This needed to be added to the repo and committed to Github for
Travis CI to pick up the new version of the repo and run the tests.
As can be seen [here](https://travis-ci.org/github/thomasbridge74/djangotdd/builds/743727041)
the build passed the tests.

## Links

[Setting up coverage + badge](https://medium.com/@erika_dike/connecting-your-django-app-to-travis-and-coveralls-c73a1a56eb06)