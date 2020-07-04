import argparse
import os
import tempfile
from collections import OrderedDict
import json

def add_item(storage,key,value):
    if args.key not in storage.keys():
        storage[key]=[]
        storage[key].append(value)
    else:
        storage[key].append(value)

def load_json(path):
    with open(path,"r") as read_file:
        storage=json.load(read_file)
    return storage

def dump_json(path,storage):
    with open(path,"w") as write_file:
        json.dump(storage,write_file)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
parser=argparse.ArgumentParser()
parser.add_argument("--key",help="getting a key to add to the storage")
parser.add_argument("--val",help="getting a value added to storage")
args=parser.parse_args()
if args.val:
    if not os.path.exists(storage_path):
        storage=OrderedDict()
        add_item(storage,args.key,args.val)
        dump_json(storage_path,storage)
    else:
        storage=load_json(storage_path)
        add_item(storage,args.key,args.val)
        dump_json(storage_path,storage)
else:
    if not os.path.exists(storage_path):
        print(None)
    else:
        storage=load_json(storage_path)
        if args.key not in storage:
            print(None)
        else:
            val_list=storage[args.key]
            values=", ".join(val_list)
            print(values)