# PyFraCalc - Fraction Calculator in Python

## Requisites

- Python 3.x
- ANTLR 4.x

On Ubuntu Linux 24.04 you need to install a number of packages:

A simple fraction calculator written in Python with a lexer/parser in ANTLR 4.x.

```sh
python3 src/main.py "1/2 + 2/3"
```

```sh
sudo apt install antlr4
```

A simple fraction calculator written in Python with a lexer/parser in ANTLR 4.x.

```sh
python3 src/main.py "1/2 + 2/3"
```

## Requisites

- Python 3.x
- ANTLR 4.x

On Ubuntu Linux 24.04 you need to install a number of packages:

```sh
sudo apt install antlr4 python3-antlr4
```

## Building

You can generate the lexer and parser with the following command:

```sh
antlr4 -Dlanguage=Python3 calculator.g4
```
