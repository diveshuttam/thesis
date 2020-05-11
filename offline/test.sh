#!/bin/bash

set -e
output="./output"
# rmse
./single.sh br2 rmse > $output/br2.csv
./single.sh matrix2 rmse > $output/matrix2.csv
./single.sh pareto0.1 rmse > $output/pareto0.1.csv
./single.sh pareto0.2 rmse > $output/pareto0.2.csv
./single.sh poission_slow0.2 rmse > $output/poission_slow0.2.csv
./single.sh poission0.1 rmse > $output/poission0.1.csv
./single.sh poission0.2 rmse > $output/poission0.2.csv
./single.sh voip0.1 rmse > $output/voip0.1.csv
./single.sh voip0.2 rmse > $output/voip0.2.csv

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