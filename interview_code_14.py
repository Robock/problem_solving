#Given a non-finite stream of characters, output an "A" if the characters "xxx" are found in exactly that sequence.  
#If the characters "xyx" are found instead, output a "B".  
#Do not re-process characters so as to output both an “A” and a “B” when processing the same input. For example:
#1. The following input xxyxyxxxyxxx would produce the following output:  BAA
#2. The following input xxxyxyxxxxyyxyxyx would produce the following output:   ABAB


def abba(sample_string):

	three = ''
	new_string = ''
	
	for ch in sample_string:
		if len(three) == 0:
			if ch == 'x':
				three += ch
			else:
				three = ''
		elif len(three) == 1:
			if ch == 'x' or ch == 'y':
				three += ch
			else:
				three = ''
		elif len(three) == 2:
			if three == 'xx':
				if ch == 'x':
					new_string += 'A'
					three = ''
				elif ch == 'y':
					three = 'xy'
				else:
					three = ''
			elif three == 'xy':
				if ch == 'x':
					new_string += 'B'
					three = ''
				else:
					three = ''
		

	return new_string




print(abba('xxyxyxxxyxxx'))
print(abba('xxxyxyxxxxyyxyxyx'))
