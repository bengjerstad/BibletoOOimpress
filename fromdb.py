# -*- coding: UTF-8 -*-
import sys
import json
import sqlite3
import time
import pyperclip

conn = sqlite3.connect('esv.db')
c = conn.cursor()

def getaverse(book,chapter,verse):
	x = c.execute("SELECT * FROM "+book+" WHERE chapter = ? AND verse = ?",(chapter,verse))
	for y in x:
		text = y[2]
		return verse,text



v,text = getaverse('Genesis','1','5')

#print("{}\u00b2".format())
SUP = str.maketrans("0123456789", u"⁰¹²³⁴⁵⁶⁷⁸⁹")
v=v.translate(SUP)
pyperclip.copy(v+text)
#spam = pyperclip.paste()