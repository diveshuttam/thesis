#!/bin/bash


output="../output"
# rm -i $output/error.csv
# set -e
for f in ../pcap/lbnl/*/*.cap;
do
    x=$(basename $f .cap)
    xp=$(basename $(dirname $f))
    output_dir="$output/lbnl/$xp/$x"
    # [ -f $output_dir ] && continue || mkdir -p $output_dir 
    [ -f $output_dir/done_cemon1 ] && continue 
    # cp $f $output_dir/$x.pcap 
    echo working on $output_dir 
    ./single.sh "$output_dir/$x.pcap" rmse "$output/error_cemon_uti.csv" > "$output_dir/"$x"_cemon_uti.csv" 2>test_errors_cemon_uti
    [ "$?" -eq "0" ] && touch $output_dir/done_cemon1
    echo $?, $f
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