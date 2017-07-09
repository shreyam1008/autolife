#using api from themoviedb.org
#api key api_key = 43bbcd5a5cc0c93679fefe0899614809


#request token for today = 5461196738e7787b9120a0986db8d76f9d7353b2

import requests

class Movies(object):
	"""docstring for Movies"""
	def __init__(self):
		super(Movies, self).__init__()
		
	def get_request_token(self):
		url = "https://api.themoviedb.org/3/authentication/token/new"
		data = {'api_key': '43bbcd5a5cc0c93679fefe0899614809'}
		resp = requests.get(url,  data = data)

		print(resp.text)
		print(resp.json()['request_token'])







def main():
	a = Movies()
	a.get_request_token()

if __name__ == '__main__': main()