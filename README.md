## metanic


### Contributing

The following section discusses the steps necessary to begin contributing to the Metanic services project. It is specifically focused on the Python & backend side of Metanic.

If you are wanting to contribute to a specific user interface, you will need to set up the development environment for the specific client(s) that you want to work on the user interface for.

If you are wanting to contribute by improving or implementing functionality for the data that comes from the API to these clients then you're in the right place.


#### Setting up your Python environment

Firstly, set up your Python environment. Python 3.x is required, and it is recommended to use a virtual environment. Although the virtual environment is optional, not using one can lead to many issues with Metanic as well as potential bugs and breakage within other software written in Python.

Virtual environments allow each Python program to have their own isolated set of installed packages to prevent these issues. If you don't use a virtual environment, please be careful. Developing can be significantly more cumbersome without one.

You can create a virtual environment easily in Python 3.x by executing ` python3 -m venv venv ` which will execute the module *venv* with the argument *venv*. The given argument is the name of the directory which will be created.

Once you've create a virtual environment, you can activate it within your shell. Activating a virtualenv modifies your environment variables so that the right version of Python is used and so that it uses a separate path for dependencies.

When developing in a virtual environment, you need to *activate* it in each shell which you will be running any related Python software in. Assuming that the directory where your virtual environment is called venv, you can use one of the following commands to activate your virtual environment:

- Windows users, run ` .\venv\Scripts\activate ` in Powershell.
- BSD|Linux|MacOS|etc, run ` source venv/bin/activate ` in your shell.


#### Installing Metanic's Dependencies

In a shell wherein your virtual environment is activated, you can now install Metanic's dependencies.

- On Windows, the extra command ` pip install pypiwin32 ` is needed.
- Install dependencies for development with ` python setup.py develop `.