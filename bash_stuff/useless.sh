#!/bin/bash
if [[ "$#" -eq 1 ]] ; then
  prefix=$1
  fileCount=$(ls $prefix* | wc -l)
  count=0
  numNew=100

  #This loop creates .txt files with the prefix the user passed from the command line
  #until there are 100 files with that prefix.
  while [[ "$fileCount" -lt "$numNew" ]] ; do
    while [[ -e "$prefix$count.txt" ]] ; do
      count=$(($count + 1 ))
    done
    touch "$prefix$count.txt"
    fileCount=$(ls $prefix* | wc -l)
  done
  echo "The file count is $fileCount."

  #This loop deletes 50 random files with prefix the user passed from the command line
  for i in $(seq 0 49) ; do
    randFile=$(ls $prefix* | head -n 1)
    rm $randFile
  done
  fileCount=$(ls $prefix* | wc -l)
  echo "The file count is $fileCount."
else echo "Error: No profix given."
fi
