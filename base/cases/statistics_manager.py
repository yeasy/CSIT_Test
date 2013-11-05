"""
CSIT test tools.
Authors: Baohua Yang@IBM, Denghui Huang@IBM
Updated: 2013-11-01
"""

from base.restlib import *
from base.testmodule import TestModule


class StatisticsManager(TestModule):
    """
    Test for the statistics manager.
    Start 2-layer tree topology network. e.g., in Mininet, run  'sudo mn --controller=remote,ip=127.0.0.1 --mac --topo tree,2'
    """
    def __init__(self,restSubContext='/controller/nb/v2/statistics',user=DEFAULT_USER, password=DEFAULT_PWD,container=DEFAULT_CONTAINER,contentType='json',prefix=DEFAULT_PREFIX):
       super(self.__class__,self).__init__(restSubContext,user,password,container,contentType,prefix)

    def get_flow_stats(self,suffix='flow'):
        """
        The name is suggested to match the NB API.
        Show the flows
        >>> StatisticsManager().get_flow_stats()
        True
        True
        True
        """
        r=super(self.__class__,self).read(suffix)
        if r:
            print {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:01'} in r
            print {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:02'} in r
            print {u'type': u'OF', u'id': u'00:00:00:00:00:00:00:03'} in r
