
#api taken from https://market.mashape.com/buggythegret/applications/MangaReader

import requests

class MangaRead:
	def __init__(self, name):
		self.headers = {"X-Mashape-Key": "x8313BfGJFmshLJ7AXmykpml1Bylp1uFjcxjsnQVLMTLyvoKrw",
					    "Accept": "text/plain"
					 }
		self.name = name

	def UnseenChapters(self, last_chap):
		# self.us =[]
		resp = requests.get("https://doodle-manga-scraper.p.mashape.com/mangareader.net/manga/{manga_name}/".format(manga_name = self.name),
		  headers= self.headers)
		for x in resp.json()['chapters']:
			if x['chapterId'] >= last_chap:
				yield{'id': x['chapterId'],
						 'name': x['name']
					}
		
	def ViewChapter(self, chapter_no):
		resp = requests.get("https://doodle-manga-scraper.p.mashape.com/mangareader.net/manga/{name}/{chap_no}"
								.format(name = self.name, chap_no = chapter_no), headers = self.headers)
		for i, x in enumerate(resp.json()['pages']):
			yield{'page_no': i, 'photo_link': x}


def main():
	a = MangaRead(name = 'beserk')
	#naruto #one-piece #works on both
	#beserk  #fairy tail #work on view+_chapter

	for x in a.UnseenChapters(last_chap = 90): print(x)

	for x in a.ViewChapter(chapter_no = 4): print(x)
	

if __name__ == '__main__': main()





	



