#!/usr/bin/python
# Air suspension controller

##### Start
print("Starting air suspension system.")

##### Imports
import time
import hw

##### Set up hardware
hw.init()

##### Toggle switch

# Activate
sensorFeed(True)
time.sleep(1)
sensorFeed(False)

# Cleanup
hw.cleanup()

