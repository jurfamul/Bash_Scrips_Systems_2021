#! /bin/bash
sleep 30 &
pid=$!
echo "Sleeping process pid is $pid"
sleep 5
$(kill $pid)
