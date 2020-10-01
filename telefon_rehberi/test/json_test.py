import json

obj = {"yusa": "yazilimci"}
path = "telefon_rehberi/res/test.json"


with open(path, "w") as file:
	json.dump(obj, file, indent=4)

with open(path) as file:
	print(json.load(file))
