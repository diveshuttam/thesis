#!/bin/bash

set -e
# rmse
./single.sh br2 rmse
./single.sh matrix2 rmse
./single.sh pareto0.1 rmse
./single.sh pareto0.2 rmse
./single.sh poission_slow0.2 rmse
./single.sh poission0.1 rmse
./single.sh poission0.2 rmse
./single.sh voip0.1 rmse
./single.sh voip0.2 rmse

# nrmse
./single.sh br2 nrmse
./single.sh matrix2 nrmse
./single.sh pareto0.1 nrmse
./single.sh pareto0.2 nrmse
./single.sh poission_slow0.2 nrmse
./single.sh poission0.1 nrmse
./single.sh poission0.2 nrmse
./single.sh voip0.1 nrmse
./single.sh voip0.2 nrmse

# dtw
./single.sh br2 dtw
./single.sh matrix2 dtw
./single.sh pareto0.1 dtw
./single.sh pareto0.2 dtw
./single.sh poission_slow0.2 dtw
./single.sh poission0.1 dtw
./single.sh poission0.2 dtw
./single.sh voip0.1 dtw
./single.sh voip0.2 dtw

# frechet
./single.sh br2 dtw
./single.sh matrix2 dtw
./single.sh pareto0.1 dtw
./single.sh pareto0.2 dtw
./single.sh poission_slow0.2 dtw
./single.sh poission0.1 dtw
./single.sh poission0.2 dtw
./single.sh voip0.1 dtw
./single.sh voip0.2 dtw