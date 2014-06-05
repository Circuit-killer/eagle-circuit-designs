# Zero crossing triac controller Arduino Shield

An arduino shield that makes it easy to detect [zero crossings](http://en.wikipedia.org/wiki/Zero_cross_circuit) on mains AC, and control a triac with [phase control](http://playground.arduino.cc/Main/ACPhaseControl)

# Circuit board

* [Schematic](schematic.png)
* Eagle schematic/board in the repo
* order boards from [oshpark](http://oshpark.com/shared_projects/XGqh7Sy8)

# BOM

The [BOM](bom.txt) is in tab separated form, with Farnell part numbers. Missing parts are standard, or don't matter:

* Diodes are forming a low current bridge rectifier
* Caps - follow voltage and polarisation.
* Reistors - power rating 1/8W unless specified.

# Useful resources

I made use of the following in the design.

## Spindle controller

Thanks to Klaas for a great write up on a [cnc router controller](https://sites.google.com/site/klaasdc/cnc-router/spindle-controller) of which this project is mostly a copy of.

## Triac Block

Thanks to Mic at [wemakethings.net](http://wemakethings.net) for his work on the Triac Bloc:

* [git repo](https://github.com/Miceuz/triac-bloc)
* [pdf schematic](https://github.com/Miceuz/triac-bloc/blob/master/ssr.pdf)

## Triac controller datasheet

* This [opto isolated triac controller](http://www.farnell.com/datasheets/1806097.pdf) datasheet has a useful circuit for controlling triac including snubber circuit.

## Zero crossing circuit

* [Zero crossing circuit](http://www.dextrel.net/diyzerocrosser.htm)