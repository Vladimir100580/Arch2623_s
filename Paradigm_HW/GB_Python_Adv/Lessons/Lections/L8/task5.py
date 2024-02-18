import json
a = 'Hello world!'
b = {key: value for key, value in enumerate(a)}
c = json.dumps(b, indent=3, separators=('; ', '= '))
print(c)    # срока лишь напоминающая JSON, т.к. поменяли разделители. (Должны быть "," и ":")
