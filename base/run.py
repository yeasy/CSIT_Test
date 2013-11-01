#!/usr/bin/env python
"""
CSIT test tools.
Authors: Baohua Yang@IBM, Denghui Huang@IBM
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
    SwitchManager().get_nodes()
