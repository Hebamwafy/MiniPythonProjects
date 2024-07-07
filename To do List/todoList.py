todo_List=[]
user_action=str
while(user_action!="exit"):
    user_action =input("Enter your choice : (add , view , remove , exit) : ")
    choice=input("you selected "+user_action+" do you want to change your choice?")
    if (choice=="yes"):
        continue
    if (user_action== "add"):
        task_name=input("Enter the task name: ")
        todo_List.append(task_name)
        for task in todo_List:
                print (task)
        print("task added successfully!")
    elif (user_action=="view"):
        if not todo_List:
            print ("no tasks to view")
            
        else:
            for task in todo_List:
                print (task)
    elif (user_action=="remove"):
        if not todo_List:
            print ("no tasks to remove!") 
        else:
            rm_task=input("Enter the task name you want to remove: ")
            todo_List.remove(rm_task)
            print("removed successfully!")
    elif(user_action=="exit"):
        print ("see you soon!!")
        exit
    else:
        print ("invalid choice!")
