import re
import os
import json

#TODO Remove \ when present in text_content
saveJsonFile = open("C:/Users/Bruno/Desktop/PUC/TCC 2/python-twitter-master/examples/resultOscars2018Day.json", "a+")
idList = []
count = 0
saveJsonFile.write("[")
filetest = open("C:/Users/Bruno/Desktop/PUC/TCC 2/python-twitter-master/examples/teste.txt", "a+")
with open("C:/Users/Bruno/Desktop/PUC/TCC 2/python-twitter-master/examples/resultOscars2018Day.txt", "r") as file:
	  line = file.readline()
	  cnt = 1
	  while line:
	  		if "created" in line:
	  			#auxLineId = line
	  			#auxLineLanguage = line
	  			aux = line.split("id_str\": \"",1)[1]
	  			idTweet = aux.split("\"",1)[0]
	  			auxLanguage = line.split("lang\": \"",1)[1]
	  			language = auxLanguage.split("\"",1)[0]
	  			auxDate = line.split("created_at\": \"",1)[1]
	  			date_time = auxDate.split("\"",1)[0]
	  			retweet = "n"
	  			if "retweet_count" in line:
	  				auxRetweetCount = line.split("retweet_count\": ",1)[1]
	  				retweet_count = auxRetweetCount.split(",", 1)[0]
	  			else:
	  				retweet_count = "0"
	  			if "followers_count" in line:
		  			auxFollowersCount = line.split("followers_count\": ",1)[1]
		  			followers_count = auxFollowersCount.split(",",1)[0]
		  		else:
		  			followers_count = "0"
		  		if "favorite_count" in line:
		  			auxLikes = line.split("favorite_count\": ",1)[1]
		  			likes = auxLikes.split(",",1)[0]
		  		else:
		  			likes = "0"
	  			auxSource = line.split("source\": ",1)[1]
	  			auxText = auxSource.split("text\": \"",1)[1]
	  			text = auxText.split("\"",1)[0]
	  			if "retweeted_status" in line:
	  				retweet = "s"
	  			#print retweet
	  			#print language
	  			#print idTweet
	  			if idTweet not in idList and language == "en":
	  				idList.append(idTweet)
	  				filetest.write(idTweet+"\n")
	  				saveJsonFile.write("{\n" + "	\"id\": \""+idTweet+"\",\n"+
	  									"	\"date_time\": \""+ date_time + "\",\n" +
	  									"	\"hashtags\": \""+  "Oscars\",\n" +
	  									"	\"retweet\": \"" + retweet +"\"," + "\n"+
	  									"	\"retweet_count\": " + retweet_count +", \n" +
	  									"	\"followers_count\": " + followers_count +", \n" +
	  									"	\"likes\": " + likes +", \n" +
	  									"	\"text_content\": \"" + text +"\"\n" +
	  									 "\n},\n")
	  				count+=1	  				 			
	  	  	#print(line)
	  	  	#print("Line {}: {}".format(cnt, line.strip()))
		  	line = file.readline()
		  	cnt += 1

print count	 
saveJsonFile.write("\n]")
filetest.close()
saveJsonFile.close()


