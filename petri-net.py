# Get the number of places from the user
num_of_places = input('Enter number of places: ')
places = []
for i in range(int(num_of_places)):
    # Get the places's names
    print('Enter place #',(i+1),': ',end='')
    pname = input()
    places.append(pname)

# Get the number of transitions  from the user
num_of_trans = input('Enter the number of transitions: ')
trans = []
for i in range(int(num_of_trans)):
    # Get the trans's names
    print('Enter transition #',(i+1),': ',end='')
    tname = input()
    trans.append(tname)

num_of_flows = input('Enter number of flows: ') # For ex: 4
flows = []
for i in range(int(num_of_flows)):
    print('Enter pair #',(i+1),' (Place): ',end='')
    pplace = input()
    while pplace not in places:
        print('Sorry, Place is not found, Try again!')
        print('Enter pair #',(i+1),' (Place): ',end='')
        pplace = input()
    print('Enter pair #',(i+1),' (Transition): ',end='')
    ptrans = input()
    while ptrans not in trans:
        print('Sorry, Transition is not found, Try again!')
        print('Enter pair #',(i+1),' (Transition): ',end='')
        ptrans = input()
    flows.append([pplace,ptrans])

initial_marking = []
for i in range(int(num_of_places)):
    print('Enter the initial marking pair, Like this -> (1,0,0): ',end='')
    im = input()
    initial_marking.append(int(im))

print(initial_marking)

# Starting execution
index = 0
for i in range(int(num_of_places)):
    if(initial_marking[i] == 1):
        index = i
        break

print('Starting execution with =>',places[index])
