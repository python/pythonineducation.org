#!/bin/bash

ERRORS=()

###
# Check that site can be built.
###

echo " *** Checking that site can be built."

wok --serve >/dev/null 2>&1 &
WOK_PID=$!

if [[ $? -eq 0 ]]; then
	echo " *** Site built ok."
else
	echo " *** Site could not be built."
	exit 1
fi

###
# Wait for server to start.
###

sleep 5
curl "http://localhost:8000" >/dev/null 2>&1

if [[ $? -ne 0 ]]; then
	echo " *** Server is not running."
	exit 1
fi

###
# Check that no links are broken.
###

# TODO reinstate this

#echo " *** Checking that no links are broken."

#linkchecker --no-status --no-warnings --check-extern "http://localhost:8000"

#if [[ $? -ne 0 ]]; then
#	ERRORS+=("Broken links found on site")
#fi

###
# Check that common names are spelt correctly.
###

#echo " *** Checking that common names are spelt correctly"

#grep -e "MicroBit" -e "Microbit" -e "microbit" -e "microBit" --line-number --recursive --include "*.html" output | grep -v https://microbit.co.uk

#if [[ $? -eq 0 ]]; then
#	ERRORS+=("Spelling mistaik detected. :-)")
#fi

kill $WOK_PID

if [[ ${#ERRORS[@]} -eq 0 ]]; then
	echo " *** All pre-flight checks passed!"
	exit 0
else
	echo " *** The following pre-flight check(s) failed:"
	for error in "${ERRORS[@]}"; do
		echo " - $error"
	done
	exit 1
fi
