# Python-Excel-Writer

## Getting started

This is a python program that retrieves data from a mySQL DB and places this data into an excel sheet.
Note that this program is intended to be run with Python 3, therefore, for systems running Python version 2, it is recommended
to create a virtual Python 3 environment using __pyenv__.
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
DB_USERNAME=... # your mysql DB username
DB_PASSWORD=... # your mysql DB password
```
Note that *.env* has been added to the gitignore file so that these secrets will not be committed to git.

Following this, you can run the application by running the following command from the root folder of the repository in your terminal (ensure you use Python 3 for this):
```bash
$ python xls_writer.py
```
An excel sheet called ```valor.xlsx``` populated with the data from the DB should now have been created in the root folder of the repository.