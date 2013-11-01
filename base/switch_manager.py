from restlib import *
from testmodule import TestModule

class SwitchManager(TestModule):
    """
    Test for the switch manager, including get switch nodes.
    Start 2-layer tree topology network. e.g., in Mininet, run  'sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2'
    """
    def __init__(self,restSubContext='/controller/nb/v2/switchmanager',user=DEFAULT_USER, password=DEFAULT_PWD,container=DEFAULT_CONTAINER,contentType='json',prefix=DEFAULT_PREFIX):
       super(SwitchManager,self).__init__(restSubContext,user,password,container,contentType,prefix)

    def get_nodes(self,suffix='/nodes'):
        """
        The name is suggested to match the NB API.
        list all nodes and their properties
        >>> SwitchManager().get_nodes()
        some output
        """
        r=super(SwitchManager,self).get_with_response(suffix)
        print r
