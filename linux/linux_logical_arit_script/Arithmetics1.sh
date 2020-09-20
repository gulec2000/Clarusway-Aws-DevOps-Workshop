#!/bin/bash

read -p "Please enter a number :" number1
read -p "Please enter another number :" number2
let total=number1+number2
let diff=number1-number2
let mult=number1*number2
let div=number1/number2

echo "Total = $total"
echo "Difference = $diff" 
echo "Multiplication = $mult"
echo "Division = $div"

