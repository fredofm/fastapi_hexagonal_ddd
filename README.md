# Overview

The purpose of this repository is to learn about using python to create a REST API using `fastapi` lib.

The project structure will follow hexagonal architecture and a DDD approach, so that will allow me to test
dependency injection and other SOLID principles with python.

## Requirements

| Component | Version | Description |
| -- | --| -- |
| Python | >= 3.12  | Any python3.x installation should work with this project. |
| Poetry | >= 1.8.3 | Package manager |

### Poetry

I'm working with a Mac laptop with homebrew installed. If this is your setup the easiest way is to install it 
using brew:

```shell
brew install poetry
```

Once installed I would recommend to set the following poetry options:

- `poetry config -- virtualenvs.in-project true`. This will configure poetry package manager to the `.venv` folder for the virtual environment inside the current project folder. If not, it will be created in the default folder for poetry.

## Tech

| Name| Description|
| -- | --|
| Fastapi | Python library to serve REST APIs |

## Install

For installing the dependencies and creating the virtual environment for python execute the following command:

```shell
poetry install
```

## Run

To serve the application just run the following commands:

- Activate the virtual environment if it's not already activated. You can do it using `poetry` o `source`:

```shell
poetry shell
```

```shell
source ./.venv/bin/activate
```

- Once the virtual environment is activated you can run the application:

```shell
poetry run start
```

## Test

```shell
to be completed
```
