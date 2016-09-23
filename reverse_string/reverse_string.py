#!/usr/bin/env python
#coding:utf-8

def reverse_string(args):
    ret = ""
    for x in range(-1, -len(args)-1, -1):
        ret+=args[x]
    return ret

if __name__ == "__main__":
    args = "Hi,Rocky!"
    print reverse_string(args)
    args = "Hi,fork"
    print reverse_string(args)
