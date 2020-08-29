import random 
from util import Stack, Queue  # These may come in handy
import pprint

'''

'''

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    ##  IMPLEMENT THIS!!!
    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        #1, 2, 3  - TAKE ALL possible user friendship combinatinos (1, 2) (1, 2) (2, 3) - all possible friendship combos. Not no (2, 1) (3, 1)(3, 2 ) bc user 1 being friends with user 2 is same as user 2 being friends with user 1
        #when we call create freindship, we're creating TWO friendships

        # Add users
        # Write a for loop that calls create user the right amount of times 
        for i in range(num_users):
            #Creates 10 users - we have an empty adjacency list with users --> ex: {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set(), 10: set()}
            self.add_user(f"User {i +1}")

        # Create friendships
        # To create N random friendships
        # you could create a list with all possible friendship combos
        possible_friendships = []
        for user_id in self.users: 
            for friend_id in range(user_id+1,self.last_id +1): #if user 4, only care abt 5 6 7
                possible_friendships.append((user_id, friend_id))
        print(possible_friendships)

        random.shuffle(possible_friendships)
        print(possible_friendships)

        #slice off first 10 from list, creating N friendships where n=average_friendships * num_users // 2 --> how did we get this? we know that
        #average_friendships = total_friendships / num_users
        #to solve for total_friendships = average_friendships * num_users
        #divided by 2 bc every time we create a friendships we're actually creating 2 friendships so we need to divde by 2
        
        for i in range(num_users * avg_friendships // 2):
            #get an int
            friendship = possible_friendships[i]
            print('here is a friendship', friendship, 'i', i)
            #create friendship
            self.add_friendship(friendship[0], friendship[1])

        #10 users, 20 total friendships, 10 users with friendships each w diff len of friends
    
    def populate_linear_graph(self, num_users, avg_friendships):
        #Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        #Add users
        #Write a for loop that calls create user the right amount
        target_friendships = num_users * avg_friendships 
        total_friendshios = 0
        # Pick a random user
        while total_friendships < target_friendships:
        # Pick another random user
            user_id = random.randint()
        # Try to create the friendship
        # If it works, increment a counter
        # If not, try again



    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        #Create a queue
        q = Queue()
        #Enqueue a path to the start user_id
        q.enqueue([user_id])
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        
        #While the queue is not empty...
        while q.size() > 0:
            #Dequeue the first path
            path = q.dequeue()
            #Grab the last id from the path 
            current_id = path[-1]
            #Check if it's been visited
            #If not...
            #IN for dictionary checks the KEY not the value
            if current_id not in visited: 
                # Add it to visited along with the path (bc dequeue will be PATH from starting user to w/e user we/re currently looking at)
                visited[current_id] = path
                # Enqueue the path to each friend to the queue
                for friend_id in self.friendships[current_id]: #gives us our friends
                    #Copy the path
                    path_copy = path.copy()
                    #Append each neighbor
                    path_copy.append(friend_id)
                    #Enqueue
                    q.enqueue(path_copy)

     
        return visited
        #BFT combined with BFS - we're doing a traversal and also storing the path. when we get to user 8, we can add path from user 1 to 8. etc etc. 


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 2)
    # print('friendships', sg.friendships)
    print(f"Friendships: \n{pprint.pformat(sg.friendships)}")
    connections = sg.get_all_social_paths(1)
    # print('connections', connections)
    # print(f"Connections: \n{pprint.pformat(connections)}")
    print(len(connections)/1000)
    total = 0
    for path in connections.values():
        total += len(path)
    print(f'Avg length = {total / len(connections) -1}')


# >>> sg = SocialGraph()
# >>> sg.populate_graph(10, 2)
# >>> print(sg.friendships)
# {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
# >>> connections = sg.get_all_social_paths(1)
# >>> print(connections)
# # {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]} 
#1, 9, 2, 6, 8, 3, 6, 10, 4, 4 9  
#key --> every user in that user's extended network, [] array is the PATH between them 
#Takes a user's user_id as an argument
#         Returns a dictionary containing every user in that user's
#         extended network with the shortest friendship path between them.

#         The key is the friend's ID and the value is the path.