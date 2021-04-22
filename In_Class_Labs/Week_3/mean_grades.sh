#!/bin/bash
valMean=0
count=0
gradeMin=100
studentMin=" "
gradeMax=0
studentMax=" "
infile=$1
while read line ; do
  nameCur=$(echo $line | cut -d "$2" -f 1)
  valCur=$(echo $line | cut -d "$2" -f $3)
  if [[ "$valCur" -gt "$gradeMax" ]] ; then
    gradeMax=$valCur
    studentMax=$nameCur
  fi
  if [[ "$valCur" -lt "$gradeMin" ]] ; then
    gradeMin=$valCur
    studentMin=$nameCur
  fi
  count=$(($count + 1 ))
  valMean=$(($valMean + $valCur ))
done < $infile
echo "The mean grade is: $(echo "scale=3;$valMean/$count" | bc )."
echo "$studentMin had the lowest grade: $gradeMin."
echo "$studentMax had the hightest grade: $gradeMax."
