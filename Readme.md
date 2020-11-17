# Py-code-challenges 🐶

![Pipeline](https://github.com/hankazajicova/Py-code-challenge/workflows/Python%20package/badge.svg)

- solutions of code challenges from [Practice Python](https://www.practicepython.org/)

- exercises for [git flow](https://guides.github.com/introduction/flow/) practice

## For local development

- for git pre-commit hooks activation run:

    ```bash
    git config --local core.hooksPath .githooks/
    ```

- for new virtual environment:

    ```bash
    python3 -m venv ./venv
    ```

- activate virtual environment:

    ```bash
    source venv/bin/activate
    ```

- install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

- run solution:

    ```bash
    python3 src/file.py
    ```

- for static analysis used [pylint](https://www.pylint.org/):

    ```bash
    pylint **/*.py --rcfile=.pylintrc
    
    pylint **/*.py --rcfile=.pylintrc_test
    ```

- for static type check used [mypy](http://mypy-lang.org/):

    ```bash
    mypy **/*.py
    ```

- tested with [pytest](https://docs.pytest.org/en/stable/):

    ```bash
    python3 -m pytest
    ```


## Links

- [Python Practice](https://www.practicepython.org/)
- [pylint](https://www.pylint.org/)
- [git flow](https://guides.github.com/introduction/flow/)