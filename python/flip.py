import functions_framework
import json

@functions_framework.http
def python_example(request):
    request_json = request.get_json()
    i=0
    count=1
    message = "Hello World"
    if request_json and 'count' in request_json:
        count = request_json['count']
    if request_json and 'message' in request_json:
        message = request_json['message']
    response = [message]*count

    return json.dumps(response)

