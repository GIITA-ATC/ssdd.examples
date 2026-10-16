from flask import Flask, request

app = Flask(__name__)
doors = {'door1': {'percentage_open': 0}}

@app.get('/devices/<door_id>')
def read_door(door_id):
    if door_id not in doors:
        return {'error': 'not found'}, 404
    return doors[door_id]

@app.put('/devices/<door_id>')
def update_door(door_id):
    doors[door_id] = {'percentage_open': request.json['percentage_open']}
    # side effect: move the motor
    return doors[door_id]

app.run(port=5001)
