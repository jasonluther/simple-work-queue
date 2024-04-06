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
  * set up branch protection in github

### Unit tests

Unit tests are in [tests](./tests). 

```sh
poetry add pytest --group test
```

Add this to `keybindings.json` in vscode's `Preferences: Open Keyboard Shortcuts (JSON)` command in order to run tests with a hotkey of your choosing. In this case, I chose F10. 
```json
[
    {
        "key": "f10",
        "command": "testing.runAll"
    }
]
```

### Using a `src` directory

This is the most confusing aspect of structuring a python project to me. I still haven't figured out the optimal way to configure the environment so that everything works, including my IDE. 

### Visual Studio Code environment

I'm checking in my .vscode files to keep track of what needs to be done to configure it to my liking. 

#### act

I will use GitHub actions, so I also wat to set up a way to test those actions locally using `act`:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install act
brew install --cask docker
open -a /Applications/Docker.app
```

This isn't going well so far, but I did get it work through rosetta. See <https://github.com/actions/setup-python/issues/108#issuecomment-1295996059> for details. The key part of the solution is to specify `--container-architecture linux/amd64` when running `act`. 

