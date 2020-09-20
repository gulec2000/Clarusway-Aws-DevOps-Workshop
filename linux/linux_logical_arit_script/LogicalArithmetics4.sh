#!/bin/bash

read -p "Please enter a number : " n1
read -p "Please enter another number : " n2
read -p "Pleae enter another number : " n3

if (( (( n2 > n1)) && ((n2 < n3)) )); then
       echo "$n2 is between $n1 and $n3"
elif (( (( n1 > n2 )) || (( n3 < n2 )) )); then
	echo "$n2 is out of range"
fi        
