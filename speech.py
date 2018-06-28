#!/usr/bin/python2

from espeak import espeak

while True:
	s = raw_input()
	if not s =='exit':
		espeak.synth(s)
	else:
		break;
