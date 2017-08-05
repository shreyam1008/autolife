#from http://football-data.org api
#api key = 7471c49d30b84a4496de867375dac63f

import requests


class Footy:
	
	def __init__(self):
		self.headers = {'X-Auth-Token': '7471c49d30b84a4496de867375dac63f'}

	def Competition(self, season):
		resp = requests.get('http://api.football-data.org/v1/competitions/?season={season}'.format(season = season), 
                        headers = self.headers)
		for x in range(len(resp.json())):
			yield{'id' : resp.json()[x]['id'],
					'name' : resp.json()[x]['caption']
				}


	def CompetitionTeams(self, league_id):
		import re
		resp = requests.get('http://api.football-data.org/v1/competitions/{league_id}/teams'.format(league_id = league_id), 
                        headers = self.headers)
		for x in resp.json()['teams']:
			yield{'team_id': re.findall(r"\/teams\/(\d{2,3})", str(x['_links']))[0],
					 'name' : x['name']
				}


	def LeagueTable(self, league_id):
		resp = requests.get('http://api.football-data.org/v1/competitions/{league_id}/leagueTable'.format(league_id = league_id),
						 headers = self.headers)
		print(resp.json()['leagueCaption'])
		for x in resp.json()['standing']:
			yield{
				'position': x['position'],
					'teamName': x['teamName'],
						'points': x['points'],
							'goalDifference': x['goalDifference']
			}


	def TeamFixtures(self, team_id):
		resp =  requests.get('http://api.football-data.org/v1/teams/{team_id}/fixtures'.format(team_id = team_id),
						headers = self.headers)
		print(resp.json()['count'])
		for x in resp.json()['fixtures']:
			yield{'homeTeamName': x['homeTeamName'],
					 'homeScore': x['result']['goalsHomeTeam'], 
					 	'awayScore': x['result']['goalsAwayTeam'],
					 		 'awayTeamName': x['awayTeamName'],
				}

				
	def TeamPlayers(self, team_id):
		resp = requests.get('http://api.football-data.org/v1/teams/{team_id}/players'.format(team_id = team_id),
						headers = self.headers)
		for x in resp.json()['players']:
			yield{
				'name': x['name'],
					'position': x['position']
			}


def main():
	pass
	a = Footy()

	for x in a.Competition(season = 2016): print(x)

	# for x in a.CompetitionTeams(league_id = 426): print(x)

	# for x in a.LeagueTable(league_id = 426): print(x)

	for x in a.TeamFixtures(team_id = 65): print(x)

	# for x in a.TeamPlayers(team_id = 65): print(x)




if __name__ == '__main__': main()

