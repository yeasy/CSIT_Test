"""
CSIT test tools.
Authors: Baohua Yang@IBM, Denghui Huang@IBM
Updated: 2013-11-05
"""

from base.restlib import *
from base.testmodule import TestModule


class ForwardingRuleManager(TestModule):
    """
    Test for the forwarding rule manager.
    Start 2-layer tree topology network. e.g., in Mininet, run  'sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2'
    """

    def __init__(self, restSubContext='/controller/nb/v2/flowprogrammer', user=DEFAULT_USER, password=DEFAULT_PWD,
                 container=DEFAULT_CONTAINER, contentType='json', prefix=DEFAULT_PREFIX):
        super(self.__class__, self).__init__(restSubContext, user, password, container, contentType, prefix)

    def get_flows(self, suffix=''):
        """
        The name is suggested to match the NB API.
        Show the flows
        """
        r = super(self.__class__, self).read(suffix)
        if r:
            return r

    def add_flow_to_node(self, node_type, node_id, name, body):
        suffix = 'node/' + node_type + '/' + node_id + '/staticFlow'
        r = super(self.__class__, self).update(suffix + '/' + name, body)
        return r

    def remove_flow_from_node(self, node_type, node_id, name):
        suffix = 'node/' + node_type + '/' + node_id + '/staticFlow'
        r = super(self.__class__, self).delete(suffix + '/' + name)
        return r

    def test_flow_operations(self, node_type, node_id, name, body):
        """
        Test the add,remove,show actions on flows.
        >>> body = {'installInHw':'true','name':'flow1','node':{'id':'00:00:00:00:00:00:00:02','type':'OF'},'priority':'1','etherType':'0x800','nwDst':'10.0.0.1/32','actions':['OUTPUT=1']}
        >>> ForwardingRuleManager().test_flow_operations('OF','00:00:00:00:00:00:00:02','flow1',body)
        True
        >>> body = {'installInHw':'true','name':'flow2','node':{'id':'00:00:00:00:00:00:00:02','type':'OF'},'priority':'1','etherType':'0x800','nwDst':'10.0.0.2/32','actions':['OUTPUT=2']}
        >>> ForwardingRuleManager().test_flow_operations('OF','00:00:00:00:00:00:00:02','flow2',body)
        True
        """
        result = []
        #current flow table should be empty.
        r = self.get_flows()
        result.append(r == None)
        #Add a flow and test if succeed
        self.add_flow_to_node(node_type, node_id, name, body)
        r = self.get_flows()
        result.append(r == body.values())
        #Remove a flow and test if succeed
        self.remove_flow_from_node(node_type, node_id, name)
        r = self.get_flows()
        result.append(r == None)
        return result == [True, True, True]
