# Diff Parser

Simple application for parsing diffs and output changes in nice format.

## Installation

* clone the repository
* enter to the project directory
* create virtual enviroment - `virtualenv env`
* activate virtual enviroment - `. ./env/bin/activate`
* install dependencies `pip install -r requirements.txt`
* run the project `./manage.py runserver`
* open `http://localhost:8000` in browser

## Notes

Application uses modified dependancy [whatthepatch](https://github.com/cscorley/whatthepatch) with additionally
implemented git diff binary files support. [Here is PR](https://github.com/cscorley/whatthepatch/pull/6) for the
implementation fully covered with tests.
