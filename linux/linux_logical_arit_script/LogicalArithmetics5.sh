#!/bin/bash

read -p "Please enter your name : " name

read -p "Please enter your age : " age

read -p "What is your average life expectancy : " ale

if (( age < 18 ));then
	echo "Name is $name and he is a student."
        echo "At least $((18 - age)) years to become a worker"
elif (( 18 <= age )) && (( age < 65 )); then
	echo "$name you must be a worker."
        echo "$((65-age)) years to retire."
elif (( age >= 65 )); then
	if (( age < ale )); then
		echo "$name you must be retired."
	        echo "$((ale-age)) years to die."
	elsei
		echo -ne '\007'
		echo "!!!!!Already DIED!!!!!!!!!!"
		sleep 2
		echo -ne '/007'
		echo "!!!!!Already DIED!!!!!!!!!"
		sleep 3
		echo "!!!!!Already DIED!!!!!!!!!"
		echo -ne '/007'
	fi
fi
