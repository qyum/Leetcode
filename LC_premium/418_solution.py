#leetcode premium problem(418)
#sentence screen fitting
#O(n*m)T | O(1)S

def  wordTyping(sentences,rows,col):
	joinWord=" ".join(sentences)+" "
	senLen=len(joinWord)

	totalLen=0
	for rowIdx in range(rows):
		totalLen += col
		if joinWord[totalLen % senLen]==" ":
			totalLen += 1
		else:
			while joinWord[(totalLen-1) % senLen] != " " and totalLen>0:
				totalLen -=1
	return totalLen//senLen
