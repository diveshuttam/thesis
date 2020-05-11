#!/bin/bash
error_type="rmse"

set -e
# ./single.sh br2_matrix2 $error_type
# ./single.sh br2_poission0.1 $error_type
# ./single.sh br2_poission0.2 $error_type
# ./single.sh br2_pareto0.2 $error_type
# ./single.sh br2_pareto0.1 $error_type
# ./single.sh br2_poission_slow0.2 $error_type
# ./single.sh br2_voip0.1 $error_type
# ./single.sh br2_voip0.2 $error_type


# ./single.sh poission0.1_matrix2 $error_type
# ./single.sh poission0.1_poission0.2 $error_type
# ./single.sh poission0.1_pareto0.2 $error_type
# ./single.sh poission0.1_pareto0.1 $error_type
# ./single.sh poission0.1_poission_slow0.2 $error_type
# ./single.sh poission0.1_voip0.1 $error_type
# ./single.sh poission0.1_voip0.2 $error_type


# ./single.sh poission0.2_matrix2 $error_type
# ./single.sh poission0.2_pareto0.2 $error_type
# ./single.sh poission0.2_pareto0.1 $error_type
# ./single.sh poission0.2_poission_slow0.2 $error_type
# ./single.sh poission0.2_voip0.1 $error_type
# ./single.sh poission0.2_voip0.2 $error_type

# ./single.sh pareto0.1_matrix2 $error_type
# ./single.sh pareto0.1_pareto0.2 $error_type
# ./single.sh pareto0.1_poission_slow0.2 $error_type
./single.sh pareto0.1_voip0.1 $error_type
./single.sh pareto0.1_voip0.2 $error_type

./single.sh pareto0.2_matrix2 $error_type
./single.sh pareto0.2_poission_slow0.2 $error_type
./single.sh pareto0.2_voip0.1 $error_type
./single.sh pareto0.2_voip0.2 $error_type

./single.sh matrix2_poission_slow0.2 $error_type 
./single.sh matrix2_voip0.1 $error_type
./single.sh matrix2_voip0.2 $error_type

./single.sh poission_slow0.2_voip0.1 $error_type
./single.sh poission_slow0.2_voip0.2 $error_type

./single.sh voip0.1_voip0.2 $error_type

