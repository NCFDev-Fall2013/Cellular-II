#====Built-in Modules====#
import Tkinter, tkMessageBox
from ConfigParser import RawConfigParser
from ast import literal_eval as decode
from sys import exit

configFile = 'cellular.ini'

class Settings():
	_changed  = True
	def __init__(self):
		self._settings = RawConfigParser()
		self._funcs	   = (self._getGeneric, self._getInt, self._getFloat, self._getStruct, self._getBool)
		
	def getValue(self, section, option, type):
	"""Returns value from settings file - 0: string/raw value, 1: integer, 2: float, 3: data structure, 4: boolean"""
		if Settings._changed:
			self._fileOpen()
			Settings._changed = False
		return self._funcs[type](select,option)
		
	def changeValue(self, section, option):
		self._settings.set(section, str(option))
		with open('cellular.ini', 'wb') as fp: self._settings.write(fp)
		Settings._changed = True
		
	def _throwError(self, message, title = 'Fatal Error'):
		Tkinter.Tk().withdraw()
		tkMessageBox.showerror(str(title),str(message))
		exit
	
	def _fileOpen(self):
		try fp = open(configFile)
		except IOError: self._throwError('config file not found.\nThe program will now terminate.')
		self._settings.readfp(fp)

	def _getGeneric(self, section, option):
		value = self._settings.get(section, option)
		return value
		
	def _getInt(self, section, option):
		try: value = self._settings.getint(section,option)
		except ValueError: self._throwError('Expected integer, recieved something else at ['+section+'],'+option+'.\nThe program will now terminate.')
		return value

	def _getFloat(self, section, option):
		try: value = self._settings.getfloat(section,option)  
		except ValueError: self._throwError('Expected float, recieved something else at ['+section+'],'+option+'.\nThe program will now terminate.')
		return value

	def _getStruct(self, section, option):
		try value = decode(self._settings.get(section,option))
		except ValueError or SyntaxError: self._throwError('Expected data structure, recieved something else at ['+section+'], '+option+'.\nTheProgram will now terminate.')
		return value

	def _getBool(self, section, option):
		try value = self._settings.getboolean(section,option)
		except ValueError: self._throwError('Expected boolean, recieved something else at ['+section+'], '+option+'.\nThe program will now terminate.')
		return value
