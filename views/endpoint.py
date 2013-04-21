from flask import Response

def serve_json(name):
    with open(name, 'r') as f:
        result = f.read()

        return Response(result, status=200, mimetype='application/json')

def search():
    return serve_json('fake/search.json')