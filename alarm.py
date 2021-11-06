#! /usr/bin/python3
'''

	for help

'''
import os 
import sys
import time
import schedule 
import requests
import playsound as player

expectedValue = float(0)

def sendMessage(coins, mess):
	if sys.platform.lower() == "darwin":
		os.system("""osascript -e 'display notification "{}" with title "{}"'
                    """.format("Change In: " + str(coins), mess))
	elif sys.platform.lower() == "linux":
		os.system('notify-send "{}" "{}"'.format("Change in: " + str(coins), mess))
	else:
		#procastination for windows :3 
		pass


def alert(price):
	sendMessage("BTC", "upper over $1200MXN")
	player.playsound(os.path.join("media","./notification.mp3"))
	pass

def main():
	alert(0)

	#algo 

if __name__ == "__main__":
	main()