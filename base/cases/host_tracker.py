"""
CSIT test tools.
Authors: Baohua Yang@IBM, Denghui Huang@IBM
Updated: 2013-11-01
"""

from restlib import *
from testmodule import TestModule

class HostTracker(TestModule):
    """
    Test for the host tracker..
    Start 2-layer tree topology network. e.g., in Mininet, run  'sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2'
    """
    def __init__(self,restSubContext='/controller/nb/v2/hosttracker',user=DEFAULT_USER, password=DEFAULT_PWD,container=DEFAULT_CONTAINER,contentType='json',prefix=DEFAULT_PREFIX):
       super(self.__class__,self).__init__(restSubContext,user,password,container,contentType,prefix)

    def get_active_hosts(self,suffix='/hosts/active'):
        """
        The name is suggested to match the NB API.
        list all active hosts, should be done after using h1 ping h2 in mininet
        >>> HostTracker().get_active_hosts()
        True
        True
        """
        r=super(self.__class__,self).read(suffix)
        if r:
            print '10.0.0.1' in r
            print '10.0.0.2' in r
