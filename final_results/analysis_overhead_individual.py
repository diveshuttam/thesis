import os
import parameters_uti
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
import load_file
import sys
import math
try:
    f = open("polled_flows_individual_list.txt")
    polled_flows = list(map(str.strip, f.readlines()))
except:
    root_dir = "./cemon_individual/flows_splited_final"
    flows_dirs = list(map(lambda x: os.path.join(root_dir,x), os.listdir(root_dir)))
    # flows_dirs = ['1744']
    flows_dirs = list(sorted(filter(lambda x:'pycache' not in x, flows_dirs)))
    polled_flows = []
    for flow_dir in flows_dirs:
        data_dir = f'{flow_dir}/data_uti_uti_singles'
        data_files = os.listdir(data_dir)
        # print(data_files)
        if len(data_files)==38:
            polled_flows.append(flow_dir)
            # print(f'appending {flow_dir}')
    f = open("polled_flows_individual_list.txt", "w")
    f.write('\n'.join(polled_flows))

# print(polled_flows)
print(len(polled_flows))

def get_overhead_cemon(parameter):
    curvature_polls_count = []
    cemon_polls_count = []
    cemon_functs = []
    tmin=float('inf')
    tmax=-float('inf')
    all_polls_time = []
    all_polls_data = []

    for polled_flow in polled_flows:
        type_ = 'curvature_vs_cemon_nrmse_with_param_uti_curvature_cemon_uti'
        data_file_path = f'{polled_flow}/data_uti_uti_singles/{type_}_' +'_'.join(map(str,parameter))+'.csv'
        data_file = open(data_file_path,'r')
        data_file_contents = data_file.readlines()
        # print(data_file_contents)
        curvature_time=eval(data_file_contents[1])
        curvature_polls=eval(data_file_contents[2])
        

        cemon_time=eval(data_file_contents[4])
        cemon_polls=eval(data_file_contents[5])
        try:
            all_polls_time.extend(cemon_time[1:-1])
            all_polls_data.extend(cemon_polls[1:-1])
        except:
            pass
        # print()
        # print(curvature_time)
        # print(curvature_polls)
        # print(cemon_time)
        # print(cemon_polls)
        curvature_polls_count.append(len(curvature_polls))
        cemon_polls_count.append(len(cemon_polls))
        cemon_functs.append(interp1d(cemon_time,cemon_polls,bounds_error=False,fill_value=(0,0)))
        tmin=min(tmin,cemon_time[0])
        tmax=max(tmax,cemon_time[-1])

    print(tmin,tmax)
    final_x = list(range(0,61))
    final_y = [0]*61

    all_polls_time = list(map(lambda x: x-tmin,all_polls_time))
    all_polls = list(sorted(list(zip(all_polls_time,all_polls_data)), key = lambda x:x[0]))
    all_polls = list(zip(*all_polls))
    
    all_polls_time = all_polls[0]
    for poll in all_polls_time:
        final_y[int(math.ceil(poll))]+=1
    print(final_x)
    print(final_y)

    return final_x, final_y

def get_overhead_curvature_and_momon(parameter, parameter1):
    prefix = "./combined/data_uti_combined_momon/curvature_vs_momon_nrmse_with_param_uti_curvature_momon_uti"
    
    # cemon
    data_file = open(f"{prefix}_" + "_".join(map(str,parameter)) + ".csv")
    data_file_contents = data_file.readlines()

    curvature_time=eval(data_file_contents[1])
    curvature_polls=eval(data_file_contents[2])

    data_file.close()

    # momon
    data_file = open(f"{prefix}_" + "_".join(map(str,parameter1)) + ".csv")
    data_file_contents = data_file.readlines()
    
    momon_time=eval(data_file_contents[4])
    momon_polls=eval(data_file_contents[5])

    # reset time
    curvature_time = list(map(lambda x: x-curvature_time[0], curvature_time))[1:-1]
    momon_time = list(map(lambda x: x-momon_time[0], momon_time))[1:-1]

    # start message
    momon_x = list(range(0,61))
    momon_y = [0]*61

    curvature_x = list(range(0,61))
    curvature_y = [0]*61
    
    for poll in curvature_time:
        curvature_y[int(math.ceil(poll))]+=1

    for poll in momon_time:
        momon_y[int(math.ceil(poll))]+=1

    return curvature_x, curvature_y, momon_x, momon_y

parameter_5 = list(filter(lambda x: x[1]==5.0, parameters_uti.parameters_array))[0]
parameter_3 = list(filter(lambda x: x[1]==3.0, parameters_uti.parameters_array))[0]

for parameter in parameters_uti.parameters_array:
    # uti
    cemon_x, cemon_y = get_overhead_cemon(parameter)
    curvature_x, curvature_y, momon_x, momon_y = get_overhead_curvature_and_momon(parameter, parameter) # from polling as single flows
    print(f"using paramter {parameter} for curvature, cemon 5.0 and momon 3.0")
    plt.figure()
    plt.plot(curvature_x, curvature_y, label="Curvature")
    plt.plot(momon_x, momon_y, label="MoMon")
    # plt.plot(cemon_x,cemon_y, label="CeMon")
    plt.xlabel("Time (sec)")
    plt.ylabel("Message Overhead (Message number)")
    ax = plt.axes()
    ax = plt.axes()

    ax.tick_params(axis='both', direction='in')
    xlim = plt.xlim
    ylim = plt.ylim
    left, right = xlim()  # return the current xlim
    top, bottom = ylim()  # return the current xlim
    xlim((0,60))   # set the xlim to left, right
    ylim(bottom=0)   # set the xlim to left, right
    plt.legend()

    plt.savefig(f"overhead_graphs_cemon_individual/both_same_tmax/without_cemon/without_cemon_overhead_"+"_".join(map(lambda x: str(float(x)),parameter))+".png")
