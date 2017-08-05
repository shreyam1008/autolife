#database for all aspects of the program
import sqlite3

class DatabaseForAll:
	def __init__(self, **kwargs):
		self.filename = kwargs.get('filename', 'mastertable.db')
		self.tablename = kwargs.get('tablename')
		self.CreateTable()

	def CreateTable(self):
		
		if self.tablename ==  'login_table':
			cmd = '''CREATE TABLE IF NOT EXISTS login_table (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
						username TEXT, password TEXT)'''

		if self.tablename ==  'series_table':
			cmd = '''CREATE TABLE IF NOT EXISTS series_table (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
						name TEXT, season INT, last_epi text, link text)''' 
		if self.tablename == 'football_table':
			pass
		if self.tablename == 'movie_table':
			pass
		if self.tablename == 'manga_table':
			pass
		if self.tablename == 'song_table':
			pass
		self.db.execute(cmd)
			
		self.db.commit()

	def AddToTable(self, **kwargs):
		if self.tablename ==  'login_table':
			self.db.execute('INSERT INTO login_table (username, password) VALUES (?, ?)',
								 (kwargs.get('username'), kwargs.get('password')))
		if self.tablename ==  'series_table':
			self.db.execute('INSERT INTO series_table (name, season, last_epi, link) VALUES (?, ?, ?, ?)',
								 (kwargs.get('name'), kwargs.get('season', 1), kwargs.get('last_epi', 1), kwargs.get('link', 'www.gomovies.to'))) 
		if self.tablename == 'football_table':
			pass
		if self.tablename == 'movie_table':
			pass
		if self.tablename == 'manga_table':
			pass
		if self.tablename == 'song_table':
			pass
		self.db.commit()


	def GetTable(self):
		self.CreateTable()
		return self.db.execute('SELECT * FROM {}'.format(self.tablename))

	def __iter__(self):
		cursor = self.db.execute('SELECT * FROM {}'.format(self.tableName))
		for row in cursor: yield dict(row)

	@property
	def filename(self): return self._filename
	@filename.setter
	def filename(self, fn):
		self._filename = fn
		self.db = sqlite3.connect(fn)
		self.db.row_factory = sqlite3.Row
	@filename.deleter
	def filename(self):
		self.db.close()
		# del self._filename

	# @property
	# def tablename(self): return _tablename
	# @tablename.setter
	# def tablename(self, tn): self._tablename = tn
	# @tablename.deleter
	# def tablename(self):
	# 	pass
	# 	# self._tablename = 'test'


def main():
	ser = DatabaseForAll(filename = 'mastertable.db', tablename = 'series_table')
	login = DatabaseForAll(tablename = 'login_table')

	# login.AddToTable(username = 'chopper', password = 'tonytony')
	# ser.AddToTable(name = 'the flash', season = 2, last_epi = 18)
	

if __name__ == '__main__': main()