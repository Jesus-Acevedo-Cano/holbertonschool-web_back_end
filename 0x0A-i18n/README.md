# 0x0A-i18n

## Objectives

- Learn how to parametrize Flask templates to display different languages
- Learn how to infer the correct locale based on URL parameters, user settings or request headers
- Learn how to localize timestamps

## Tasks 

- ### 0. Basic Flask app
      Setup a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton”

- ### 1. Basic Babel setup
      Install the Babel Flask extension:
            $ pip3 install flask_babel
      Then instantiate the Babel object in your app. Store it in a module-level variable named babel.
