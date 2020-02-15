iDiet Tracking Server
=====================


![Continuous Integration](https://github.com/johnhoman/tracking-server/workflows/Continuous%20Integration/badge.svg)

## Development
### Install requirements
To install requirements, pip install the repo root. Note, this repo doesn't
contain a setup.py so make sure you're using the latest pip `pip install -U pip`

First create a virtual environment.
See [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).

```bash
$ mkvirtualenv tracking-server
(tracking-server) $ python -m pip install .
```

### Run tests
To run tests install tox

Note: python interpreters must be installed. Tox will not do that for you
```bash
(tracking-server) $ python -m pip install tox
(tracking-server) $ tox -e py36 # runs tests on python3.6
```
or just run pytest directly -- although this is not recommended

```bash
pytest tests
flake8 idiet tests
```
