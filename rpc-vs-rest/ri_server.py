from flask import Flask, request

app = Flask(__name__)
doors = {'door1': {'percentage_open': 0}}

@app.put('/devices/<door_id>')
def execute(door_id):
    msg = request.json
    if msg['operation'] == 'open':
        doors[door_id] = {'percentage_open': msg['args'][0]}
        return {'result': 'ok'}

    if msg['operation'] == 'getOpening':
        return {'result': doors[door_id]['percentage_open']}

    return {'error': 'unknown operation'}, 400

app.run(port=5001)

# Other option:

# @app.post('/devices/<door_id>/open')
# def open_door(door_id): ... msg = {'args': [20]}

# @app.post('/devices/<door_id>/getOpening')
# def get_opening(door_id): ... msg = {'args': []}
