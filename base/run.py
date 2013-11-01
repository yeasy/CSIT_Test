#!/usr/bin/env python
"""
CIST test tools.
Authors: Denghui Huang@IBM
         Baohua Yang@IBM
Updated: 2013-10-30
"""
from restlib import *
from testmodule import TestModule
from switch_manager import SwitchManager


'''
This only tests the switchmanager now.
TODO: extend to write a template to all bundles.
'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()
