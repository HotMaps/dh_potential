#!/usr/bin/env bash

sudo gnome-terminal -e "sudo python3 consumer_cm_alive.py" --title="consumer_cm_alive dh_potential"

sudo gnome-terminal -e "sudo python3 run.py" --title="run CM dh_potential"

sudo gnome-terminal -e "sudo python3 consumer_cm_compute.py" --title="consumer_cm_compute dh_potential"

sudo gnome-terminal -e "sudo python3 register_cm.py" --title="register_cm dh_potential"



