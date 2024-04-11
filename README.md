# Cookiecutter Flask Simple

This is a simple Cookiecutter template for generating Flask projects.

## Features

- Minimal Flask project structure.
- Basic app.py file with a single route.
- Example static and templates directories with placeholder files.
- Easily customizable with Cookiecutter variables.

## Usage

To generate a new Flask project using this Cookiecutter template, follow these steps:

1. Install Cookiecutter if you haven't already:

    ```
    pip install cookiecutter
    ```

2. Run Cookiecutter and provide the path to this Cookiecutter template:

    ```
    cookiecutter https://github.com/sureshguru18/cookiecutter-flask-simple
    ```

3. Follow the prompts to provide values for the variables defined in the Cookiecutter template.

4. Once completed, you'll have a new Flask project generated based on the provided values.

## Directory Structure

After generating a project using this template, you'll have the following directory structure:
```bash
my_flask_app/
│
├── app.py
├── static/
│ └── (static files like css, js, images)
│
├── templates/
│ └── (HTML templates)
│
└── requirements.txt
```

- `app.py`: The main Flask application file with a basic route.
- `static/`: Directory for static files like CSS, JavaScript, and images.
- `templates/`: Directory for HTML templates.
- `requirements.txt`: File listing the dependencies of the project.

## Running the Flask Application

To run the Flask application locally, navigate to the project directory and run:


This will start the development server, and you can access the application in your web browser at `http://127.0.0.1:5000/`.

