"""
CSIT test tools.
Authors: Baohua Yang@IBM, Denghui Huang@IBM
Updated: 2013-11-01
"""

from base.restlib import *
from base.testmodule import TestModule


class HostTracker(TestModule):
    """
    Test for the host tracker..
    Start 2-layer tree topology network. e.g., in Mininet, run  'sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2'
    """
    def __init__(self,restSubContext='/controller/nb/v2/hosttracker',user=DEFAULT_USER, password=DEFAULT_PWD,container=DEFAULT_CONTAINER,contentType='json',prefix=DEFAULT_PREFIX):
       super(self.__class__,self).__init__(restSubContext,user,password,container,contentType,prefix)

    def get_hosts(self):
        """
        The name is suggested to match the NB API.
        list all active hosts, should be done after using h1 ping h2 in mininet
        """
        return super(self.__class__, self).get_entries('hosts/active')

    def add_host(self, name, body):
        """
        Add a host.
        """
        r = super(self.__class__, self).add_entry('address', name, body)

    def remove_host(self, name):
        """
        Remove a host.
        """
        r = super(self.__class__, self).remove_entry('address', name)

    def test_host_operations(self, name, body):
        """
        Test host operations, like adding and removing.
        >>> HostTracker().test_host_operations('10.0.0.1',{'nodeType': 'OF', 'dataLayerAddress': '8e:ad:13:44:4d:8c', 'vlan': '0', 'nodeId': '00:00:00:00:00:00:00:02', 'nodeConnectorId': '1', 'networkAddress': '10.0.0.1', 'staticHost': True, 'nodeConnectorType': 'OF'})
        True
        >>> HostTracker().test_host_operations('10.0.0.4',{'nodeType': 'OF', 'dataLayerAddress': '5e:bf:79:84:10:a6', 'vlan': '0', 'nodeId': '00:00:00:00:00:00:00:03', 'nodeConnectorId': '2', 'networkAddress': '10.0.0.4', 'staticHost': True, 'nodeConnectorType': 'OF'})
        True
        """
        r = super(self.__class__, self).test_add_remove_operations('hosts/active', 'address', name, body, 'hostConfig')
        return r == [True, True]
