#!/bin/bash
runningSum=0
while [[ "$#" -gt 0 ]] ; do
  runningSum=$(echo "$runningSum" + "$1" | bc -l)
  shift
done
echo "The sum is $runningSum."
