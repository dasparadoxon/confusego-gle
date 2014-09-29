# F*CK YOU GOOGLE XD
# VERSION 1.1
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
wordListFile = 'woerterbuch2.txt' # SET YOUR WORDLIST FILENAME HERE
logQuery = True 
numberOfLinesInDictionary = 0
lines = []
secondsToWait = 10
secondsCountedDown = secondsToWait


def readDictionary():
	global lines
	global numberOfLinesInDictionary
	with open(wordListFile) as f:
	    lines = f.read().splitlines()

	numberOfLinesInDictionary = len(lines)

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
			f = open('logfile.txt','a')
			f.write(wortliste[0]+"+"+wortliste[1]+"+"+wortliste[2]+'\n') # python will convert \n to os.linesep
			f.close() # you can omit in most cases as the destructor will call if

		wordsRun1Label[x].configure(text=wortliste[0]+"+"+wortliste[1]+"+"+wortliste[2])

def GoogleTimer():
    
    global secondsCountedDown
    global secondsToWait
    secondsUntilToCallGoogleLabel.configure(text=secondsCountedDown)
    secondsCountedDown = secondsCountedDown-1
    if secondsCountedDown==0:
    	callGoogle()
    	secondsCountedDown=secondsToWait
    root.after(1000, GoogleTimer)

root = Tk()

secondsUntilToCallGoogleLabel = Label(root, text="Calling Google")
secondsUntilToCallGoogleLabel.pack()

wordsRun1Label = []

wordsRun1Label.append(Label(root,text="Three Words 1"))
wordsRun1Label[0].pack()

#wordsRun1Label.append(Label(root,text="Three Words 2"))
#wordsRun1Label[1].pack()

#wordsRun1Label.append(Label(root,text="Three Words 3"))
#wordsRun1Label[2].pack()

GoogleTimer()

root.mainloop()		