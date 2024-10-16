# QGFX

Quick graphics library for the TI-84 Plus CE-T Python Edition

## Description

An improved version of the built in ti_graphics library on the TI-84 Plus CE-T Python Edition graphing calculator.
This library uses ```sys.stdout.write``` instead of ```print``` to avoid unnecessary flushing of graphics commands, as well as adding some more useful features such as the ```Color``` class.

## Getting Started

### Installing

* Put QGFX.py and QGFX_COL.py with your python programs on the graphing calculator.

### Drawing Things

* ```import QGFX``` at the top of your program
* Use whatever graphics commands you want, such as: ```QGFX.draw_line(0,0,100,100)```
* Use ```QGFX.flush()``` in order to flush any graphics commands to the screen

## Authors

ZyberDev

## Version History

* 1.0
  * Initial Release

## License
This project is licensed under the MIT License - see the LICENSE file for details
