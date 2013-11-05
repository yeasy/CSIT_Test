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
        suffix = 'hosts/active'
        r=super(self.__class__,self).read(suffix)
        if r:
            return r

    def add_host(self, host_id, body):
        """
        Add a host.
        """
        suffix = 'address'
        r = super(self.__class__, self).update(suffix + '/' + host_id, body)

    def remove_host(self, host_id):
        """
        Remove a host.
        """
        suffix = 'address'
        r = super(self.__class__, self).delete(suffix + '/' + host_id)

    def test_host_operations(self, host_id, body):
        """
        Test host operations, like adding and removing.
        >>> HostTracker().test_host_operations('10.0.0.1',{'nodeType': 'OF', 'dataLayerAddress': '8e:ad:13:44:4d:8c', 'vlan': '0', 'nodeId': '00:00:00:00:00:00:00:02', 'nodeConnectorId': '1', 'networkAddress': '10.0.0.1', 'staticHost': True, 'nodeConnectorType': 'OF'})
        True
        """
        result = []
        #Add a host and test if succeed
        self.add_host(host_id, body)
        r = self.get_hosts()
        result.append(body in r['hostConfig'])
        #Remove the added host and test if succeed
        self.remove_host(host_id)
        r = self.get_hosts()
        result.append(body not in r['hostConfig'])
        return result == [True, True]
