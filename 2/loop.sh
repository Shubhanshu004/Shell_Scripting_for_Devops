#!/bin/bash

count=1

while [ $count -le  5 ]
do
	echo $count
	count=$((count+1))
done

input=""

while [ "$input" != "exit" ]
do 
	read -p "Enter something (type exit to quit): " input
	echo "You entered: $input"
done
