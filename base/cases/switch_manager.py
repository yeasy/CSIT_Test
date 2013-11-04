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

    def get_nodes(self):
        """
        The name is suggested to match the NB API.
        list all nodes and their properties
        """
        suffix='nodes'
        r=super(self.__class__,self).read(suffix)
        if r:
            return r

    def get_node(self,suffix):
        """
        The name is suggested to match the NB API.
        list nodeconnector and properties of a node.
        """
        r=super(self.__class__,self).read(suffix)
        if r:
            print r

    def add_property_to_node(self,suffix):
        """
        Add a property to given node.
        """
        r=super(self.__class__,self).update(suffix)

    def remove_property_from_node(self,suffix):
        """
        Remove a property from given node.
        """
        r=super(self.__class__,self).delete(suffix)

    def test_list_nodes(self):
        """
        The name is suggested to match the NB API.
        list all nodes and their properties
        >>> SwitchManager().test_list_nodes()
        True
        """
        r=self.get_nodes()
        if r:
            print ({u'type': u'OF', u'id': u'00:00:00:00:00:00:00:01'} in r and \
                   {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:02'} in r and \
                   {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:03'} in r)

    def test_node_property_operations(self,suffix,property,value):
        """
        Test the add,remove,show actions on node properties.
        Remove a property from given node.

        >>> SwitchManager().test_node_property_operations('node/OF/00:00:00:00:00:00:00:02/property','description','Switch2')
        True
        True
        True
        """
        #current node properties should not include description
        r=self.get_nodes()
        index = r.index({u'type': u'OF', u'id': u'00:00:00:00:00:00:00:02'})
        print r[index+1][property] == {u'value': u'None'}
        #After adding, current node properties should include description
        self.add_property_to_node(suffix+'/'+property+'/'+value)
        r=self.get_nodes()
        index = r.index({u'type': u'OF', u'id': u'00:00:00:00:00:00:00:02'})
        print r[index+1][property] ==  {u'value': value}
        #After removing, current node properties should not include description
        self.remove_property_from_node(suffix+'/'+property)
        r=self.get_nodes()
        index = r.index({u'type': u'OF', u'id': u'00:00:00:00:00:00:00:02'})
        print r[index+1][property] ==  {u'value': u'None'}
