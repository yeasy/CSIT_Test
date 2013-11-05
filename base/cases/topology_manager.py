"""
CSIT test tools.
Authors: Baohua Yang@IBM, Denghui Huang@IBM
Updated: 2013-11-01
"""

from base.restlib import *
from base.testmodule import TestModule


class TopologyManager(TestModule):
    """
    Test for the topology manager.
    Start 2-layer tree topology network. e.g., in Mininet, run  'sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2'
    """

    def __init__(self, restSubContext='/controller/nb/v2/topology', user=DEFAULT_USER, password=DEFAULT_PWD,
                 container=DEFAULT_CONTAINER, contentType='json', prefix=DEFAULT_PREFIX):
        super(self.__class__, self).__init__(restSubContext, user, password, container, contentType, prefix)

    def get_topology(self):
        """
        The name is suggested to match the NB API.
        Show the topology
        >>> TopologyManager().get_topology()
        True
        """
        r = super(self.__class__, self).read()
        if r:
            v = r['edgeProperties']
            for i in range(0, len(r), 2):
                nc = v[i]['edge']
                if nc[u'tailNodeConnector'] == {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:03'},
                                                u'type': u'OF', u'id': u'3'}:
                    if nc[u'headNodeConnector'] != {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:01'},
                                                    u'type': u'OF', u'id': u'2'}:
                        print False
                elif nc[u'tailNodeConnector'] == {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:02'},
                                                  u'type': u'OF', u'id': u'3'}:
                    if nc[u'headNodeConnector'] != {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:01'},
                                                    u'type': u'OF', u'id': u'1'}:
                        print False
                elif nc[u'tailNodeConnector'] == {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:01'},
                                                  u'type': u'OF', u'id': u'1'}:
                    if nc[u'headNodeConnector'] != {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:02'},
                                                    u'type': u'OF', u'id': u'3'}:
                        print False
                elif nc[u'tailNodeConnector'] == {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:01'},
                                                  u'type': u'OF', u'id': u'2'}:
                    if nc[u'headNodeConnector'] != {u'node': {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:03'},
                                                    u'type': u'OF', u'id': u'3'}:
                        print False
                else:
                    print False
            print True

    def get_userlinks(self):
        """
        The name is suggested to match the NB API.
        Show the userlinks.
        """
        suffix = 'userLinks'
        r = super(self.__class__, self).read(suffix)
        if r:
            return r

    def add_userlink(self, name, body):
        """
        Add a userlink.
        """
        suffix = 'userLink'
        r = super(self.__class__, self).update(suffix + '/' + name, body)
        return r

    def remove_userlink(self, name):
        """
        Remove a userlink.
        """
        suffix = 'userLink'
        r = super(self.__class__, self).delete(suffix + '/' + name)
        return r

    def test_userlink_operations(self, name, body):
        """
        Test userlink operations, like adding and removing.
        >>> TopologyManager().test_userlink_operations('link1', {'status':'Success','name':'link1','srcNodeConnector':'OF|1@OF|00:00:00:00:00:00:00:02','dstNodeConnector':'OF|1@OF|00:00:00:00:00:00:00:03'})
        True
        """
        return super(self.__class__, self).test_add_remove_operations('userLinks', 'userLink', name, body, 'userLinks')
