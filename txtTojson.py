import re
import os
import json


saveJsonFile = open("C:/Users/Bruno/Desktop/PUC/TCC 2/python-twitter-master/examples/resultOscars2018Day.json", "a+")
idList = []
with open("C:/Users/Bruno/Desktop/PUC/TCC 2/python-twitter-master/examples/resultOscars2018Day.txt", "r") as file:
	  line = file.readline()
	  cnt = 1
	  while line:
	  		if "created" in line:
	  			aux = line.split("id_str\": \"",1)[1]
	  			aux2 = aux.split("\"",1)[0]
	  			print aux2
	  			idList.append(aux2)
	  	  	#print(line)
	  	  	#print("Line {}: {}".format(cnt, line.strip()))
		  	line = file.readline()
		  	cnt += 1


