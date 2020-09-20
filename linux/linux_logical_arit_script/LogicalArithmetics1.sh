#!/bin/bash

read -p "Please enter a number as first number : " num1

read -p "Please enter a number as second number : " num2

let total=num1+num2
echo $((total++))

echo $total

echo $((total-num1))




