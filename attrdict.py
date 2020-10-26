# Copyright (c) 2020, Alexandre Hamelin

#from argparse import Namespace

__all__ = ['attrdict']

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __getattr__(self, k):
        return self[k]
    def __setattr__(self, k, v):
        self[k] = fromdict(v) if type(v) is dict else v
    def __delattr__(self, k):
        del self[k]

def walk_obj(obj, parent_obj, key):
    if type(obj) is dict:
        for k in obj:
            walk_obj(obj[k], obj, k)
        parent_obj[key] = AttrDict(obj)
    elif type(obj) is list:
        for i, e in enumerate(obj):
            walk_obj(obj[i], obj, i)
        parent_obj[key] = obj

def fromdict(d):
    coll = [d]
    walk_obj(coll[0], coll, 0)
    return coll[0]
