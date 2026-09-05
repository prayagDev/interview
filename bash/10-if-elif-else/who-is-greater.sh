#!/bin/bash

read -p "Prayag ji plzz fill your number na plzzz: " num1
read -p "Prayag ji plzz fill your number2   plzzz: " num2

if [ "$num1" -gt "$num2" ]; then
    echo "$num1 is greater"
elif [ "$num1" -lt "$num2" ]; then
    echo "$num2 is greater"
else
    echo "$num1 and $num2 are equal"
fi

