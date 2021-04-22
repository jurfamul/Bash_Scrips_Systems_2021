#! /bin/bash
start=$(date +%s)
tsleep=$((1 + $1))
sleep $tsleep
end=$(date +%s)
echo "The time slept was $(($end - $start)) seconds."
