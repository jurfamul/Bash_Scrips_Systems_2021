#!/bin/bash
infile="alice.txt"
count=0
while read line ; do
  lineCount=$(grep -oi "the" $infile | wc -l)
  if [[ "$lineCount" -gt 0 ]] ; then
    count=$(($count + $linecount))
    echo $line
  fi
done < $infile
echo "The file $infile contains $count instances of the word 'the'"
