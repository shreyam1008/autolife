import re
import urllib.request
import requests
from bs4 import BeautifulSoup
 
class Songs():
	def __init__(self, artist, song_title):
		self.artist = artist
		self.song_title = song_title

	def getLyrics(self):
		self.artist = self.artist.lower()
		self.song_title = self.song_title.lower()
		# remove all except alphanumeric characters from self.artist and self.song_title
		self.artist = re.sub('[^A-Za-z0-9]+', "", self.artist)
		self.song_title = re.sub('[^A-Za-z0-9]+', "", self.song_title)
		if self.artist.startswith("the"):    # remove starting 'the' from self.artist e.g. the who -> who
			self.artist = self.artist[3:]
		url = "http://azlyrics.com/lyrics/"+self.artist+"/"+self.song_title+".html"
		
		# try:
		content = requests.get(str(url))
		print(content.text)
		soup = BeautifulSoup(content, 'html.parser')
		lyrics = str(soup)
		# lyrics lies between up_partition and down_partition
		up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
		down_partition = '<!-- MxM banner -->'
		lyrics = lyrics.split(up_partition)[1]
		lyrics = lyrics.split(down_partition)[0]
		lyrics = lyrics.replace('<br>','').replace('</br>','').replace('</div>','').strip()
		return lyrics
		# except Exception as e:
		#     return "Exception occurred \n" +str(e)

 
def main():
	a = Songs(artist = 'sia', song_title = 'cheap thrills')

	print(a.getLyrics())

if __name__ == '__main__':
	main()