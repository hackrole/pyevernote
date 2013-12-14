#!/usr/bin/env python
#coding=utf8

import string


def json_data_print_totable(thead, data, title="no title", d="=", dd='-'):
    """ print the data list with table style """
    c, dl = _max_table_length(thead, data)

    cl = (c - len(title) - 4) / 2
    # TODO print to sys.stdout.write
    print d*cl,title,d*cl
    print ''.join([string.ljust(h, dl[h]) for h in thead])
    print dd*c
    for d in data:
        print ''.join([string.ljust(str(d.get(h)), dl[h]) for h in thead])


def _max_table_length(thead, data):
    """ return lenght info about a table list """
    dl = {}
    for h in thead:
        tmp = [str(d.get(h)) for d in data]
        tmp.append(h)
        dl[h] = _max_length(tmp)

    c = sum(dl.values())
    return (c, dl)


def _max_length(l, space=4):
    """ return length of the max length in a list add with a space """
    def len2(s):
        if s is None:
            return 0
        return len(s)
    return len(max(l, key=len2)) + space



if __name__ == '__main__':
    l = []
    th = ['title', 'guid', 'content', 'create_time', 'update_time']
    for i in range(5):
        o = {}
        o['title'] = "time"
        o['guid'] = "everything at onece"
        o['content'] = 'hello world, I hate you.'
        o['create_time'] = "2012/12/01"
        o['update_time'] = '2013/12/11'
        l.append(o)

    json_data_print_totable(th, l, title="test for print")
