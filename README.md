# rpi
A small collection of conveninence code for my personal experiments with the RPi.
# System-level Installation
Clone the repo:

    git clone https://github.com/ephsmith/rpi.git

Change to the top-level repo dir and install using `pip3`:

    cd rpi && pip3 install .

# Installing into a virtual environment (better)
`virtualenvwrapper` is probably the fastest way to start using Python virtual environments if you aren't already.

## Install `virtualenvwrapper`
The
[Basic Installation guide](http://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation)
is a great place to start. However...

If you prefer not to follow the install guide, these commands will
get you up and running quickly on the RaspberryPi:

~~~ bash
sudo pip3 install virtualenv virtualenvwrapper
echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc
~~~

## Create the virtual environment.
For RaspberryPi projects, its best to configure your virtual environment to use site-packages so that modules like RPi.GPIO are still accessible.  Modules here require RPi.GPIO. Create the virtual env like so:

    mkvirtualenv --python=python3 --system-site-packages <env-name-here>

`virtualenvwrapper` will create the virtualenv directory under the
`WORKON_HOME` directory and activate it. Your prompt should indicate
this with the env name in parens--like so:

~~~ bash
(env-name-here) user@pi$
~~~

## Install the `rpi` package.
Change to the top-level project directory and run

    pip install .

# Importing the modules
Here's an example that imports the `ussensor` module and reads a distance measurement.

~~~ python
from rpi.ussensor import ussensor

sensor = ussensor(echo=17, trigger=4, poll=True)
print(sensor.distance())
~~~

*Note*: If you installed into a virtual environment, you'll need to
 activate the venv *prior to executing the script*.

The `Arm` class is currently useful for the LynxMotion AL5B/SSC-23U
combination. Here's an example:

~~~ python

from rpi.arm import Arm
import serial

com = serial.Serial('/dev/ttyUSB0', 9600)
a = Arm(com=com)

# Set all servo positions to midpoint on the AL5B
a.move()
~~~

Here's a quick example that interfaces a NewHaven LCD display and
reports a message:

~~~ python
import serial
from rpi.lcd import lcd

com = serial.Serial('/dev/ttyS0', 9600)
disp = lcd(com=com)

disp.display_clear()
disp.text('Hello World')
~~~

# Examples
Examples are available under the `examples` directory.
