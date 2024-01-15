# Shorten url application

## Install Python on Linux
The following command could be used to install the latest version of Python on almost every Linux system.
```bash
$ sudo apt-get update
$ sudo apt-get install python3
```
Also, you can mention the particular version of Python you want to install, shown below :
```bash
$ sudo apt-get install python3.8
```

To check if your system has any Python Version already Installed:
```bash
$ python3 --version
```

## Setup a virtual environment
Virtualenv is a tool to set up your Python environments.

Install venv to your host Python by running this command in your terminal:
```bash
$ pip3 install virtualenv
```

You can install python-pip3 with command:
```bash
$ sudo apt-get install python3-pip
```

Move to the project folder in your terminal, and run the following command to create virtual environment for project:
```bash
$ python3 -m venv <virtual-environment-name>
```
Then, activate the venv to use.
```bash
$ source ./<virtual-environment-name>/bin/activate
```

## Getting started

### Setup requirements for project
First ensure that you have the necessary dependencies installed.
```bash
$ sudo apt-get install libpq-dev python3-dev
```

Install required packages.
```bash
$ pip3 install -r requirements.txt
```

### Running the code
Run the server using `uvicorn`.
```bash
$ uvicorn app.main:app --reload
```

`--reload` option is used to enable auto-reloading of application during development

### Running unit testing
You can unit test the project with command `pytest`:
