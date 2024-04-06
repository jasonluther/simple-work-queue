# Simple Work Queue in Python

The purpose of this project is for me to learn how to build and publish a python module.

The code itself is meant to provide a simple interface for a work queue. Using the interface should make it easier to swap out different types of queues. 

## Configuration

I will attempt to use poetry to manage the [pyproject.toml](pyproject.toml) file. 

```sh
pip3 install poetry
export POETRY_VIRTUALENVS_PATH=.venv
poetry init
```

To do:

  * add [classifiers](https://python-poetry.org/docs/pyproject/#classifiers). 

### Unit tests

Unit tests are in [tests](./tests). 

```sh
poetry add pytest --group test
```


### Using a `src` directory

This is the most confusing aspect of structuring a python project to me. I still haven't figured out the optimal way to configure the environment so that everything works, including my IDE. 

### Visual Studio Code environment

I'm checking in my .vscode files to keep track of what needs to be done to configure it to my liking. 

To do:

  * Get pylance to work with the virtual environment created by poetry
