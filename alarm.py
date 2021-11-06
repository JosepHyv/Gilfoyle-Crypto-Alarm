#! /usr/bin/python3
'''

	for help

'''
import os 
import sys
import requests
import playsound as player

expectedValue = float(0) #only test
urlApi = "https://api.coinbase.com/v2/exchange-rates?currency="
crypto = "BTC" #default  gilfoyle is BTC
coin = "USD" #default 
times = 30 #time in seconds

def sendMessage(coins, mess):
	if sys.platform.lower() == "darwin":
		os.system("""osascript -e 'display notification "{}" with title "{}"'
                    """.format(str(coins) + " Change:", mess))
	elif sys.platform.lower() == "linux":
		os.system('notify-send "{}" "{}"'.format(str(coins) + " Change:", mess))
	else:
		#procastination for windows :3 
		pass

def queryPrice():
	"""
		return value
		float coin value
	"""
	qry = requests.get(str(urlApi + crypto))
	value = qry.json()["data"]["rates"][coin]
	return float(value)


def plsound(status):
	player.playsound(os.path.join("media", "./{}-notification.mp3".format(status)))
	pass


def launch(price):
	"""
		compare expectedValue  with price
		return values 
		-1 into the range
		0 price down
		1 price up
	"""
	if float(price) < float(expectedValue):			
		sendMessage(crypto, """price dropped below {}{}""".format("{:.2f}".format(float(expectedValue - price)), coin))
		return 0
	elif float(price) > float(expectedValue):
		sendMessage(crypto, """the price rose above {}{}""".format("{:.2f}".format(float(price - expectedValue)) , coin))
		return 1
	else:
		return -1



