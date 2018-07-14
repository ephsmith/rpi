# sp_goofy_theramin
These two scripts comprise a silly experiment inspired by a raspberrypi.org tutorial.

# Try it out
Prerequisites:
 - Sonic Pi (tested with version 3.01)
 - `pythonosc`
 - `ussensor.py`
 - hardware installation of HC-SR04 (see `ussensor.py`)

1. Save `ussensor.py` to a location on your python path
2. Open `sp_goofy_theramin.rb` in Sonic Pi and click "Run"
3. Issue `python -m sp_goofy_theramin.py`
4. Wave like you just don't care... in front of the HC-SR04 of course.

# Notes
The function `clip_and_scale` handles input/output range adjustment to *hopefully* produce a range of MIDI note numbers that aren't painful. In `sp_goofy_theramin.py`, the input/output ranges are set using the `opts` `dict`. Adjust as needed for the situation.
