import os
import parameters_uti
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
import load_file
import sys
import similarity

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

def get_final_combined_flow_cemon(parameter):
    try:
        f = open(f"final_cemon_individual_polled_uti_{parameter[1]}.txt")
        final_x = list(map(float, f.readline().split(",")))
        final_y = list(map(float, f.readline().split(",")))
        cemon_polls_count = list(map(int, f.readline().split(",")))
    except:
        curvature_polls_count = []
        cemon_polls_count = []
        cemon_functs = []
        tmin=float('inf')
        tmax=-float('inf')
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
        final_x = list(np.arange(tmin,tmax,0.01))
        final_y = np.array([0]*len(final_x))
        for i in cemon_functs:
            final_y = final_y + i(final_x)
        
        # write to file
        f = open(f"final_cemon_individual_polled_uti_{parameter[1]}.txt", "w")
        f.write(",".join(map(str,final_x)) + "\n")
        f.write(",".join(map(str,final_y)) + "\n")
        f.write(",".join(map(str,cemon_polls_count)) + "\n")
    
    final_x = list(map(lambda x: x-final_x[0], final_x))
    return final_x, final_y, cemon_polls_count

def get_orig_flow():
    try:
        f = open("final_orig_uti.txt")
        uti_x = list(map(float, f.readline().split(",")))
        uti_y = list(map(float, f.readline().split(",")))
    except:
        arr = list(zip(*load_file.load_file('./cemon_individual/single1tcp.pcap')))
        print(arr[0][:5])
        print(arr[1][:5])
        orig_x = list(map(lambda x: x.timestamp(), arr[0]))
        orig_y = arr[1]
        bytes_fun = interp1d(orig_x,orig_y,kind='previous',fill_value=(0,orig_y[-1]), bounds_error=False)
        uti_x = np.arange(orig_x[0], orig_x[-1],0.1)
        uti_y = bytes_fun(uti_x)-bytes_fun(uti_x-1)
        f = open("final_orig_uti.txt", "w")
        f.write(','.join(map(str,uti_x))+"\n")
        f.write(','.join(map(str,uti_y))+"\n")
    uti_x = list(map(lambda x: x-uti_x[0], uti_x))
    return uti_x, uti_y

def get_curvature_and_momon(parameter, parameter1):
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
    curvature_time = list(map(lambda x: x-curvature_time[0], curvature_time))
    momon_time = list(map(lambda x: x-momon_time[0], momon_time))
    return curvature_time, curvature_polls, momon_time, momon_polls

parameter_5 = list(filter(lambda x: x[1]==5.0, parameters_uti.parameters_array))[0]
parameter_3 = list(filter(lambda x: x[1]==3.0, parameters_uti.parameters_array))[0]

for parameter in parameters_uti.parameters_array:
    # uti
    cemon_x, cemon_y, cemon_polls_count = get_final_combined_flow_cemon(parameter)
    orig_x, orig_y = get_orig_flow()
    curvature_x, curvature_y, momon_x, momon_y = get_curvature_and_momon(parameter,parameter) # from polling as single flows

    print( 'total polls cemon=', sum(cemon_polls_count) - 2*len(polled_flows))
    print(len(cemon_x))
    plt.figure()
    plt.plot(orig_x,orig_y, label="actual")
    plt.plot(curvature_x, curvature_y, label="curvature")
    plt.plot(momon_x, momon_y, label="momon")
    plt.plot(cemon_x,cemon_y, label="cemon")
    plt.xlabel("Time (s)")
    plt.ylabel("Utilization (bytes/sec) ")
    plt.title(f"Utilization as measured by various schemes\n paramters = {parameter}")
    plt.legend()
    plt.savefig(f"utilization_graphs/both_same_tmax/all/all_utilization_"+"_".join(map(lambda x: str(float(x)),parameter))+".png")

# print()
# print(parameter)
# print(sum(curvature_polls_count))
# print(sum(cemon_polls_count))
# print(cemon_polls_count)