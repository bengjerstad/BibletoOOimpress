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
	fintext = []
	fintextindex = 0
	slidelength = 262
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
			#remove newline char.
			atext = "".join(atext.split('\n'))
			#splitverese into slides
			#262 for the first one 290 for the rest
			try:
				lenlast = len(fintext[fintextindex])
			except:
				lenlast = 0
			lenthis = len(atext)
			print(lenlast,lenthis)
			if lenthis+lenlast > slidelength:
				#advance to next slide
				fintext.append(atext)
				fintextindex = fintextindex + 1
				slidelength = 290
				
			elif (lenlast == 0):
				fintext.append(atext)
			else:
				print(fintextindex)
				fintext[fintextindex] = fintext[fintextindex]+atext
	return fintext


text = getmultiverses('Genesis 1:1-10')
print(text)



#pyperclip.copy(text)
#spam = pyperclip.paste()

file = open('out.txt', 'w',encoding="UTF-8")
for outtext in text:
	file.write(outtext)
	file.write('\n\n')
file.close()