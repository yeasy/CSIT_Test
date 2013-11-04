"""
CSIT test tools.
Authors: Denghui Huang@IBM, Baohua Yang@IBM
Updated: 2013-10-30
"""
import requests
import json
from requests.auth import HTTPBasicAuth

# Global variables
DEFAULT_CONTROLLER_IP = '127.0.0.1'
#DEFAULT_CONTROLLER_IP = '9.186.105.113' #just for temp test
DEFAULT_PORT = '8080'
DEFAULT_PREFIX = 'http://'+DEFAULT_CONTROLLER_IP+':'+DEFAULT_PORT
DEFAULT_CONTAINER = 'default'
DEFAULT_USER = 'admin'
DEFAULT_PWD = 'admin'
CASES_DIR='cases'
TIMEOUTS=5

'''
Send a POST request.
'''
def do_post_request(url, content_type, payload=None, user=DEFAULT_USER, password=DEFAULT_PWD):
	if content_type == 'json':
		headers = {'Content-type' : 'application/json', 'Accept' : 'text/plain'}
		if payload == None:
			data = None
		else:
			data = json.dumps(payload)
			print data
	elif content_type == 'xml':
		headers = {'Content-type' : 'application/xml', 'Accept' : 'text/plain'}
	else:
		print 'unsupported content-type'
	try:
		r = requests.post(url, data, headers = headers, auth=(user, password), timeout=TIMEOUTS)
		r.raise_for_status()
	except (requests.exceptions.HTTPError, requests.exceptions.Timeout) as e:
		return 400 
	else:
		return r.status_code

'''
Send a GET request.

@return The status code.
'''
def do_get_request_with_status_code(url, content_type, user=DEFAULT_USER, password=DEFAULT_PWD):
	try:
		r = requests.get(url, auth=(user, password), timeout=TIMEOUTS)
		r.raise_for_status()
	except (requests.exceptions.HTTPError, requests.exceptions.Timeout) as e:
		print e
		return r.status_code
	else:
		return r.status_code

'''
Send a PUT request.

@return The status code.
'''
def do_put_request(url, content_type, payload=None, user=DEFAULT_USER, password=DEFAULT_PWD):
	if content_type == 'json':
		headers = {'Content-type' : 'application/json', 'Accept' : '*/*'}
		if payload == None:
			data=None
		else:
			data = json.dumps(payload)
			data={
				"status":"Success",
				"name":"link1",
				"srcNodeConnector":"OF|1@OF|00:00:00:00:00:00:00:01",
				"dstNodeConnector":"OF|1@OF|00:00:00:00:00:00:00:02"
			}
	elif content_type == 'xml':
		headers = {'Content-type' : 'application/xml', 'Accept' : 'text/plain'}
	else:
		print 'unsupported content-type'
	try:
		r = requests.put(url, data, headers = headers, auth=(user, password), timeout=TIMEOUTS)
		r.raise_for_status()
	except (requests.exceptions.HTTPError, requests.exceptions.Timeout) as e:
		print headers,data
		print e
		return 400 
	else:
		return r.status_code

'''
Send a DELETE request.

@return The status code.
'''
def do_delete_request(url, user=DEFAULT_USER, password=DEFAULT_PWD):
	try:
		r = requests.delete(url, auth=(user, password), timeout=TIMEOUTS)
		r.raise_for_status()
	except (requests.exceptions.HTTPError, requests.exceptions.Timeout) as e:
		print e
		return r.status_code
	else:
		return r.status_code

'''
Convert the result content to list.
'''
def convert_result_to_list(result):
	list2 = []
	#print result
	content = result.values()
	for list1 in content:
		list2 = [dict1.values() for dict1 in list1]
	#print list2
	list3 = []
	for list4 in list2:
		for element in list4:
			list3.append(element)
	#print list3
	return list3

'''
Send a GET request and get the response.
@return response content as list.
'''
def do_get_request_with_response_content(url, content_type, user=DEFAULT_USER, password=DEFAULT_PWD):
	try:
		#print url
		r = requests.get(url, auth=(user,password), timeout=TIMEOUTS)
		r.raise_for_status()
	except (requests.exceptions.HTTPError, requests.exceptions.Timeout) as e:
		print e
		return None
	else:
		if r != None:
			if content_type == 'json':
				content = r.json()
				#print content
				return convert_result_to_list(content)
			elif content_type == 'xml':#TODO: add parser to xml
				return None

if __name__ == '__main__':
	pass
