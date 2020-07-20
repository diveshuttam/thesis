#!/bin/bash
# traffic br2
set -e
traffic=$1
error=$2
error_file=$3
method1=$4
method2=$5
type=$6
echo $traffic $error
# echo "/${method1}_vs_${method2}_${error}_with_param_${type}"
echo -e "\n"
x=$(dirname $traffic)
./main_${type}.py "$traffic" "$error" "${method1}" "${method2}" 61 61 "$x/graphs_${type}_w_tratio_summary_results/${method1}_vs_${method2}_${error}_with_param_${type}" "$error_file"
echo -e "\n"
paplay "/usr/share/sounds/ubuntu/stereo/phone-outgoing-busy.ogg"