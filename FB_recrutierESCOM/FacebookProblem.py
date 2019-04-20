def executeCoolDown(cooldown):
  for i in range(cooldown):
    print "_ "

def executeTask(task):
    print task+" "

def iDontKnowTheNameOfTheProblem(task, cooldown):
  #O(n*k) n -> task.lenght and k -> # diferent tasks
  #hashtable = {task : number of tasks executed after the last time I executed this task}
  hashtable = {}
  count = 0

  for element in task:    
    #Auxiliar variable, just save the number of elements(task+cooldown) that I put in this iteration
    res = 0

    #If element is in hashtable, it means that the value of that key is the number of elements(task+cooldown) executed after the last execution
    if element in hashtable:
      
      #get number of elements executed after the last execution of this task
      a = hashtable[element]  

      #if there is more elements that the cooldown, no is necessary insert cooldowns
      if a >= cooldown:
        count += 1
      #if there is less elements that the cooldown, i need to put as cooldowns possible to respect original cooldown
      else:
        res = cooldown - a
        #adding one because of the execution of the task
        res += 1
        #executing task and cooldowns
        count += res
    
    #if element is not in hashtable, it means that this is the first time the task is executed
    else:
      #Execute the task
      count += 1
      #The number of elements I put is 1 because I only execute 1 task
      res = 1

    #Traversal the hastable adding the number of elements I put this iteration  
    for key in hashtable:
      hashtable[key] += res
    #set element value in zero, because this is the last task I've executed, so there is no other task after 
    hashtable[element] = 0

  return count

#task = ['A', 'A', 'B', 'A', 'A']
#task = ['A', 'A', 'B', 'A']
#task = ['A', 'B', 'C', 'D', 'E', 'F', 'A', 'F']
task = ['A', 'B', 'C', 'B', 'A', 'F', 'E', 'F']
cooldown = 6

count = iDontKnowTheNameOfTheProblem(task, cooldown)
print count