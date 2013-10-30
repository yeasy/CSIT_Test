#!/usr/bin/env python
"""
CIST test tools.
Authors: Denghui Huang@IBM
         Baohua Yang@IBM
Updated: 2013-10-30
"""
from restlib import *
from testmodule import TestModule

class SwitchManager(TestModule):
    """
    Test for the switch manager, including get switch nodes.
    Start 2-layer tree topology network. e.g., in Mininet, run  'sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2'
    """
    def __init__(self,restSubContext='/controller/nb/v2/switchmanager',user=DEFAULT_USER, password=DEFAULT_PWD,container=DEFAULT_CONTAINER,contentType='json',prefix=DEFAULT_PREFIX):
       super(SwitchManager,self).__init__(restSubContext,user,password,container,contentType,prefix)

    def get_switch_nodes(self,suffix='/nodes'):
        """
        list all nodes and their properties
        >>> SwitchManager().get_switch_nodes()
        some output
        """
        r=super(SwitchManager,self).getWithResponse(suffix)
        print r


'''
This only tests the switchmanager now.
TODO: extend to write a template to all bundles.
'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()
