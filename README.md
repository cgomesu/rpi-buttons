# Description
This is a simple python script to run customized commands using three push buttons connected to a Raspberry Pi 3B's general purpose input/output (GPIO) pins.  (Of course, it's also compatible with RPi 3B+ and any other RPi that has the same GPIO version as the 3B.)

# Materials
- 1x mini-breadboard
- 3x push button
- 5x male-to-female dupont compatible jumper cable
- 4x male-to-male simple jumper cable
- 3x 1k ohms resistor
- 3x 10k ohms resistor

# Wiring
- The recommended circuit features a current limiting resistor (1k ohms) as well as a pull-down resistor (10k ohms)

![rpi 4b wiring](https://i.imgur.com/IfLnKS6.png)

# Installation
- Raspbian OS:
```
apt-get update
apt-get install git
cd /opt
git clone https://github.com/cgomesu/rpi-buttons.git
# IFF you have permission issues, run 'sudo chown -R pi:sudo rpi-buttons' to change the folder ownership to user pi.
cd rpi-buttons
# Add a command that will be executed whenever each button is pressed):
nano red-button.sh
nano white-button.sh
nano yellow-button.sh
# Run the script
python3 button.py
# Check log
tail -f /opt/rpi-buttons/button.log
```

# Usage
```
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
```

# Running as a service (systemd)
```
# IFF you have permission issues, just add 'sudo' before each command
cp /opt/rpi-buttons/systemd/button-rpi.service /lib/systemd/system/
systemctl enable button-rpi.service
systemctl start button-rpi.service
# Check status it's running without issues
systemctl status button-rpi.service
# Check log
tail -f /opt/rpi-buttons/button.log
```
