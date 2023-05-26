#!/bin/bash

echo "Please give the 01100011 01101000 01100001 01101001 01110010 as a word."
read answer

if [[ "$answer" == "chair" ]]; then
    echo "Please give me the 154 151 155 145 as a word."
    read answer

    if [[ "$answer" == "lime" ]]; then
        echo "Please give me the 70656172 as a word."
        read answer

        if [[ "$answer" == "pear" ]]; then
            echo "flag{y0u_r_pw3tty_d3c3nt}"
        else
            echo "Incorrect answer"
        fi
    else
        echo "Incorrect answer"
    fi
else
    echo "Incorrect answer"
fi
