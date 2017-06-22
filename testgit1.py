"""
noting but still test
"""

import time

def test0():
    now = time.asctime()
    print now,
    print 'is that what you want?'


def test_sys_exit():

    for _ in range(10):
        print 'Hello conda!'


if(__name__ == '__main__'):
    import sys
    sys.exit(test_sys_exit())
    print 'done!'