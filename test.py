import json
import re

count_han=0
count_hon=0
count_den=0
count_det=0
count_denna=0
count_denne=0
count_hen=0

with open('sample2') as f:
    for line in f:
	if line.strip():
		data=json.loads(line)
		if data['retweet_count']== 0:
			string=data['text'].lower()
			print(string)
		#print(data['text'])
			data_split=string.split()
			if sum(1 for match in re.finditer(r"\bhan\b",string)) >0:
				count_han  += 1
			if sum(1 for match in re.finditer(r"\bhon\b",string)) >0:
				count_hon += 1
			if sum(1 for match in re.finditer(r"\bden\b",string)) >0:
				count_den +=1
			if sum(1 for match in re.finditer(r"\bdet\b",string)) >0:
				count_det +=1
			if sum(1 for match in re.finditer(r"\bdenna\b",string)) >0:
				count_denna +=1
			if sum(1 for match in re.finditer(r"\bdenne\b",string)) >0:
				count_denne +=1
			if sum(1 for match in re.finditer(r"\hen\b",data['text'])) >0:
				count_hen +=1

#print("han number ",count_han)
#print("hon number ",count_hon)
#print("den number ",count_den)
#print("det number ",count_det)
#print("denna number ",count_denna)
#print("denne number ",count_denne)
#print("hen number ",count_hen)

D = dict( han = count_han, hon = count_hon, den = count_den, det = count_det, denna = count_denna, denne=count_denne, hen=count_hen)
print(D)
