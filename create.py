from uuid import uuid4
import jsonlines

N=1000000
data = [ {'uuid': str(uuid4()), 'key': 1 } for _i in range(N) ]

with jsonlines.open('data.jsonl', mode='w') as writer:
    for line in data:
        writer.write(line)

