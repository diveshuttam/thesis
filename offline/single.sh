#!/bin/bash
# traffic br2
set -e
traffic=$1
error=$2
error_file=$3
echo $traffic $error
echo -e "\n"
mkdir -p graphs/traffic_${traffic}/${error}/
# ./main_bytes.py $traffic $error curvature proportional 61 61 graphs/traffic_${traffic}/${error}/curvature_vs_proportional 
# ./main_bytes.py $traffic $error curvature ewma 61 61 graphs/traffic_${traffic}/${error}/curvature_vs_ewma
./main_bytes.py $traffic $error curvature cemon 61 61 "$(dirname $traffic)/${error}-curvature_vs_cemon_uti" $error_file
# echo ./main_bytes.py $traffic $error curvature cemon 61 61 "$(dirname $traffic)/${error}-curvature_vs_cemon_uti" $error_file

# ./main_bytes.py $traffic $error curvature momon 61 61 graphs/traffic_${traffic}/${error}/curvature_vs_momon
# ./main_bytes.py $traffic $error curvature curvature2 61 61 graphs/traffic_${traffic}/${error}/curvature_vs_curvature2 
echo -e "\n"