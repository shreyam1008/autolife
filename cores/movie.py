#using api from themoviedb.org
#api key api_key =xxx


#request token for today = xxx
import requests

class Movies(object):
	"""docstring for Movies"""
	def __init__(self):
		super(Movies, self).__init__()
		
	def get_request_token(self):
		url = "https://api.themoviedb.org/3/authentication/token/new"
		data = {'api_key': 'xxx'}
		resp = requests.get(url,  data = data)

		print(resp.text)
		print(resp.json()['request_token'])







def main():
	a = Movies()
	a.get_request_token()

if __name__ == '__main__': main()
