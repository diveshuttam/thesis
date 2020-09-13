import os
import pyshark
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from pathlib import Path


from yaml import load, dump

byte_count = 0
# byte_count1 = 0
def load_file(file_name):
    path = Path(file_name)
    parent = path.parent
    base = os.path.splitext(file_name)[0]
    if f'{base}.yaml' not in os.listdir(parent):
        cap = pyshark.FileCapture(f'{base}.pcap')
        global byte_count
        byte_count = 0
        arr = []
        def new_packet(pkt):
            global byte_count
            # global byte_count1
            byte_count+=int(pkt.length)
            # byte_count1+=int(pkt.captured_length)
            sniff_time = pkt.sniff_time
            arr.append((sniff_time,byte_count))
            # print(pkt.length, pkt.captured_length, byte_count, byte_count1)

        cap.apply_on_packets(new_packet)
        data = dump(arr,Dumper=Dumper)
        open(f"{base}.yaml","w").write(data)
    else:
        data = open(f"{base}.yaml").read()
        arr = load(data, Loader=Loader)
    return arr
