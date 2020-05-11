#!/bin/bash

./merge_file.py br2 matrix2
./merge_file.py br2 poission0.1
./merge_file.py br2 poission0.2
./merge_file.py br2 pareto0.2
./merge_file.py br2 pareto0.1
./merge_file.py br2 poission_slow0.2
./merge_file.py br2 voip0.1
./merge_file.py br2 voip0.2


./merge_file.py poission0.1 matrix2
./merge_file.py poission0.1 poission0.2
./merge_file.py poission0.1 pareto0.2
./merge_file.py poission0.1 pareto0.1
./merge_file.py poission0.1 poission_slow0.2
./merge_file.py poission0.1 voip0.1
./merge_file.py poission0.1 voip0.2


./merge_file.py poission0.2 matrix2
./merge_file.py poission0.2 pareto0.2
./merge_file.py poission0.2 pareto0.1
./merge_file.py poission0.2 poission_slow0.2
./merge_file.py poission0.2 voip0.1
./merge_file.py poission0.2 voip0.2

./merge_file.py pareto0.1 matrix2
./merge_file.py pareto0.1 pareto0.2
./merge_file.py pareto0.1 poission_slow0.2
./merge_file.py pareto0.1 voip0.1
./merge_file.py pareto0.1 voip0.2

./merge_file.py pareto0.2 matrix2
./merge_file.py pareto0.2 poission_slow0.2
./merge_file.py pareto0.2 voip0.1
./merge_file.py pareto0.2 voip0.2

./merge_file.py matrix2 poission_slow0.2
./merge_file.py matrix2 voip0.1
./merge_file.py matrix2 voip0.2

./merge_file.py poission_slow0.2 voip0.1
./merge_file.py poission_slow0.2 voip0.2

./merge_file.py voip0.1 voip0.2