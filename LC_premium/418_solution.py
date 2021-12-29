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



#leetcode premium problem(418) 2nd solution using DP
#sentence screen fitting
#O(n)T | O(n)S

def  wordTyping(sentences,rows,col):
	s=’ ‘ .join(sentences)+’ ‘
	totalLen=len(s)
	backtrack=[0]*len(totalLen)
	
	preTrack=-1
	for i in range(totalLen):
		If s[i]==’ ‘:
			preTrack=i
		backTrack[i]=i-(preTrack+1)

	position=0
	for rowIdx in rows:
		position  += col
		position =position-backtrack[position %totalLen]

	return (position+1)//totalLen
