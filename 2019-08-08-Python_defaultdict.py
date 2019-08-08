# Python 3.7.4
# https://pymotw.com/3/collections/defaultdict.html
# Tested on https://repl.it 

import collections


def default_factory():
    return 'default value'


d = collections.defaultdict(default_factory, foo='bar')
print('d:', d)
print('foo =>', d['foo'])
print('bar =>', d['bar'])
# eof
