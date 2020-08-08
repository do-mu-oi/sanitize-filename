# sanitize-filename
Sanitizes all file names under the specified directory. e.g.: `foo:bar.txt` to `foo_bar.txt`.

## Setup

```bash
$ git clone https://github.com/do-mu-oi/sanitize-filename.git
```

## Usage

```
usage: sanitize.py [-h] [--expression EXPRESSION] [--replacement REPLACEMENT]
                   [--test] [--log LOG]
                   directory

positional arguments:
  directory             target directory

optional arguments:
  -h, --help            show this help message and exit
  --expression EXPRESSION, -e EXPRESSION
                        regular expression pattern (default: [/?<>\\:*|\"])
  --replacement REPLACEMENT, -r REPLACEMENT
                        replacement string (default: _)
  --test, -t            do not make any changes
  --log LOG, -l LOG     CSV log file name
```

## Example

```bash
$ python sanitize.py .
```

## License

MIT License