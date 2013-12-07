#!/usr/bin/env python
#coding=utf8

import string


def data_print(data, title="no title", d="=", dd='-'):
    """ print the data list with table style """
    kl = data[0].keys()
    c, l = max_length_list(data, kl)
    dn = (c - len(title) - 4) / 2

    print d*dn,title,d*dn
    print ''.join([string.center(k, l[i]) for i, k in enumerate(kl)])
    print dd*c
    for d in data:
        print ''.join([string.ljust(getattr(d, k), l[i]) for i, k in enumerate(kl)])


def max_length_list(lt, kl):
    """ return a max_length attrs of a object list and the max_length sum"""
    l = [max_length(lt, k) for k in kl]
    c = sum(l)
    return (c, l)


def max_length(l, k, s=4):
    """ return object from an object list which has the most length of the attr """
    return len(getattr(max(l, key=lambda x: len(x.get(k))), k))+s

if __name__ == '__main__':
    l = []
    for i in range(5):
        o = {}
        o['title'] = "time"
        o['guid'] = "everything at onece"
        o['content'] = 'hello world, I hate you.'
        o['create_time'] = "2012/12/01"
        o['update_time'] = '2013/12/11'
        l.append(o)

    data_print(l, title="test for print")
