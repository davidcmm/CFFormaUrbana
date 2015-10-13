# coding=utf-8

import sys
from scipy import stats
import numpy as np

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "Uso: <arquivo com imagens> <arquivo com questionário>"
		sys.exit(1)

	imagesFile = open(sys.argv[1], "r")
	questFile = open(sys.argv[2], "r")

	images = imagesFile.readlines()
	quest = questFile.readlines()
	
	questHeader = quest[0].rstrip('\n\r')
	print questHeader+"\n"

	for question in quest[1:]:
		for image in images:
			#print "teste"
			prevQuest = question.rstrip('\n\r')
			print prevQuest + image.rstrip('\n\r')
	
