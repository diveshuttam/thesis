#!/usr/bin/env python3
import os
import pyshark
import sys
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from yaml import load, dump

byte_count = 0
byte_count1 = 0
byte_count2 = 0

def merge_file(file_name1,file_name2):
    data1 = open(f"../pcap/{file_name1}.yaml").read()
    data2 = open(f"../pcap/{file_name2}.yaml").read()
    arr1 = load(data1, Loader=Loader)
    arr2 = load(data2, Loader=Loader)
    arr10 = arr1[0][0]
    arr20 = arr2[0][0]
    print(arr10, arr20)
    arr11 = arr1[0][1]
    arr21 = arr2[0][1]

    for idx,i in enumerate(arr1):
        if(idx==0):
            continue
        arr1[idx]=(arr1[idx][0],arr1[idx][1]-arr1[idx-1][1])
    
    for idx,i in enumerate(arr2):
        if(idx==0):
            continue
        arr2[idx]=(arr2[idx][0],arr2[idx][1]-arr2[idx-1][1])
    
    arr1 = list(map(lambda x: (x[0],x[1]), arr1))
    arr2 = list(map(lambda x: (x[0]-arr20+arr10,x[1]), arr2))
    arr = sorted(arr1+arr2)

    for idx,i in enumerate(arr):
        if(idx==0):
            continue
        arr[idx]=(arr[idx][0],arr[idx][1]+arr[idx-1][1])

    print(arr[:10])
    return arr

if __name__ =='__main__':
    arr = merge_file(sys.argv[1],sys.argv[2])
    f = open(f"../pcap/{sys.argv[1]}_{sys.argv[2]}.yaml","w")
    dump(arr,f,Dumper=Dumper)
