#!/bin/bash
# rm -i $output/error.csv
# set -e
for f in ../output/chosen_traffics/**/*.pcap;
do
    x=$(basename $f .pcap)
    output_dir=$(dirname $f)
    echo $x $output_dir
    [ -f $output_dir/done_momon_uti_fine ] && continue 
    [ -f $output_dir/graphs ] || mkdir -p "$output_dir/graphs" 
    [ -f $output_dir/csvs ] || mkdir -p "$output_dir/csvs" 
    echo working on $output_dir 
    # read a
    ./single.sh "$output_dir/$x.pcap" rmse "../output/chosen_traffics/error_curv_momon_uti_with_param_fine.csv" > "$output_dir/csvs/momon_uti_fine.csv" 2>>test_errors_momon_uti_fine
    status=$?
    echo $status, $f
    [ "$status" -eq "0" ] && touch $output_dir/done_momon_uti_fine
    
    # read a
done;
# rmse
# ./single.sh br2 rmse > $output/br2.csv
# ./single.sh matrix2 rmse > $output/matrix2.csv
# ./single.sh pareto0.1 rmse > $output/pareto0.1.csv
# ./single.sh pareto0.2 rmse > $output/pareto0.2.csv
# ./single.sh poission_slow0.2 rmse > $output/poission_slow0.2.csv
# ./single.sh poission0.1 rmse > $output/poission0.1.csv
# ./single.sh poission0.2 rmse > $output/poission0.2.csv
# ./single.sh voip0.1 rmse > $output/voip0.1.csv
# ./single.sh voip0.2 rmse > $output/voip0.2.csv

# # nrmse
# ./single.sh br2 nrmse
# ./single.sh matrix2 nrmse
# ./single.sh pareto0.1 nrmse
# ./single.sh pareto0.2 nrmse
# ./single.sh poission_slow0.2 nrmse
# ./single.sh poission0.1 nrmse
# ./single.sh poission0.2 nrmse
# ./single.sh voip0.1 nrmse
# ./single.sh voip0.2 nrmse

# # dtw
# ./single.sh br2 dtw
# ./single.sh matrix2 dtw
# ./single.sh pareto0.1 dtw
# ./single.sh pareto0.2 dtw
# ./single.sh poission_slow0.2 dtw
# ./single.sh poission0.1 dtw
# ./single.sh poission0.2 dtw
# ./single.sh voip0.1 dtw
# ./single.sh voip0.2 dtw

# # frechet
# ./single.sh br2 dtw
# ./single.sh matrix2 dtw
# ./single.sh pareto0.1 dtw
# ./single.sh pareto0.2 dtw
# ./single.sh poission_slow0.2 dtw
# ./single.sh poission0.1 dtw
# ./single.sh poission0.2 dtw
# ./single.sh voip0.1 dtw
# ./single.sh voip0.2 dtw