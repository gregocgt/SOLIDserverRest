#!/usr/bin/python
# -*-coding:Utf-8 -*
##########################################################
# Request example: http://<SOLIDserver-IP>/rest/<service>?<param> [param=URLencode(value)]
###########################################################

import sys
import base64

import requests
import urllib

from mapper import *

################################################################################
class REPONSE:
	def __init__(self):
		self.status_code = 0
		self.content = "[{'error' : 'SOLIDServer unreachable'}]"

	def	__str__(self):
		return 'REPONSE [ERROR]'

class SOLIDserverRest:

	def __init__(self, host, user, password, debug=False):
		self.debug = debug
		self.host = host
		self.user = user
		self.password = password
		self.prefixUrl = 'https://{}/rest/'.format(host)
		
		# Encryption management in function of Python version
		if sys.version_info[0] == 3:
			self.headers = {'X-IPM-Username': base64.b64encode(user.encode()),
							'X-IPM-Password': base64.b64encode(password.encode()),
							'content-type': 'application/json'}
		else:
			self.headers = {'X-IPM-Username': base64.standard_b64encode(user),
							'X-IPM-Password': base64.standard_b64encode(password),
							'content-type': 'application/json'}
		self.lastUrl = ''
		self.resp = None

	def query(self, service, params=None, payload=None, sslVerify=False):
				
		if params == None:
			params = ''
		else:
			if sys.version_info[0] == 3:
				params = urllib.parse.urlencode(params)
			else:
				params = urllib.urlencode(params)

			params = "?{}".format(params)

		#choose methode
		methode = service.replace('_', ' ')
		for mot in methodeMapper:
			if mot in methode:
				methode =  methodeMapper.get(mot)

		#flag_add management
		if methode == 'POST':
			params = "{}{}".format(params, '&add_flag=new_only')
		elif methode == 'PUT':
			params = "{}{}".format(params, '&add_flag=edit_only')

		#choose service
		service = serviceMapper.get(service)
		self.last_url = "{}{}".format(service, params).strip()
		url = "{}{}".format(self.prefixUrl, self.last_url)
		
		#displaying info to debug
		#print("Methode: {}".format(methode))
		#print("URL: {}".format(url))

		#to https communication whithout certificate
		print('Request version:')
		print(requests.__version__)
		requests.urllib3.disable_warnings()
				

		try:
			answer = requests.request(methode, url, headers=self.headers, verify=sslVerify, timeout=2)
		except:
			answer = REPONSE()

		return answer
			


#########################################################################
# Hors Lib
##########################################################################

if __name__ == "__main__":

	print("")
	print("#####################################")
	print("# Module to request SOLIDServer API #")
	print("#####################################")
	print("")
	print("MANUAL")
	print("------")
	print("1. Declare object")
	print("      Your object declaration permits to set:")
	print("         => host = IP adresse of the SOLIDserver server")
	print("         => user = user who want to use")
	print("         => password = password of the user")
	print("")
	print("Object declaration:")
	print('      your_obj = SOLIDserverRest("host", "user", "password")')
	print("")
	print("2. Request to SOLIDserver API")
	print("      You need parameters:")
	print("         => methode = choose your methode in the list below")
	print("         => parameters = Python dico with parameters you want to use")
	print("         => sslVerify = this option permits to check your server SSL certificate. To check you must set: sslVerify=True")
	print("")
	print("Query to SOLIDserver API")
	print('      rest_answer = your_obj.query("methode", "parameters", sslVerify=False)')
	print("")
	print("3. Keep answer")
	print("      print(rest_answer) => object name")
	print("      print(rest_answer.status_code) => current http answer code set in the object")
	print("      print(rest_answer.content) => Answer core from SOLIDserver API set in the object")
	print("")
