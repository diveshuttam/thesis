#!/usr/bin/env python3
import os
import sys
from collections import Counter
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from yaml import load, dump
import matplotlib.pyplot as plt


def drawfile(file_name1):
    data1 = open(f"../pcap/{file_name1}.yaml").read()
    arr1 = load(data1, Loader=Loader)
    arr10 = arr1[0][0]
    arr11 = arr1[0][1]

    idts = []
    ps = []
    for idx,i in enumerate(arr1[:-1]):
        idts.append(arr1[idx+1][0].timestamp()-arr1[idx][0].timestamp())
        ps.append(arr1[idx+1][1]-arr1[idx][1])
    
    d1 = {}
    for i in ps:
        try:
            d1[i]+=1
        except:
            d1[i]=1

    d2 = {}
    for i in idts:
        try:
            d2[int(i*10000000)]+=1
        except:
            d2[int(i*10000000)]=1
    
    l1 = list(zip(*list(sorted(d1.items()))))
    l2 = list(zip(*list(sorted(d2.items()))))
    print(l1[0][-10:], l1[1][-10:])
    print(l2[0][:10], l2[1][:10])
    print(sorted(Counter(ps).items()))
    return l1, l2


if __name__ =='__main__':
    l1,l2=drawfile(sys.argv[1])
    plt.bar(l1[0],l1[1], width=1000)
    plt.savefig(f'graphs/distr/{sys.argv[1]}_ps.png')
    