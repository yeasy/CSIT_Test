"""
CSIT test tools.
Authors: Baohua Yang@IBM, Denghui Huang@IBM
Updated: 2013-11-01
"""

from restlib import *
from testmodule import TestModule

class ContainerManager(TestModule):
    """
    Test for the container manager.
    Start 2-layer tree topology network. e.g., in Mininet, run  'sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2'
    """
    def __init__(self,restSubContext='/controller/nb/v2/containermanager',user=DEFAULT_USER, password=DEFAULT_PWD,container=DEFAULT_CONTAINER,contentType='json',prefix=DEFAULT_PREFIX):
       super(self.__class__,self).__init__(restSubContext,user,password,container,contentType,prefix)

    def get_containers(self,suffix='containers'):
        """
        The name is suggested to match the NB API.
        Show the flows
        >>> ContainerManager().get_containers()
        """
        self.container = None
        r=super(self.__class__,self).read(suffix)
        if r:
            print r