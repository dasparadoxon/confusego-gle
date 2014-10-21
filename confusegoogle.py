# CONFUSE GO*GLE
# FORMER F*CK YOU GO*GLE XD
# VERSION 1.2
#
# CREATING RANDOM QUERIES
# RUN THIS SCRIPT A FEW TIMES A DAY
# OR WHEN YOUR COMPUTER IS IDLE
# YOU WILL NEED A WORDLIST WITH WORD ONE EVERY LINE 
# SHOULD WORK UNDER WINDOWS, MAC AND LINUX
# USING TKINTER AS GUI KIT

from Tkinter import *
from random import randint
import urllib
import webbrowser
import time

inBrowser = False; # SET THIS TO TRUE IF YOU WANT TO SEE THE RESULTS IN YOUR BROWSER
wordListFile = 'defaultWordList.txt' # SET YOUR WORDLIST FILENAME HERE
numberOfLinesInDictionary = 0 # INTERNAL COUNTER OF WORDS IN DICTINOARY
lines = [] # INTERNAL GLOBAL BUFFER OF WORDS IN DICTIONARY
secondsToWaitAtLeast = 60  # EVERY SO AND SO MANY SECONDS AT LEAST TO DO A GOOGLE SEARCH QUERY
secondsToWait = 0
secondsCountedDown = secondsToWait # INTERNTAL COUNTER


#LOGGING
nameOfLogFile = 'logfile.txt';
logQuery = True # SET THIS TO TRUE IF WANT YOUR QUERIES TO BE LOGGED
numberOfQuerysSoFar = 0


def readDictionary():
	global lines
	global numberOfLinesInDictionary
	with open(wordListFile) as f:
	    lines = f.read().splitlines()

	numberOfLinesInDictionary = len(lines)

def readLogLines():
	loglines = []
	global numberOfQuerysSoFar
	with open(nameOfLogFile) as f:
	    loglines = f.read().splitlines()

	numberOfQuerysSoFar = len(loglines)	

def callGoogle():

	readDictionary()

	numberOfRuns = 1

	for x in range(0, numberOfRuns):

		wortliste = []

		wortliste.append(lines[randint(1,numberOfLinesInDictionary-1)])
		wortliste.append(lines[randint(1,numberOfLinesInDictionary-1)])
		wortliste.append(lines[randint(1,numberOfLinesInDictionary-1)])

		url = "https://www.google.de/?#q="+wortliste[0]+"+"+wortliste[1]+"+"+wortliste[2]

		if inBrowser == True:
			webbrowser.open_new_tab(url)

		if inBrowser == False:
			webpage = urllib.urlopen(url)
			erg = webpage.read()

		if logQuery == True:
			f = open(nameOfLogFile,'a')
			f.write(wortliste[0]+"+"+wortliste[1]+"+"+wortliste[2]+'\n') # python will convert \n to os.linesep
			f.close() # you can omit in most cases as the destructor will call if

		wordsRun1Label[x].configure(text=wortliste[0]+"+"+wortliste[1]+"+"+wortliste[2])

def GoogleTimer():
    
    global secondsCountedDown
    global secondsToWait
    global secondsToWaitAtLeast
    global logQuery
    global numberOfQuerysSoFar
	
    secondsUntilToCallGoogleLabel.configure(text=secondsCountedDown)
    secondsCountedDown = secondsCountedDown-1
    if secondsCountedDown==0:
    	callGoogle()
	secondsToWait = randint(1,secondsToWaitAtLeast-1);
    	secondsCountedDown=secondsToWait
    	if logQuery==True:
                global LogLinesLabel
                numberOfQuerysSoFar = numberOfQuerysSoFar + 1
                LogLinesLabel.configure(text=numberOfQuerysSoFar)
                
 
    root.after(1000, GoogleTimer)

root = Tk()

#secondsToWait = randint(1,secondsToWaitAtLeast-1);
secondsCountedDown = 1


secondsUntilToCallGoogleLabel = Label(root, text="Calling Google")
secondsUntilToCallGoogleLabel.pack()

wordsRun1Label = []

wordsRun1Label.append(Label(root,text="Three Words 1"))
wordsRun1Label[0].pack()

#wordsRun1Label.append(Label(root,text="Three Words 2"))
#wordsRun1Label[1].pack()

#wordsRun1Label.append(Label(root,text="Three Words 3"))
#wordsRun1Label[2].pack()

LogLinesLabel = Label(root, text=numberOfQuerysSoFar)

if logQuery==True:
        global LogLinesLabel
        readLogLines();
        LogLinesLabel.pack()

GoogleTimer()

root.mainloop()		
