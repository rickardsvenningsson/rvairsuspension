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
hw.sensorFeed_on()
time.sleep(1)
hw.sensorFeed_off()

# Cleanup
hw.cleanup()

