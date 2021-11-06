import os
import time
import alarm
import schedule
import argparse
from sys import platform
from datetime import datetime

try:
	with open (os.path.join("media", "coins.txt"),"r" ) as file:
		data = file.read().rstrip()
except Exception as e:
	print("found exception {}".format(str(e)))

textHelp = """

		Gilfoyle Crypto Alarm

		supported crypto ocurrency 

		|  BTC: BITCOIN      |
		|  ETH: ETHERUM      |
		|  BCH: BITCOIN CASH |
		|  ZEC: ZCASH        |
		|  LTC: LITECOIN     |
		|  XRP: XRP          |

		foreign exchange supported

		{}


		Default data 
		Crypto = BTC
		foreign exchange = USD

""".format(str(data))


def main():
	#print(textHelp)
	arguments = argparse.ArgumentParser(description="""Gilfoyle Crypto Alarm
		Set an alarm and run it when your favorite cryptocurrency rises or falls more than 
		your desired price in your chosen currency 
		supported crypto {}""".format(str(alarm.supportedCrypto)))
	arguments.add_argument("-d", "--D", type=str, default="USD",help="Select the foreign exchange Default = USD")
	arguments.add_argument("-c", "--C", type=str, default="BTC",help="Select the cryptocurrency Default = BTC")
	arguments.add_argument("-t", "--T", type=int, default=30, help="time in seconds Default = 30 seconds")
	arguments.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")
	requiredNames = arguments.add_argument_group("required named arguments")
	requiredNames.add_argument("-l", "--L", type=float, help="type your limit in foreign exchange value", required=True)
	args = arguments.parse_args()

	run(args)

def date():
	"""
		month / day at hour:minute
	"""
	aux = str(datetime.now())
	dates = aux[5:10]
	hours = str(datetime.now())[11:16]
	#print("dates tiene -> ",  dates, "lo demas es " + str(datetime.now())[5:5] )
	return "date: {} at {}".format(dates,hours)

def run(args):

	if args.C.upper() in alarm.supportedCrypto:
		alarm.crypto = args.C.upper()
	else:
		print("Error Crypto {} not supported".format(args.C))
		print("using Default {}".format(alarm.crypto))

	if args.D.upper() in data:
		alarm.coin = args.D.upper()
	else:
		print("Error foreign exchange {} not supported".format(args.D))
		print("using Default {}".format(alarm.coin))

	times = args.T
	alarm.expectedValue = args.L

	lastPrice = float(0)
	minPrice = [float("inf"), date()]	
	maxPrice = [float("-inf"), date()]
	
	try:

		while True:
			current = float(alarm.queryPrice())
			option = alarm.launch(alarm.queryPrice())
			if option == 0:
				alarm.plsound("down")
			elif option == 1:
				alarm.plsound("upper")
			else:
				print("price on limits")
		
			print("""
			{} -> info:

			last in {}: {}
			best {} in {}
			worst {} in {}""".format(alarm.crypto, alarm.coin, "{:.2f}".format(lastPrice), "{:.2f}".format(minPrice[0]), minPrice[1], "{:.2f}".format(maxPrice[0]), maxPrice[1]))
		
			if minPrice[0] > current:
				minPrice[0] = current
				minPrice[1] = date()
			if maxPrice[0] < current:
				maxPrice[0] = current
				maxPrice[1] = date()
			lastPrice = current
		
			time.sleep(times)
	except KeyboardInterrupt:
		print("\nClosing gilfoyle")

	

if __name__ == "__main__":
	main()