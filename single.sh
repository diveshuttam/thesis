#!/bin/bash
# traffic br2
set -e
traffic=$1
error=$2
mkdir -p graphs/traffic_${traffic}/${error}/
./main_bytes.py $traffic $error curvature proportional 61 61 graphs/traffic_${traffic}/${error}/curvature_vs_proportional 
./main_bytes.py $traffic $error curvature ewma 61 61 graphs/traffic_${traffic}/${error}/curvature_vs_ewma
./main_bytes.py $traffic $error curvature cemon 61 61 graphs/traffic_${traffic}/${error}/curvature_vs_cemon
./main_bytes.py $traffic $error curvature momon 61 61 graphs/traffic_${traffic}/${error}/curvature_vs_momon
./main_bytes.py $traffic $error curvature curvature2 61 61 graphs/traffic_${traffic}/${error}/curvature_vs_curvature2 
