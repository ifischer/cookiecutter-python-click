Python click Cookiecutter template
==================================

Cookiecutter scaffold to create minimal Python click application.
Features:

* proper module setup with setup.py and requirements.txt
* Docker as sole requirement
* Makefile for quick access to Docker commands 


Installation
------------

Install cookiecutter:
```
# Globally:
pip install cookiecutter

# Via pipsi (https://github.com/mitsuhiko/pipsi):
pipsi install cookiecutter
```

Create project from template:
```
cookiecutter -o $PROJECT_HOME .
```

Test
----

For an initial test, go to your generated project home and run:

```
make build test
```
