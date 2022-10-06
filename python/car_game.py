#To tell user about the various commands
print("\nRules:\n1. start- start the car\n2. stop- stop the car\n3. quit- exit the game")

comm=''

#initializing start as false so car is not moving initially
start=False

#loop
while comm.lower()!='quit':
    
    #asking user for command
    comm=input("\nCommand: ").lower()
    
    #conditions based on input
    if comm=='start':
        if not start:
            print("Started the car....")
            start=True
        else:
            print("Car is already running....")
    elif comm=='stop':
        if start:
            print("The car stopped....")
            start=False
        else:
            print("Car is already not moving....")
    elif comm!='quit':
        print("I don't understand the command....")
        
#end of loop and final print statement
else:
    print("You exited the game successfully")