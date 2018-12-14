#!/usr/bin/env bash

sudo gnome-terminal -e "sudo python3 consumer_cm_alive.py" --title="District Heating Potential: consumer_cm_alive dh_potential"

sudo gnome-terminal -e "sudo python3 run.py" --title="District Heating Potential: run CM"

sudo gnome-terminal -e "sudo python3 consumer_cm_compute.py" --title="District Heating Potential:  consumer_cm_compute dh_potential"

sudo gnome-terminal -e "sudo python3 register_cm.py" --title="District Heating Potential: register_cm dh_potential"



