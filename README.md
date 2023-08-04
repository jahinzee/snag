# snag
A super-simple down-to-the-wire "framework" for building websites with shell scripts.

## Dependencies

This app relies on two external dependencies: BeautifulSoup and htmlmin.

If you are using `pip`, you can install them using

```
$ pip install -r requirements.txt
```

If you are using an externally managed Python environment, like in most Linux distributions, please refer to your package manager's listings for the correct packages to install.

### Fedora

On Fedora 38+, the dependencies can be installed with:

```
# dnf install python3-beautifulsoup4 python3-htmlmin
```

## Command-line Usage

```
snag [--help | --settings]
```
- `--help`: Shows the help message.
- `--settings`: Generates a settings file.

## General Usage

For more information, see the [Getting Started](GETTING_STARTED.md) guide.
