#!/bin/bash
input="./traffics.txt"
set -e
while IFS= read -r line
do
  echo "$line"
  dir=$(dirname "$line")
  fname=$(basename $line .pcap)
  [ -f "$line" ] && echo "exists" && echo "$dir"
  echo "$fname"
  mkdir -p $fname
  cp -i $line $fname
done < "$input"