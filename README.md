# Python-Excel-Writer

## Getting started

This is a python program that retrieves data from an SQL server and places this into an excel sheet.
This program is not Python 3 compatible, therefore, for systems running Python version 3 or higher, it is recommended
to create a virtual Python 2 environment using __pyenv__.
The project uses a virtual environment to isolate package dependencies. 
To create the virtual environment and install required packages, run the following from a bash shell terminal:

### On macOS and Linux
```bash
$ source setup.sh
```
### On Windows (Using Git Bash)
```bash
$ source setup.sh --windows
```

Once the setup script has completed and all packages have been installed, add the following variables to the *.env* file:
```
HOST=... # your mysql DB host
DATABASE=... # your mysql DB
USERNAME=... # your mysql DB username
PASSWORD=... # your mysql DB password
```
Note that *.env* has been added to the gitignore file so that these secrets will not be commited to git.
