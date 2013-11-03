"""
CSIT test tools.
Authors: Baohua Yang@IBM, Denghui Huang@IBM
Updated: 2013-11-01
"""
from restlib import *
from testmodule import TestModule

class SwitchManager(TestModule):
    """
    Test for the switch manager, including read switch nodes.
    Start 2-layer tree topology network. e.g., in Mininet, run  'sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2'
    """
    def __init__(self,restSubContext='/controller/nb/v2/switchmanager',user=DEFAULT_USER, password=DEFAULT_PWD,container=DEFAULT_CONTAINER,contentType='json',prefix=DEFAULT_PREFIX):
       super(self.__class__,self).__init__(restSubContext,user,password,container,contentType,prefix)

    def get_nodes(self,suffix='nodes'):
        """
        The name is suggested to match the NB API.
        list all nodes and their properties
        >>> SwitchManager().get_nodes()
        True
        True
        True
        """
        r=super(self.__class__,self).read(suffix)
        if r:
            print {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:01'} in r
            print {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:02'} in r
            print {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:03'} in r

    def add_property_to_node(self,suffix='node/OF/00:00:00:00:00:00:00:02/property/description/Switch2'):
        """
        Add a property to some node.

        >>> SwitchManager().add_property_to_node()
        201
        """
        r=super(self.__class__,self).update(suffix)
        print r
