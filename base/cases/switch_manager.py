"""
CSIT test tools.
Authors: Baohua Yang@IBM, Denghui Huang@IBM
Updated: 2013-11-01
"""
from base.restlib import *
from base.testmodule import TestModule


class SwitchManager(TestModule):
    """
    Test for the switch manager, including read switch nodes.
    Start 2-layer tree topology network. e.g., in Mininet, run  'sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2'
    """

    def __init__(self, restSubContext='/controller/nb/v2/switchmanager', user=DEFAULT_USER, password=DEFAULT_PWD,
                 container=DEFAULT_CONTAINER, contentType='json', prefix=DEFAULT_PREFIX):
        super(self.__class__, self).__init__(restSubContext, user, password, container, contentType, prefix)

    def get_nodes(self):
        """
        The name is suggested to match the NB API.
        list all nodes and their properties
        """
        suffix = 'nodes'
        r = super(self.__class__, self).read(suffix)
        if r:
            return r

    def get_node(self, suffix):
        """
        The name is suggested to match the NB API.
        list nodeconnector and properties of a node.
        """
        r = super(self.__class__, self).read(suffix)
        if r:
            return r

    def add_property_to_node(self, node_type, node_id, property, value):
        """
        Add a property to given node.
        """
        suffix = 'node/' + node_type + '/' + node_id + '/property'
        r = super(self.__class__, self).update(suffix + '/' + property + '/' + str(value))

    def remove_property_from_node(self, node_type, node_id, property):
        """
        Remove a property from given node.
        """
        suffix = 'node/' + node_type + '/' + node_id + '/property'
        r = super(self.__class__, self).delete(suffix + '/' + property)

    def add_property_to_nodeconnector(self, node_type, node_id, nc_type, nc_id, property, value):
        """
        Add a property to given node.
        """
        suffix = 'nodeconnector/' + node_type + '/' + node_id + '/' + nc_type + '/' + nc_id + '/property'
        r = super(self.__class__, self).update(suffix + '/' + property + '/' + str(value))

    def remove_property_from_nodeconnector(self, node_type, node_id, nc_type, nc_id, property):
        """
        Add a property to given node.
        """
        suffix = 'nodeconnector/' + node_type + '/' + node_id + '/' + nc_type + '/' + nc_id + '/property'
        r = super(self.__class__, self).delete(suffix + '/' + property)

    def test_list_nodes(self):
        """
        The name is suggested to match the NB API.
        list all nodes and their properties
        >>> SwitchManager().test_list_nodes()
        True
        """
        r = self.get_nodes()
        if r:
            print ({u'type': u'OF', u'id': u'00:00:00:00:00:00:00:01'} in r and
                   {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:02'} in r and
                   {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:03'} in r)

    def test_node_property_operations(self, node_type, node_id, property, value):
        """
        Test the add,remove,show actions on node properties.

        >>> SwitchManager().test_node_property_operations('OF','00:00:00:00:00:00:00:01','description','Switch1')
        True
        >>> SwitchManager().test_node_property_operations('OF','00:00:00:00:00:00:00:02','description','Switch2')
        True
        >>> SwitchManager().test_node_property_operations('OF','00:00:00:00:00:00:00:03','description','Switch3')
        True
        """
        result=[]
        #current node properties should not include description
        r = self.get_nodes()
        index = r.index({u'type': node_type, u'id': node_id})
        result.append(r[index + 1][property] == {u'value': u'None'})
        #After adding, current node properties should include description
        self.add_property_to_node(node_type, node_id, property, value)
        r = self.get_nodes()
        index = r.index({u'type': node_type, u'id': node_id})
        result.append(r[index + 1][property] == {u'value': value})
        #After removing, current node properties should not include description
        self.remove_property_from_node(node_type, node_id, property)
        r = self.get_nodes()
        index = r.index({u'type': node_type, u'id': node_id})
        result.append(r[index + 1][property] == {u'value': u'None'})
        return result == [True,True,True]

    def test_nodeconnector_property_operations(self, node_type, node_id, nc_type, nc_id, property, value):
        """
        Test the add,remove,show actions on nodeconnector properties.

        >>> SwitchManager().test_nodeconnector_property_operations('OF','00:00:00:00:00:00:00:01','OF','1','bandwidth',1000)
        True
        """
        result=[]
        node_suffix = 'node/' + node_type + '/' + node_id
        #default bw should be 10000000000L
        r = self.get_node(node_suffix)
        index = r.index({u'node': {u'type': node_type, u'id': node_id}, u'type': nc_type, u'id': nc_id})
        default_value = r[index + 1][property]['value']
        #After setting, the value should be the value
        self.add_property_to_nodeconnector(node_type, node_id, nc_type, nc_id, property, value)
        r = self.get_node(node_suffix)
        index = r.index({u'node': {u'type': node_type, u'id': node_id}, u'type': nc_type, u'id': nc_id})
        current_value = r[index + 1][property]['value']
        result.append(current_value == value)
        #After removing, the bandwidth property should be empty
        self.remove_property_from_nodeconnector(node_type, node_id, nc_type, nc_id, property)
        r = self.get_node(node_suffix)
        index = r.index({u'node': {u'type': node_type, u'id': node_id}, u'type': nc_type, u'id': nc_id})
        result.append(property not in r[index + 1])
        self.add_property_to_nodeconnector(node_type, node_id, nc_type, nc_id, property, default_value)
        r = self.get_node(node_suffix)
        index = r.index({u'node': {u'type': node_type, u'id': node_id}, u'type': nc_type, u'id': nc_id})
        current_value = r[index + 1][property]['value']
        result.append(current_value == default_value)
        return result == [True,True,True]
