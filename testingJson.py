import json
import os
import re

file_path='../TempTwitterDataTest/data/'
data = []
filtered_data = []

han_c = 0
hon_c = 0
den_c = 0
det_c = 0
denna_c = 0
denne_c = 0
hen_c = 0

num_obj = 0
act_obj = 0

BASEDIR="../TempTwitterDataTest/data"
files = os.listdir(BASEDIR)

#print(len(files))
#print(files)

for file in files:
	with open(file_path + file) as fp:
		line = fp.readline()
		while line:
			if line != "\n":
				data.append(line)
				one_data = json.loads(data[num_obj])
				if not one_data.get("retweeted_status"):
					#filtered_data.append(one_data)

					y = re.compile(r'\bhan\b|\bhon\b|\bden\b|\bdet\b|\bdenna\b|\bdenne\b|\bhen\b', re.IGNORECASE)
					x = y.findall(one_data.get("text").lower())

					han_c += x.count('han')
					hon_c += x.count('hon')
					den_c += x.count('den')
					det_c += x.count('det')
					denna_c += x.count('denna')
					denne_c += x.count('denne')
					hen_c += x.count('hen')
					act_obj += 1
				num_obj+= 1
			line = fp.readline()

print("The total number of lines: " + str(num_obj) + "\n")
print("The filtered number of lines: " + str(act_obj) + "\n")

print("Han_c = " + str(han_c))
print("Hon_c = " + str(hon_c))
print("Den_c = " + str(den_c))
print("Det_c = " + str(det_c))
print("Denna_c = " + str(denna_c))
print("Denne_c = " + str(denne_c))
print("Hen_c = " + str(hen_c))
