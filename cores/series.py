#try using tvdb api
# https://api.thetvdb.com
'''
data = {"apikey": "xxx",
			 "userkey": "xxx",
			  "username": "xxx"
			}
	'''

import requests
import json

class SeriesNAnime():

	def __init__(self, name, season):
		self.headers = {'Content-Type' : 'application/json', 'Accept': 'application/json',
						 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0OTYwNzI0NTAsImlkIjoibWFuZ2FyZWFkZXIiLCJvcmlnX2lhdCI6MTQ5NTk4NjA1MCwidXNlcmlkIjo0Nzk5MTksInVzZXJuYW1lIjoicmFqZXNoX2tvb3RyYXBhbGkifQ.rN036_yLRICT1-r7QI6EANVZBmixburmc7ol05EXg-k7j-GWMHPBio7qFdfroxm_-YdZlvOf0RE94UGF5W0rIIZ2-5FfykYJ6yE8YBrr12nKDf1Fu_evHpqFHo0DqfOd3r0EDhxsxOOPSuWGLGRKIfYrMK6uVTpOWItAy_Aj-v06csyfDRed-ZS1hRIJdVd7qTJwcbrD-U4Xz5BHQkqNXnqsrhyAqsKkUvgOo37vPpB-gjB0GiC7sXJTa-cXRwklFfpw95KpjZBsxc3odtgWP43-oKS3b9x0L5JBlA7H8G6457XL-puKinZlTofyjPuN_UF0fUayPkLo1okBTTFF1A'}
		self.series_name = name
		self.season = season

	def epiList(self):
		resp = requests.get('https://api.thetvdb.com/series/{id}/episodes'.format(id = self.id),
								 headers = self.headers)

		data = resp.json()['data']
		for x in data:
			if(x['airedSeason'] == self.season):
				yield{'epi_name':x['episodeName'],
						'epi_number':x['airedEpisodeNumber']}

	def samenames(self):
		for no, x in enumerate(self.data): yield{'no': no,'seriesname': x['seriesName'], 'date': x['firstAired']}

	def seaosnNumber(self):
		resp = requests.get('https://api.thetvdb.com/series/{id}/episodes'.format(id = self.id),
								 headers = self.headers)

		data = resp.json()['data']
		seaosns = []
		for x in data:
			seaosns.append(x['airedSeason'])
		return(max(seaosns)) 


	def unseen(self, last_epi):
		'''itterable object.returns unseen episodes in tuple foremat]
		(episode_number, 'epsode_name', 'release dae')
		'''
		resp = requests.get('https://api.thetvdb.com/series/{id}/episodes'.format(id = self.id),
								 headers = self.headers)
		data = resp.json()['data']
		for x in data:
			if ((x['airedSeason'] == self.season) and (x['airedEpisodeNumber'] >= last_epi + 1)):
				yield{'epi_number' : x['airedEpisodeNumber'],
						 'epi_name' : x['episodeName'],
							 'aired_date' : x['firstAired']}

	def get_link(self):
		import bs4 as bs
		import re
		resp = requests.get('https://gomovies.to/movie/search/{}'.format(self.series_name.replace(' ', '+')))
		search = 'film/' + self.series_name.replace(' ', '-') + '-season-' + str(self.season)
		soup = bs.BeautifulSoup(resp.text, 'lxml')
		for links in soup.find_all('a'):
		  if re.search(search, str(links.get('href'))): return(links.get('href'))


	@property
	def series_name(self): return self._series_name
	@series_name.setter
	def series_name(self, sn):
		self._series_name = sn
		try:
			resp = requests.get('https://api.thetvdb.com/search/series?name={}'.format(self.series_name),
									 headers = self.headers)
			data = resp.json()['data']
		except:
			key = '{"apikey": "047D9161230D8AED", "userkey": "167A6DDFFE15D5F8", "username": "rajesh_kootrapali"}'
			resp = requests.post('https://api.thetvdb.com/login', headers = self.headers, data = key)
			self.headers = {'Content-Type' : 'application/json', 'Accept': 'application/json',
								'Authorization': 'Bearer {}'.format(resp.json()['token'])}
			resp = requests.get('https://api.thetvdb.com/search/series?name={}'.format(self.series_name),
									 headers = self.headers)
			data = resp.json()['data']

		# # temp = int(input('Enter the no of the series:'))
		temp = 0
		self.id = data[temp]['id']


		

				
		
				

def main():
	a = SeriesNAnime(name = 'game of thrones', season = 4)

	for x in a.epiList(): print(x)

	print(a.seaosnNumber())
	
	# for x in a.unseen(last_epi = 5): print(x)
	# print(a.get_link())

if __name__ == '__main__': main()
