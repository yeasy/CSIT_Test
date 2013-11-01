#!/usr/bin/env python
"""
CSIT test tools.
Authors: Baohua Yang@IBM, Denghui Huang@IBM
Updated: 2013-11-01

Usage: Before running the test tool, should
 1. Start 2-layer tree topology network. e.g., in Mininet, run  'sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2'.
 2. Configure gateway in the controller web GUI, name = 'gateway', subnet = '10.0.0.254/24'.
 3. In Mininet, run 'h1 ping h2' to make sure the network is connected.
"""
import doctest,os
from restlib import *
from testmodule import TestModule


'''
Run single test on given module.
'''
def test_case(module_name):
    print module_name
    cmd = 'python -m doctest '+module_name
    os.system(cmd)

'''
Run test cases according to the given modules.
If no parameter is given, then will scan the case directory,
 and try to run all cases.
'''
def run(modules=None):
    if modules:
        for name in modules:
            test_case(CASES_DIR+'/'+name+'.py')
    else:
        for root,dirs,files in os.walk(CASES_DIR,topdown=True):
            for name in files:
                test_case(root+'/'+name)

'''
This only tests the switchmanager now.
TODO: extend to write a template to all bundles.
'''
if __name__ == '__main__':
    doctest.testmod()
    module_names=['arp_handler','host_tracker','switch_manager']
    run(module_names)
    #run()
