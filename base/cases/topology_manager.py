"""
CSIT test tools.
Authors: Baohua Yang@IBM, Denghui Huang@IBM
Updated: 2013-11-01
"""

from restlib import *
from testmodule import TestModule

class TopologyManager(TestModule):
    """
    Test for the topology manager.
    Start 2-layer tree topology network. e.g., in Mininet, run  'sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2'
    """
    def __init__(self,restSubContext='/controller/nb/v2/topology',user=DEFAULT_USER, password=DEFAULT_PWD,container=DEFAULT_CONTAINER,contentType='json',prefix=DEFAULT_PREFIX):
       super(self.__class__,self).__init__(restSubContext,user,password,container,contentType,prefix)

    def get_topology(self,suffix=''):
        """
        The name is suggested to match the NB API.
        Show the topology
        >>> TopologyManager().get_topology()
        8
        True
        True
        True
        True
        """
        r=super(self.__class__,self).read(suffix)
        if r:
            print len(r)
            print {u'tailNodeConnector': {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:01'}, u'type': u'OF', u'id': u'2'}, u'headNodeConnector': {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:03'}, u'type': u'OF', u'id': u'3'}} in r
            print {u'tailNodeConnector': {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:01'}, u'type': u'OF', u'id': u'1'}, u'headNodeConnector': {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:02'}, u'type': u'OF', u'id': u'3'}} in r
            print {u'tailNodeConnector': {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:02'}, u'type': u'OF', u'id': u'3'}, u'headNodeConnector': {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:01'}, u'type': u'OF', u'id': u'1'}} in r
            print {u'tailNodeConnector': {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:03'}, u'type': u'OF', u'id': u'3'}, u'headNodeConnector': {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:01'}, u'type': u'OF', u'id': u'2'}} in r
