def getMilestoneDays(revenues, milestones):
	
	milestones.sort()

	currentMilestone = 0
	totalSum = 0
	length = len(milestones)
	rtnarr = [0]*length
	i = 0

	while i <= len(revenues):
		if(totalSum >=  milestones[currentMilestone]):
			rtnarr[currentMilestone] = i
			currentMilestone = nextMilestone(length, currentMilestone)
			if(currentMilestone == -1):
				break
		else:
			totalSum += revenues[i]
			i += 1

	return rtnarr

def nextMilestone(length, currentMilestone):
	if(currentMilestone+1 >= length):
		return -1
	return currentMilestone+1

def check(a, b):
	if(a == b):
		return "Correct!"
	return "Incorrect :("

revenues_1 = [100, 200, 300, 400, 500]
milestones_1 = [300, 800, 1000, 1400]
expected_1 = [2, 4, 4, 5]
output_1 = getMilestoneDays(revenues_1, milestones_1)
print(check(expected_1, output_1))

revenues_2 = [700, 800, 600, 400, 600, 700]
milestones_2 = [3100, 2200, 800, 2100, 1000] 
expected_2 = [5, 4, 2, 3, 2]
output_2 = getMilestoneDays(revenues_2, milestones_2)
print(check(expected_2, output_2))