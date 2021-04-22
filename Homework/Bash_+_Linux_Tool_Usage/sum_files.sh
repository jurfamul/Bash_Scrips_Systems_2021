#!/bin/bash

#sum_files.sh
#By: Jurgen Famula
#4-21-21
#Advanced Systems Programming
numArgs=2
countFiles=0
totalSize=0
function sum_File_Size {
  if [[ "$#" -eq 1 ]] ; then
    totalSize=$(( "$totalSize" + "$1" ))
  fi
}
if [[ "$#" -eq "$numArgs" ]] ; then
  if [ -d "$2" ] ; then
    for file in $(find $2 -name $1 -type f)  ; do
      countFiles=$(($countFiles + 1 ))
      curFileSize=$(ls -la $file | cut -d " " -f 5)
      sum_File_Size $curFileSize
    done
    echo "Found $countFiles $1 files under directory $2 with a total size of $totalSize bytes."
  else echo "Error: $2 is not a valid directory path. Exiting script."
  fi
else echo "Error: This script requires $numArgs arguments. Exiting script"
fi
