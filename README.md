### Hexlet tests and linter status:
[![Actions Status](https://github.com/AlexanderUridin/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AlexanderUridin/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/8e807bb55565ff5dba42/maintainability)](https://codeclimate.com/github/AlexanderUridin/python-project-50/maintainability)
[![PyCI](https://github.com/AlexanderUridin/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/AlexanderUridin/python-project-50/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8e807bb55565ff5dba42/test_coverage)](https://codeclimate.com/github/AlexanderUridin/python-project-50/test_coverage)

# Difference calculator Project

"Generate diff" is a program that finds the differences between two data structures. Its capabilities:

- Files could be in json or yaml formats, data in files could be flat or nested  
- Package coud be used as CLI utility or library  
- Printing of differences is possible in 3 formats: stylish (default), plain or json

## How to install

```bash
git clone git@github.com:AlexanderUridin/python-project-50.git
cd python-project-50/
install poetry
make install
```

## How to use

Use command `gendiff` and specify pathes to files 

Comparison of two JSON files 
[![asciicast](https://asciinema.org/a/6ZjniA8QIseerPeSXjyuwvfwn.svg)](https://asciinema.org/a/6ZjniA8QIseerPeSXjyuwvfwn)

Comparison of two YAML files  
[![asciicast](https://asciinema.org/a/Go0h5yOWlGjKs90kY807re9os.svg)](https://asciinema.org/a/Go0h5yOWlGjKs90kY807re9os)

Comparison of two nested files 
[![asciicast](https://asciinema.org/a/9FK3jcz7nE4UD9B1oZbPf6KwR.svg)](https://asciinema.org/a/9FK3jcz7nE4UD9B1oZbPf6KwR)

Comparison printed in plain format 
[![asciicast](https://asciinema.org/a/x3R9tEAJ8APBTKNyIF5udvCZg.svg)](https://asciinema.org/a/x3R9tEAJ8APBTKNyIF5udvCZg)

Comparison printed in json format
[![asciicast](https://asciinema.org/a/NImau3aVI761Vbrz8D5JKoK7D.svg)](https://asciinema.org/a/NImau3aVI761Vbrz8D5JKoK7D)