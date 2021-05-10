#!/usr/bin/python
# Air suspension controller

##### Start
print("Starting air suspension system.")

##### Imports
import time
import hw

##### Set up hardware
hw.init()

##### Main
print("Pitch: "+hw.getPitch())


# Cleanup
hw.cleanup()

