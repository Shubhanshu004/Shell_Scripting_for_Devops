#!/bin/bash

<<comment 
This is conditional bash scripting
comment

read -p "Enter the number " num

if [ $num -gt 10 ];
then
	echo "Number is greater than 10"
else 
	echo "Number is less than 10"
fi

