# Description
This is a simple python script to run customized commands using three push buttons connected to a Raspberry Pi 3B's general purpose input/output (GPIO) pins.  (Of course, it's also compatible with RPi 3B+ and any other RPi that has the same GPIO version as the 3B.)

# Wiring
- The recommended circuit features a current limiting resistor (1k ohms) as well as a pull-down resistor (10k ohms)
![rpi 4b wiring](https://i.imgur.com/IfLnKS6.png)

# Usage
``
python3 button.py --help
usage: button.py [-h] [--red-gpio RED_GPIO] [--white-gpio WHITE_GPIO]
                 [--yellow-gpio YELLOW_GPIO] [--log-file LOG_FILE]
                 [--red-command RED_COMMAND] [--white-command WHITE_COMMAND]
                 [--yellow-command YELLOW_COMMAND]

optional arguments:
  -h, --help            show this help message and exit
  --red-gpio RED_GPIO   integer: GPIO number of the RED button. default=7
  --white-gpio WHITE_GPIO
                        integer: GPIO number of the WHITE button default=11
  --yellow-gpio YELLOW_GPIO
                        integer: GPIO number of the YELLOW button. deafult=13
  --log-file LOG_FILE   string: /path/to/button.log. default=button.log
  --red-command RED_COMMAND
                        string: /path/to/red-button.sh RED button press script. default=red-button.sh
  --white-command WHITE_COMMAND
                        string: /path/to/white-button.sh RED button press
                        script. default=white-button.sh
  --yellow-command YELLOW_COMMAND
                        string: /path/to/yellow-button.sh RED button press
                        script. default=yellow-button.sh
``
