# Web-UI-For-Bedroom-Control
This app will eventually be the main user interface for my raspberry pi bedroom control and monitoring system. 


Build instructions:

It's very important to start the python module first then the nextJS module. The nextJS module doesn't have proper error handling yet so i could fail without error if the python module isn't up.

Python Module: will need to install flask using 'pip install flask'. Then just run the main.py and the raspberry pi server is up and running. You could also use the venv and run bin/python main.py

NodeJS/nextJS module: The command to install the folder is 'npm install'. Next you can run the dev server by typing 'npm run dev' or start the build server by typing npm run build

On Windows see [this](https://github.com/JackClarkeUottawa/Web-UI-For-Bedroom-Control/issues/3#issue-658350269) issue
