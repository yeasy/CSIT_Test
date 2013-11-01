"""
CIST test tools.
Authors: Denghui Huang@IBM
		 Baohua Yang@IBM
Updated: 2013-10-30
"""

from restlib import *


class TestModule(object):
    """
    Basic module class for test restful APIS.
    Support the standard Create, Read, Update, Delete (CRUD) actions.
    """
    def __init__(self,restSubContext,user=DEFAULT_USER, password=DEFAULT_PWD,container=DEFAULT_CONTAINER,contentType='json',prefix=DEFAULT_PREFIX):
        self.restSubContext=restSubContext
        self.container=container
        self.user = user
        self.password = password
        self.contentType=contentType
        self.prefix=prefix

    def create(self,suffix,body=None):
        """
        PUT to given suffix url.
        TODO: complete
        """
        url = self.prefix+self.restSubContext+'/'+self.container+suffix
        if body: #create with body
            pass
        else: #create without body
            pass

    def read(self,suffix):
        """
        GET from given suffix url.
        """
        url = self.prefix+self.restSubContext+'/'+self.container+suffix
        return do_get_request_with_response_content(url, self.contentType, self.user, self.password)

    def update(self,suffix,body=None):
        """
        POST to given suffix url.
        TODO: complete
        """
        url = self.prefix+self.restSubContext+'/'+self.container+suffix
        if body: #create with body
            pass
        else: #create without body
            pass

    def delete(self,suffix):
        """
        DELETE to given suffix url.
        TODO: complete
        """
        pass
