"""
CSIT test tools.
Authors: Baohua Yang@IBM, Denghui Huang@IBM
Updated: 2013-11-01
"""

from restlib import *
from testmodule import TestModule

class ArpHandler(TestModule):
    """
    Test for the arp handler.
    Start 2-layer tree topology network. e.g., in Mininet, run  'sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2'
    """
    def __init__(self,restSubContext='/controller/nb/v2/subnetservice',user=DEFAULT_USER, password=DEFAULT_PWD,container=DEFAULT_CONTAINER,contentType='json',prefix=DEFAULT_PREFIX):
       super(self.__class__,self).__init__(restSubContext,user,password,container,contentType,prefix)

    def get_subnets(self,suffix='/subnets'):
        """
        The name is suggested to match the NB API.
        list all subnets and their properties.
        NOTE: This test should pass after configure the gateway name and subnet as 10.0.0.254/24.
        >>> ArpHandler().get_subnets()
        [u'10.0.0.254/24', [], u'gateway']
        """
        r=super(self.__class__,self).read(suffix)
        if r:
            print r
