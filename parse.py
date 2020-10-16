import jsonlines

uuid="9531ba30-90ee-4dd1-afe8-47fd8417701b"


def sum():

    sum = 0
    with jsonlines.open('data.jsonl', mode='r') as reader:
        for obj in reader:
            sum += obj['key']
            
    print(f"Sum of all keys: {sum}")

def search(uuid):
    """Search for entry with a particular UUID"""
    with jsonlines.open('data.jsonl', mode='r') as reader:
        for obj in reader:
            if obj['uuid'] == uuid:
                print(f"Found uuid {uuid}, key {obj['key']}")
                break

