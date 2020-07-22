#!/bin/bash
# set -e
method1="curvature" # curvature/momon/cemon
method2="momon" # curvature/momon/cemon
type="uti" # bytes/uti
error="nrmse" # nrmse/relabs/correlation/rmse/nrmsep/relabsp
[ -f "../output/processed/${type}_w_tratio_summary_results" ] || mkdir -p "../output/processed/${type}_w_tratio_summary_results"

for f in ../output/processed/**/splits/**/*.pcap;
do
    x=$(basename $f .pcap)
    output_dir=$(dirname $f)
    echo $x $output_dir
    # [ -f "$output_dir/done_${method1}_${method2}_${type}_w_tratio_summary_results_${error}" ] && continue 
    [ -f "$output_dir/graphs_${type}_w_tratio_summary_results" ] || mkdir -p "$output_dir/graphs_${type}_w_tratio_summary_results" 
    [ -f "$output_dir/csvs_${type}_w_tratio_summary_results" ] || mkdir -p "$output_dir/csvs_${type}_w_tratio_summary_results" 
    echo "working on $output_dir "
    # read a
    ./single.sh "$output_dir/$x.pcap" "${error}" "../output/processed/${type}_w_tratio_summary_results/error_${method1}_${method2}_${error}_with_param_${x}.csv" "$method1" "$method2" "$type" > "$output_dir/csvs_${type}_w_tratio_summary_results/${method1}_${method2}_${error}_with_param_${type}.csv" 2>>"test_errors_${method1}_${method2}_${error}_with_param_${type}_${x}";
    status=$?
    echo "$status, $f"
    [ "$status" -eq "0" ] && touch "$output_dir/done_${method1}_${method2}_${type}_w_tratio_summary_results_${error}";
    # read a
done;

paplay "/usr/share/sounds/ubuntu/stereo/desktop-login.ogg";