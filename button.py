import RPi.GPIO as GPIO
import time
import argparse
import logging
from subprocess import Popen


ap = argparse.ArgumentParser()
ap.add_argument("--red-gpio", type=int, default=7, help="integer: GPIO number of the RED button. default=7")
ap.add_argument("--white-gpio", type=int, default=11, help="integer: GPIO number of the WHITE button default=11")
ap.add_argument("--yellow-gpio", type=int, default=13, help="integer: GPIO number of the YELLOW button. deafult=13")
ap.add_argument("--log-file", type=str, default="button.log", help="string: /path/to/button.log. default=button.log")
ap.add_argument("--red-command", type=str, default="red-button.sh", help="string: /path/to/red-button.sh RED button press script. default=red-button.sh")
ap.add_argument("--white-command", type=str, default="white-button.sh", help="string: /path/to/white-button.sh RED button press script. default=white-button.sh")
ap.add_argument("--yellow-command", type=str, default="yellow-button.sh", help="string: /path/to/yellow-button.sh RED button press script. default=yellow-button.sh")
args = vars(ap.parse_args())


# Logging configuration
logging.basicConfig(filename=args["log_file"],
					level=logging.DEBUG,
					format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s : %(message)s',
					datefmt='%Y-%m-%d %H:%M:%S')


logging.info("Setting up GPIO pins...")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(args["red_gpio"],GPIO.IN)
GPIO.setup(args["white_gpio"],GPIO.IN)
GPIO.setup(args["yellow_gpio"],GPIO.IN)


# Main
logging.info("Started monitoring the state of the buttons!")
try:
	while True:
		red = GPIO.input(args["red_gpio"])
		white = GPIO.input(args["white_gpio"])
		yellow = GPIO.input(args["yellow_gpio"])
		if red == True:
			logging.info("[NOTICE] The RED button was pressed!")
			Popen(["/bin/bash", args["red_command"]])
			time.sleep(.5)
		elif white == True:
			logging.info("[NOTICE] The WHITE button was pressed!")
			Popen(["/bin/bash", args["white_command"]])
			time.sleep(.5)
		elif yellow == True:
			logging.info("[NOTICE] The YELLOW button was pressed!")
			Popen(["/bin/bash", args["yellow_command"]])
			time.sleep(.5)
		time.sleep(.05)
except:
	logging.info("The script was terminated. Cleaning up and exiting...")
	GPIO.cleanup()
	logging.info("Bye!")
