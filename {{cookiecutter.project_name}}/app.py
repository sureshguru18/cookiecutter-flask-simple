from flask import Flask, render_template

app = Flask(__name__)

# {{ cookiecutter.route_name }} will be replaced by the user-provided route name
@app.route('{{ cookiecutter.route_url }}')
def {{ cookiecutter.route_function }}():
    return render_template('{{ cookiecutter.template_name }}')

if __name__ == '__main__':
    app.run(debug=True)

