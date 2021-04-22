#!/bin/bash
totalfiles=10
count=0
for f in $(ls); do count=$((count + 1))
done
if [[ "$count" -lt "$totalfiles" ]]; then
  echo "Less than ten files."
elif [[ "$count" -eq "$totalfiles" ]]; then
  echo "Correct number of files found"
else echo "More than ten files."
fi
