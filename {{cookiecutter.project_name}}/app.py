# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("{{ cookiecutter.route_url }}")
def {{ cookiecutter.route_function }}():
    return render_template('{{ cookiecutter.template_name }}', title='{{ cookiecutter.title }}', greeting='{{ cookiecutter.greeting }}')

if __name__ == '__main__':
    app.run(debug=True)
