[![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/80x15.png)](https://creativecommons.org/licenses/by/4.0/)

# Critical Response Talk
By Jacob Stoebel

This is a talk on Liz Lerman's [Critical Response Process](https://lizlerman.com/critical-response-process/). See [slides.md](slides.md) for more information. It began as a talk at [PyOhio 2017](https://pyohio.org/) and will be given at [Ruby Conf 2017](http://rubyconf.org/program#session-214)

This slide show is written using remark.js. All dependencies are local (no Internet connection needed). Just load `index.html` in any browser and you're good to go!

## Presentation Hotkeys

_taken from remark github_ 
Press C to clone a display; then press P to switch to presenter mode. Open help menu with h.

## Building the presentation

Remark allows you to include slides from a separate `.md` file, but chrome and possibly other browsers does not let javascript access other files when using the `file` protocol. To solve this we _could_ spin up a web server to serve `index.html` but...bleg. We could also drop the content from `slides.md` directly into an html file but that's confusing for most text editors. Instead, we're using a python script to "build" the presentation (really just inserting the markdown contents into `index.html`). This repo should come pre built (meaning `index.html`) is ready to load in any browser, but if you want to make changes you'll need to run `build.py` to rebuild the project. To do so:

1. Spin up a virtual environment (optional but recommended)
1. run `pip install -r requirements.txt`
1. run `python build.py`

`index.html` should contain your updates.
