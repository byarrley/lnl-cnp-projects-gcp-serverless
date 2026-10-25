import functions_framework
import random, json

@functions_framework.http
def python_example(request):
    request_json = request.get_json()
    i=0
    count=1
    if request_json and 'count' in request_json:
        count = request_json['count']
    trials=flip_coin(count)
    response = f"Your sequence of {count} trials: {trials}" 

    return json.dumps(response)

def flip_coin(count):
    outcomes=['H','T']
    trials = "".join(random.choices(population=outcomes, k=count))
    return trials

if __name__ == "__main__":
   count=4
   print(f"count={count}, flip_coin result={flip_coin(count)}")
