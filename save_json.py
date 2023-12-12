import json, os, sys
from unicodedata import normalize
import re as regex

def save_json(data, filename):
	# data = json.dumps(data, indent=4, ensure_ascii=False).encode('utf8')
	with open(filename, 'w') as f:
		json.dump(data, f, indent=4, ensure_ascii=False)

# Scanning all folder names in the premade_exemple folder
for folder in os.listdir('premade_exemple'):
	# Scanning all file names in the folder
	data = {}
	try:
		with open('premade_exemple/' + folder + '/desc.txt', 'r') as f:
			data['Desc'] = f.read()
	except:
		data['Desc'] = ''
	try:
		with open('premade_exemple/' + folder + '/name.txt', 'r') as f:
			data['Name'] = f.read()
	except:
		data['Name'] = ''
	save_json(data, 'premade_exemple/' + folder + '/data.json')