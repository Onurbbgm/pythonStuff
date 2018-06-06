import re
import os
import json
import sys, getopt
import time
from random import randint
def generateJsonUsers(inputfile, outputfile):
    #usersDictionary = {}
    idUserList = []
    with open(inputfile) as json_data:
      tweets = json.load(json_data)
    
    file  = open(outputfile, "a+")
    file.write("[")
    for index in range(len(tweets)):
        tweet = tweets[index]
        if tweet["idUser"] not in idUserList:
            idUserList.append(tweet["idUser"])
            originalFollowers = tweet["followers_count"]
            retweetsTotal = tweet["retweet_count"]
            likesTotal = tweet["likes"]
            number_of_tweets = 1
            raiseOfFollowers = False
            finalFollowers = tweet["followers_count"]
            for index2 in range(index+1, len(tweets)):
                tweUs = tweets[index2]                
                if tweet["idUser"] == tweUs["idUser"]:
                    number_of_tweets += 1                    
                    retweetsTotal += tweUs["retweet_count"]
                    likesTotal += tweUs["retweet_count"]
                    if raiseOfFollowers is True and finalFollowers < tweUs["followers_count"]:
                        finalFollowers = tweUs["followers_count"]
                    elif tweUs["followers_count"] > originalFollowers:
                        raiseOfFollowers = True
                        finalFollowers = tweUs["followers_count"]
            averageRetweets = retweetsTotal/number_of_tweets
            averageLikes = likesTotal/number_of_tweets
            raisedFollowers = "n"
            if raiseOfFollowers is True:
                raisedFollowers = "y"
            file.write("{\n" + "	\"idUser\": \""+tweet["idUser"]+"\",\n"+	  								
                                            "	\"hashtags\": \""+ tweet["hashtags"] +"\",\n" +
                                            "	\"number_of_tweets\": " + str(number_of_tweets) +"," + "\n"+
                                            "	\"retweet_count_total\": " + str(retweetsTotal) +", \n" +
                                            "	\"average_retweet_count\": " + str(averageRetweets) +",\n" +
                                            "	\"followers_count\": " + str(originalFollowers) +",\n" +
                                            "    \"followers_count_increased\": \""+ raisedFollowers + "\",\n"+
                                            "    \"final_followers_count\": "+ str(finalFollowers) + ",\n" +
                                            "	\"total_likes\": " + str(likesTotal) +",\n" +
                                            "    \"average_likes\": " + str(averageLikes) +",\n"+
                                            "    \"nivel_popularidade\": "+ str(randint(0,4)) +"\n"
                                            "\n},\n")
    file.write("\n]")
    file.close()

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile
   start_time = time.time()
   generateJsonUsers(inputfile, outputfile)
   print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
   main(sys.argv[1:])