"""
CIST test tools.
Authors: Denghui Huang@IBM
		 Baohua Yang@IBM
Updated: 2013-10-30
"""

from restlib import *


class TestModule(object):
    """
    Basic module class for test.
    """
    def __init__(self,restSubContext,user=DEFAULT_USER, password=DEFAULT_PWD,container=DEFAULT_CONTAINER,contentType='json',prefix=DEFAULT_PREFIX):
        self.restSubContext=restSubContext
        self.container=container
        self.user = user
        self.password = password
        self.contentType=contentType
        self.prefix=prefix

    def get_with_response(self,suffix):
        url = self.prefix+self.restSubContext+'/'+self.container+suffix
        return do_get_request_with_response_content(url, self.contentType, self.user, self.password)
