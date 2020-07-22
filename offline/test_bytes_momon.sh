#!/bin/bash
# set -e
method1="curvature" # curvature/momon/cemon
method2="momon" # curvature/momon/cemon
type="bytes" # bytes/uti
error="nrmse" # nrmse/relabs/correlation/rmse/nrmsep/relabsp
results_folder="fine70_momon"
efname="runtime_errors"

[ -f "../output/processed/${type}_${results_folder}" ] || mkdir -p "../output/processed/${type}_${results_folder}"
[ -f "../output/processed/${type}_${results_folder}/${efname}" ] || mkdir -p "../output/processed/${type}_${results_folder}/${efname}"
error_folder="../output/processed/${type}_${results_folder}/${efname}"

for f in ../output/processed/**/splits/**/*.pcap;
do
    x=$(basename $f .pcap)
    output_dir=$(dirname $f)
    echo $x $output_dir
    # [ -f "$output_dir/done_${method1}_${method2}_${type}_${results_folder}_${error}" ] && continue 
    [ -f "$output_dir/graphs_${type}_${results_folder}" ] || mkdir -p "$output_dir/graphs_${type}_${results_folder}" 
    [ -f "$output_dir/csvs_${type}_${results_folder}" ] || mkdir -p "$output_dir/csvs_${type}_${results_folder}" 
    echo "working on $output_dir "
    # read a
    ./single.sh "$output_dir/$x.pcap" "${error}" "../output/processed/${type}_${results_folder}/error_${method1}_${method2}_${error}_with_param_${x}.csv" "$method1" "$method2" "$type" "${results_folder}" > "$output_dir/csvs_${type}_${results_folder}/${method1}_${method2}_${error}_with_param_${type}.csv" 2>>"${error_folder}/test_errors_${method1}_${method2}_${error}_with_param_${type}_${x}";
    status=$?
    echo "$status, $f"
    [ "$status" -eq "0" ] && touch "$output_dir/done_${method1}_${method2}_${type}_${results_folder}_${error}";
    # read a
done;

paplay "/usr/share/sounds/ubuntu/stereo/desktop-login.ogg";