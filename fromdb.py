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
	multichap = input.split(sep=";")
	for chap in multichap:
		splitbookchapverse = chap.split(sep=":")
		bookchap = splitbookchapverse[0]
		verses = splitbookchapverse[1]
		splitbookchap = bookchap.split(sep=" ")
		book = splitbookchap[0]
		chap = splitbookchap[1]
		splitverses = verses.split(sep="-")
		print(book, chap, verses)
		for verse in range(int(splitverses[0]),int(splitverses[1])+1):
			print(book, chap, verse) 
			atext = getaverse(book, chap, str(verse))
			fintext = fintext+atext
	return fintext


text = getmultiverses('Genesis 1:1-5;Genesis 5:1-5')
print(text)

#pyperclip.copy(text)
#spam = pyperclip.paste()

file = open('out.txt', 'w',encoding="UTF-8")
file.write(text)
file.close()