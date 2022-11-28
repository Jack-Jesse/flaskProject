from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World! :)</h1?'


@app.route('/convert')
@app.route('/convert/<celsius>')
def convert(celsius=""):
    fahrenheit = convert_celsius_to_fahrenheit(float(celsius))
    return f"{fahrenheit}"


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
