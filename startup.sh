#!/bin/bash

echo "Starting listeners for reboot and shutdown"
sudo -- bash -c 'echo -e "HTTP/1.1 200 OK\r\nSuccessful" | nc -lN 81; reboot'&
sudo -- bash -c 'echo -e "HTTP/1.1 200 OK\r\nSuccessful" | nc -lN 82; shutdown -h now'&

echo "Waiting for gateway route"
GATEWAY=""

while [[ $GATEWAY == "" ]]; do
   GATEWAY=`ip route | grep -Po "via \d+\.\d+\.\d+\.\d+" | grep -Po "\d+\.\d+\.\d+\.\d+"`
done

echo "Waiting for gateway response"
# Wait until gateway respond to ping
while [[ $(ping -c 1 -w 1 $GATEWAY) == "" ]]; do
   sleep 2
done

echo "Attempting git pull"
cd /home/pi/rvairsuspension
git pull

echo "Post-boot script loaded. Calling main.py"
src/main.py

