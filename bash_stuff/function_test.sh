#!/bin/bash
args=2
function add {
  if [[ "$#" -eq "$args" ]] ; then
    sum=$(( "$1" + "$2"))
    echo "$sum"
  else echo "This function requires two arguments"
fi
}

function multiply {
  if [[ "$#" -eq "$args" ]] ; then
    product=$(( "$1" * "$2"))
    echo "$product"
  else echo "This function requires two arguments"
fi
}

argsFac=1
function factorial {
  if [[ "$#" -eq "$argsFac" ]] ; then
    if [[ "$1" -gt 0 ]] ; then
      if [[ "$1" -eq 1 ]] ; then
        echo "$1"
      else
        next=$(( "$1" - 1 ))
        facProduct=$(multiply $1 $(factorial $next))
        echo "$facProduct"
      fi
    else echo "The argument must be a positive value"
    fi
  else echo "This function requires one argument"
  fi
}

#first=3
#second=14
if [[ "$#" -eq "$args" ]] ; then
  valSum=$(add $1 $2)
  valProduct=$(multiply $1 $2)
  echo "The sum of $1 and $2 is $valSum."
  echo "The product of $1 and $2 is $valProduct."
elif [[ "$#" -eq "$argsFac" ]] ; then
  valFac=$(factorial $1)
  echo "The value of $1 factorial is $valFac."
else echo "This script requires one or two arguments"
fi
