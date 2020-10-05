from collections import Counter
from flask import jsonify
from tasks import file_function
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def counter():
	total_count = Counter({'han':0, 'hon':0, 'den':0, 'det':0, 'denna':0, 'denne':0,'hen':0})
	path = "/home/ubuntu/data"
	dir_list = os.listdir(path)
	for name in dir_list:
		ind_file_count=file_function.delay(name)
		#result=ind_file_count.ready()
		while ind_file_count.ready() is not True:
			print("Processing...")
		print(type(total_count))
		result=ind_file_count.get(timeout=1)
		m=Counter(result)
		print(type(m))
		total_count= m + total_count
		#print(type(total_count))
		#print(type(result))
	print(total_count)
	return total_count
if __name__ == '__main__':
    #app.debug = True
    app.run(host='0.0.0.0', port=5000)
