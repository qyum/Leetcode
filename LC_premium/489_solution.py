#leetcode premium problem(489)
#o(n^4)T | O(N)S

def cleanRooms(robot):
	def  goBack():
		robot.moveRight
		robot.moveRight
		robot.move
		robot.moveRight
		robot.moveRight
	def backTrack(x,y,d):
		robot.clean()
		for idx in range(4):
			new_d=(d+idx)%4
			new_x=x+directions[new_d][0]
			new_y=y+directions[new_d][1]
			if (new_x,new_y) not in seen and robot.move():
				seen.add((new_x,new_y))
				backTrack(new_x,new_y,new_d)
				robot.goBack()
			robot.turnRight()
				

	
	seen=set()
	seen.add((0,0))
	directions=[(-1,0),(0,1),(1,0),(0,-1)]
	backTrack(0,0,0)

