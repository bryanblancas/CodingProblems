class MyQueue(object):
    def __init__(self):
        self.stack_queue = []
        self.lenght = 0
        self.stack = []        
    
    def peek(self):
        a = self.stack_queue.pop()
        self.stack_queue.append(a)
        return a
        
    def pop(self):
        
        a = self.stack_queue.pop()
        self.lenght -= 1
        

    def put(self, value):
        
        if(self.lenght == 0):
            self.stack_queue.append(value)
        else:            
            #print("------")
            #print(self.stack_queue)

            for i in range(self.lenght):
                self.stack.append(self.stack_queue.pop())
            self.stack_queue.append(value)
            
            #print(self.stack)

            for i in range(self.lenght):
                self.stack_queue.append(self.stack.pop())

            #print(self.stack_queue)
            #print("------")

        self.lenght += 1
        
queue = MyQueue()

file = open("input_myqueue.txt", 'r')
w = open("output_myqueue.txt", 'w')
#t = int(input())
t = int(file.readline())

for line in range(t):
    values = map(int, file.readline().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        a = queue.peek()
        w.write(str(a)+"\n")
        print(a)

