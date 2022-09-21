largest = None
smallest = None

# Initialize loop control variavle and other variable outside the loop
# (before entering the loop) to get the max and min numbers game properly started.

# The cleanInput variable is used to skip to the end of the loop
# (but not break out of the loop). It is initialized to True and
# will become False when an input exception is caught
cleanInput = True

# num is our loop control variable. Loop control variables must be initialized,
# checked, and changed. The first prompt for a number from the user is made outside
# the loop to properly initialize the loop control variable named num
# This variable is also used to store the input integer
num = input("Enter a number (done to stop): ")

# Both largest and smallest are assigned the value of num. They now have a value
# other than their initialized value of None.
largest = num;
smallest = num;

# This loop will run until a break statement.
while True:
    # reset cleanInput to true so we can properly restart the input process
    cleanInput = True
    if (num == "done"):
        break
    try:
        (isinstance(int(num),int))
    except:
        print("Invalid input")
        # Do not break here -- just note an invalid input action and move to the end of the loop
        # using the cleanInput flag.
        cleanInput = False

    if (cleanInput):
        num = int(num)
        # print(num)
        if (int(num) > int(largest)):
            largest = num
        if (int(num) < int(smallest)):
            smallest = num

    # We are at the end of the loop and this is where we change the loop control variable!
    num = input("Enter a number: ")

# We broke out of our loop because the user input "done" and we need to output the max and min numbers!
print("Largest number is ", largest)
print("Smallest number is ", smallest)