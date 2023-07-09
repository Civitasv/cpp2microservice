from flask import Flask, jsonify
from plugin.addition import add
from plugin.method_in_A import static_method
from plugin.person import create_person, delete_person, print_person

app = Flask(__name__)


@app.route('/add', methods=['GET'])
def _add():
    result = add(3, 4)

    return jsonify(result)


@app.route('/static', methods=['GET'])
def _static_method():
    result = static_method()

    return jsonify(result)


@app.route('/person', methods=['GET'])
def _person():
    p = create_person("husen", 18)
    val = print_person(p)

    delete_person(p)

    return jsonify(val)
