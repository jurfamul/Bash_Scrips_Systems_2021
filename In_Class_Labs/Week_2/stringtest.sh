#!/bin/bash
if [[ "$#" -eq 2 ]] ; then
if [[ "$1" == "$2" ]] ; then echo "$1 and $2 are equivalent strings."
elif [[ "$1" < "$2" ]] ; then echo "$1 comes before $2 alphabetically."
else echo "$2 comes before $1 alphabetically."
fi
else echo "Must have two arguments."
fi
