# Overview

The purpose of this repository is to learn about using python to create a REST API using `fastapi` lib.

The project structure will follow hexagonal architecture and a DDD approach, so that will allow me to test
dependency injection and other SOLID principles with python.

## Requirements

| Component | Version | Description |
| -- | --| -- |
| Python | >= 3.12  | I think that any python3.x installation should work with this project. |
| Poetry | >= 1.8.3 | This is the version I'm currently checking. I think that any other 1.x version should work |

### Poetry

I'm working with a Mac laptop with homebrew installed. If this is your setup the easiest way is to install it 
using brew:

```shell
brew install poetry
```

Once installed I would recommend to set the following poetry options:

- `poetry config -- virtualenvs.in-project true`. This will create a `.venv` with the virtual environment in
the project folder. If not, it will be created in the default folder for poetry.

## Tech

| Name| Description|
| -- | --|
| Fastapi | Python library to serve REST APIs |

## How to run

### Install

```shell
poetry install
```

### Run

```shell
poetry run start
```

### Test

```shell
to be completed
```
