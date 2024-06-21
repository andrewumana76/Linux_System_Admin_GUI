#!/bin/bash

if id "$1" &>/dev/null; then
	#Username exists
	echo "User does exists. Exiting with 1"
	exit 1;
else
	#User does not exist
	echo " User does not exist. Creating User"
	useradd $1 -p $2
fi

exit 0
