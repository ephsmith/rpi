# rpi
A small collection of conveninence code for my personal experiments with the RPi.
# System-level Installation
Clone the repo:

    git clone https://github.com/ephsmith/rpi.git

Change to the top-level repo dir and install using `pip3`:

    cd rpi && pip3 install .

# Using a virtual environment (better)
`virtualenvwrapper` is probably the fastest way to start using Python virtual environments if you aren't already.

Install `virtualenvwrapper` using the [Basic Installation guide](http://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation).

For RaspberryPi projects, its best to configure your virtual environment to use site-packages so that modules like RPi.GPIO are still accessible.  Modules here require RPi.GPIO. Create the virtual env like so:

    mkvirtualenv --python=python3 --system-site-packages <env-name-here>

`virtualenvwrapper` will create the virtual env and activate it (your prompt should indicate this.

Change to the top-level project directory and run `pip install .`.  
