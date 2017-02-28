# -*- coding: UTF-8 -*-
import sys
import json
import sqlite3
import time
import pyperclip

conn = sqlite3.connect('esv.db')
c = conn.cursor()

def getaverse(book,chapter,verse):
	SUP = str.maketrans("0123456789", u"⁰¹²³⁴⁵⁶⁷⁸⁹")
	v=verse.translate(SUP)
	x = c.execute("SELECT * FROM "+book+" WHERE chapter = ? AND verse = ?",(chapter,verse))
	for y in x:
		text = y[2]
		return v+text

def getmultiverses(input):
	fintext = ''
	#parse the input
	
	#loop for each verse. 
	atext = getaverse('Genesis','1','5')
	#combine the txt for loops.
	fintext = atext
	
	return fintext


text = getmultiverses('Genesis 1:1-5')

#pyperclip.copy(text)
#spam = pyperclip.paste()

file = open('out.txt', 'w',encoding="UTF-8")
file.write(text)
file.close()