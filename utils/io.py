import json
import pickle


def dump_json(file_name, obj):
    with open(file_name, "w") as f:
        json.dump(obj, f)


def load_json(file_name):
    with open(file_name, 'r') as f:
        obj = json.load(f)
        return obj
    

def dump_pkl(name, obj):
    with open(name, 'wb') as f:
        pickle.dump(obj, f)


def load_pkl(name):
    with open(name, 'rb') as f:
        obj = pickle.load(f)
    return obj
