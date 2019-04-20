stack_queue = [1,2,3,4]
stack = []


for i in range(len(stack_queue)):

	print stack_queue
	stack.append(stack_queue.pop())
	print "-> \t"+str(stack)

stack_queue.append(24)

print "----------------"

for i in range(len(stack)):
	print stack
	stack_queue.append(stack.pop())
	print "-> \t"+str(stack_queue)
