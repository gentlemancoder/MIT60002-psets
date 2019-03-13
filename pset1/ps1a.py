###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cowdict = {}
    with open(filename, 'r') as cowfile: # with used for memory optimization
        for line in cowfile:
            line = line.rstrip()
            if not (len(line) == 0 or line.startswith('//')):
                cowinfo = line.split(',')
                cowdict[cowinfo[0]] = int(cowinfo[1])
        cowfile.close()

    return cowdict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
   
    cowscopy = sorted(cows, key=cows.get) # only returns list of names
    
    trip_weight = 0
    trip_list = []
    total_trips = []
    already_gone = []
    
    while len(already_gone) < len(cowscopy):
        for cow in cowscopy:
            if cow not in already_gone:
                cow_weight = cows[cow]
                if cow_weight + trip_weight < limit:
                    trip_weight += cow_weight
                    trip_list.append(cow)
                    already_gone.append(cow)
                else:
                    total_trips.append(trip_list)
                    trip_list = []
                    trip_weight = 0
                    break
    total_trips.append(trip_list)
    return total_trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowscopy = sorted(cows, key=cows.get)
    possible_trips = []
#                if partition not in possible_trips: #parts_dict[total_weight]:
#                    parts_dict[total_weight].append(partition) # sorts each trip by weight
#                    possible_trips.append(partition) 
#        
#    parts_dict = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
    
    
    for parts in get_partitions(cowscopy):
        valid = True # flag to eliminate partition with invalid trip
        for partition in parts:
            total_weight = 0
            for cow in partition:
                total_weight += cows[cow]                
            if total_weight > limit:
                valid = False
                break # There is no need to cycle after one trip is invalid
        if valid:
            possible_trips.append(parts)
            
    
    return min(possible_trips, key=len) # selects shortest list from possible trips


#    This code works beautifully:

#    def weight(sub):
#        sum = 0
#        for e in sub:
#            sum += cows[e]
#        return sum
#
#    valid_trips = []
#    for part in list(get_partitions(cows)):
#        if all(weight(sub) <= limit for sub in part):
#            valid_trips.append(part)
#    print(valid_trips)
#    return min(valid_trips, key=len)
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    greedy_result = greedy_cow_transport(cows)
    end = time.time()
    print("Greedy alogrithm result:", greedy_result)
    print("Greedy number of trips:", len(greedy_result))
    print("Greedy execution time:", end - start)
    
    start = time.time()
    brute_result = brute_force_cow_transport(cows)
    end = time.time()
    print("Brute force result:", brute_result)
    print("Brute number of trips:", len(brute_result))
    print("Brute execution time:", end - start)
    

if __name__ == '__main__':
    cows = load_cows('ps1_cow_data.txt')
    compare_cow_transport_algorithms()