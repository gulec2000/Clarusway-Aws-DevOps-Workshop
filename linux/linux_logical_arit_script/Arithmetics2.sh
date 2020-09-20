#!/bin/bash

read -p "Please enter a number :" number1
read -p "Please enter another number :" number2
total=$((number1+number2))
diff=$((number1-number2))
mult=$((number1*number2))
div=$((number1/number2))

echo "Total = $total"
echo "Difference = $diff" 
echo "Multiplication = $mult"
echo "Division = $div"

