#!/usr/bin/env bash

while :
do
    nc -z $1 $2
    WAITFORIT_result=$?

    if [[ $WAITFORIT_result -eq 0 ]]; then
        break
    fi
    echo "sleeping 2 sec for $1:$2";
    sleep 2
done
echo "connected"
