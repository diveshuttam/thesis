#!/bin/sh

traffic="voip0.2"

./main_bytes.py $traffic rmse periodic periodic 10 10 periodic_graphs/periodic10
./main_bytes.py $traffic rmse periodic periodic 20 20 periodic_graphs/periodic20
./main_bytes.py $traffic rmse periodic periodic 30 30 periodic_graphs/periodic30
./main_bytes.py $traffic rmse periodic periodic 40 40 periodic_graphs/periodic40
./main_bytes.py $traffic rmse periodic periodic 50 50 periodic_graphs/periodic50
./main_bytes.py $traffic rmse periodic periodic 60 60 periodic_graphs/periodic60
./main_bytes.py $traffic rmse periodic periodic 70 70 periodic_graphs/periodic70
./main_bytes.py $traffic rmse periodic periodic 80 80 periodic_graphs/periodic80
./main_bytes.py $traffic rmse periodic periodic 90 90 periodic_graphs/periodic90
./main_bytes.py $traffic rmse periodic periodic 100 100 periodic_graphs/periodic100
./main_bytes.py $traffic rmse periodic periodic 200 200 periodic_graphs/periodic200
./main_bytes.py $traffic rmse periodic periodic 400 400 periodic_graphs/periodic400
./main_bytes.py $traffic rmse periodic periodic 800 800 periodic_graphs/periodic800
./main_bytes.py $traffic rmse periodic periodic 1600 1600 periodic_graphs/periodic1600
./main_bytes.py $traffic rmse periodic periodic 3200 3200 periodic_graphs/periodic3200
