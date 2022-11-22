# front-diff-checker
(name subject to changes.)

Using Selenium and its BrowserDrivers, it take's screenshots and compare them to get differences between two given environments.

Require python3.10

# Usage

```shell
usage: script.py [-h] [-s URL] [-t URL] [-k] [-p] [-o] [-w WARMUP_TIME] [-v] [-b BROWSER]

Take screenshot and compare them to get differences between two given environments

options:
  -h, --help            show this help message and exit
  -s URL, --source URL  The source website URL
  -t URL, --target URL  The target website URL
  -k, --keep-files      Keep files after comparison
  -p, --purge-files     Remove files before take screenshots
  -o, --open-result     Show result picture once it generated
  -w WARMUP_TIME, --warmup-time WARMUP_TIME
                        Wait before starting Selenium once it's driver is ready (seconds)
  -v, --verbose         Add some debug texts
  -b BROWSER, --browser BROWSER
                        Browser used by Selenium to run screenshot
```

# Example

```shell
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python script.py -s https://fr.wikipedia.org/wiki/Tatenectes -t https://fr.wikipedia.org/wiki/Genre_\(biologie\) -o -v -k
```

# Testing API endpoints with Swagger

```shell
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r dev-requirements.txt
$ python -m uvicorn api:app --reload
```

Then open [Swagger endpoint](http://127.0.0.1/docs/) to test API

:warning: Current UVICORN settings are not designed for production needs.

Use with caution and check [this documentation page](https://www.uvicorn.org/deployment/) first.

# Build

```shell
$ python -m pip install pip --upgrade
$ pip install -r build-requirements.txt
$ python -m build
```

This will generate new package into `./dist/` folder.
You'll need to edit `./pyproject.toml` file in order to fit your needs.
