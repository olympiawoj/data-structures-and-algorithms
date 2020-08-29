# Social Graph

You have been assigned the task of building a new friend-based social network. In this network, users are able to view their own friends, friends of their friends, friends of their friends' friends, and so on. People connected to you through any number of friendship connections are considered a part of your extended social network.

The functionality behind creating users and friendships has been completed already. Your job is to implement a function that shows all the friends in a user's extended social network and chain of friendships that link them. The number of connections between one user and another are called the degrees of separation.

Your client is also interested in how the performance will scale as more users join so she has asked you to implement a feature that creates large numbers of users to the network and assigns them a random distribution of friends.

## 1. Generating Users and Friendships

It will be easier to build your extended social network if you have users to test it with. `populate_graph()` takes in a number of users to create and the average number of friends each user should have and creates them.

```
>>> sg = SocialGraph()
>>> sg.populate_graph(10, 2)  # Creates 10 users with an average of 2 friends each
>>> print(sg.friendships)
{1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
>>> sg = SocialGraph()
>>> sg.populate_graph(10, 2)
>>> print(sg.friendships)
{1: {8}, 2: set(), 3: {6}, 4: {9, 5, 7}, 5: {9, 10, 4, 6}, 6: {8, 3, 5}, 7: {4}, 8: {1, 6}, 9: {10, 4, 5}, 10: {9, 5}}
```

Note that in the above example, the average number of friendships is exactly 2 but the actual number of friends per user ranges anywhere from 0 to 4.

* Hint 1: To create N random friendships, you could create a list with all possible friendship combinations, shuffle the list, then grab the first N elements from the list. You will need to `import random` to get shuffle.
* Hint 2: `add_friendship(1, 2)` is the same as `add_friendship(2, 1)`. You should avoid calling one after the other since it will do nothing but print a warning. You can avoid this by only creating friendships where user1 < user2.

## 2. Degrees of Separation

Now that you have a graph full of users and friendships, you can crawl through their social graphs. `get_all_social_paths()` takes a userID and returns a dictionary containing every user in that user's extended network along with the shortest friendship path between each.

```
>>> sg = SocialGraph()
>>> sg.populate_graph(10, 2)
>>> print(sg.friendships)
{1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
>>> connections = sg.get_all_social_paths(1)
>>> print(connections)
{1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
```
Note that in this sample, Users 3, 4 and 9 are not in User 1's extended social network.

* Hint 1: What kind of graph search guarantees you a shortest path?
* Hint 2: Instead of using a `set` to mark users as visited, you could use a `dictionary`. Similar to sets, checking if something is in a dictionary runs in O(1) time. If the visited user is the key, what would the value be?

## 3. Questions

1. To create 100 users with an average of 10 friends each, how many times would you need to call `add_friendship()`? Why?
- Call it half of that
- 500 is the correct answer
12:46 - about 46 min 

2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?
- With 1000 users and average 5 random friends each, a user will have 99% extended network coverage and an average 5 degrees of separation (`log(5000)/log(5) = 5.29`)
- Figure this out by running a test. Create 1000 thousands with an average of 5 freindshsip each popluate_graph(1000, 5). Then I'd get all social paths from user1 
- Then, what % of users will be in that particular users social network? Let's see length
- (graph) olympiawojcik social $ python solution.py 
0.987 people are in user 1's extended social network, 99% 

What is the average length of that degree of separation?
- If we print our conections, we'll get a list of every user and that path
- We want to go through EACH path and compute length of path
- (graph) olympiawojcik social $ python solution.py 
0.993
Avg length = 4.079556898288016 - 1 less than 5
- seems consistent, around 4.5ish
- Each of 1000 users is only friends with about 5 ppl so each user is only friends with 0.5% of every other user in this 1000 person network. Yet they're still connected to 99% of all other users and they're connected by around 4 degrees of separation! 


## 4. Stretch Goal

1. You might have found the results from question #2 above to be surprising. Would you expect results like this in real life? If not, what are some ways you could improve your friendship distribution model for more realistic results?
- This is a pretty decent model of how friendship distributions might work out and how it might affect our social graph, but why is this not realistic? Why is it unrealistic to have a completely random friendship distribution? BC our freinds aren't random, they tend to know each other, there's clustering. 

2. If you followed the hints for part 1, your `populate_graph()` will run in O(n^2) time. Refactor your code to run in O(n) time. Are there any tradeoffs that come with this implementation?

- n^2 comes from when we generate every single possible friendships
shuffle is O^N but also O(n^2)
- the O(n) solution risks longer (or infinite) runtime when number of friendships and number of users are close (due to friendship collisions)



### What are the inputs, outputs, and variables?
- **Inputs:** 2
    - Number of users to create
    - Average number of friends each user should have
- **Output:**  
    - An object of 10 friendships. Keys are 1-10 (the users) and the values are the friend's user ids
- **Functions:**
    - Social Graph Class 
        - `add_friendship` creates a bi-directional edge/friendship (user1 points to user2 and user2 points to user1) --> GIVEN
        - `add_user` to add a node --> GIVEN
        - `populate_graph` takes # of users and avg number of friendships as arguments, creates random users
- **Variables:**


### Three Steps for solving ANY graph problem
1. Translate the problem into graph terminology
    - What are the nodes? Users
    - What are the edges? Bidirectional friendships between users 
    - Is it directed or undirected? Undirected becauses friendships are bidirectional 
    - Is it cyclical or acyclical? Cyclical because could go from Olympia -> Megan -> Court -> Olympia
    - Is it weighted or unweighted?  Unweighted because there are no values in the edges
    - Dense or Sparse, ratio of edges to modes? 
2. Build your graph 
3. Traverse your graph - using DFS or BFS
 

 1. Create graph `sg = SocialGraph()`
 2. Call `populate_graph(num_users, avg_friendships)`
    - Average means take  total number of friendships and divide by number of users we have
    - 10 users with an average of 2 friendships each means we should have 20 total friendships

## Step 1: Generating Users & Friendships 
### populate_graph Algorithm 
Goal: Takes a number of users and an average number of friendships as arguments.
- Creates that number of users and a randomly distributed friendships between those users.
- The number of users must be greater than the average number of friendships.

1. Reset Graph
2. Write a for loop that calls `add_user` the right amount of times
    - `for i in range(num_users) `
    - Add users via `self.add_user(f"User {self.last_id+1}")`

3. Create possible  friendships
    - To create N random friendships, you could create a list with all possible friendship combinations, shuffle the list, then graph the first N elements from the list
        - We'll need `possible_friendships = []` - an empty array 
    1 2
    1 3
    1 4
    1 5
    1 6
    1 7
    1 8
    1 9
    1 10
    2 3
    2 4
    2 5
    2 6...
    8 9
    8 10
    9 10  

    - Then let's use a for loop `for user_id in self.users`: iterating through each user and matching them up with EVERY `user_id` that's larger than their current id
        - Since we need the id of the firend larger than current user_id, we do another for loop `for friend_id in range(user_id + 1, self.last_id + 1)`. If current user_id is 4 we want to look at friend 5.
        - Append the friendship of user_id and friend_id `possible_friendships.append((user_id, friend_id))`
            - This is a classic for in a for loop. In our first loop, we're going through `n`, but in our second loop, we're not always going through them (n/2).The time complexity of this operation is: n * (n/2) or  On^2 
            - Possible friendships for 10 users and 2 average friendships: [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 7), (6, 8), (6, 9), (6, 10), (7, 8), (7, 9), (7, 10), (8, 9), (8, 10), (9, 10)]
            - This is okay for 10 users, but how do we optimize for 1 billion users?
4. Shuffle the possible friendships using the random module - `random.shuffle(possible_friendships)`
    - `random` is a built-in Python module that you can use to make random numbers 
    - `shuffle(list_name)` shuffle's a list (reorganize the order of the list items)
5. To create `n` friendships where `n = avg_friendships * num_users // 2`, loop trough the range `for in in range(num_users * avg_friendships //2)` - this slices off the first 10 from the possible_friends list
    - `avg_friendships = total_friendships / num_users`
    - `total_friendships = avg_friendships * num_users`
    - The `//2` comes from every time we're creating a friendship, we're actually creating two friendships & `//` is to get an integer

6. For each of the 10 random possible friendships, get the `friendship = possible_friendships[i]` and then create the friendship `self.add_friendship(friendship[0], friendship[1])`

**Testing**
- Should print Friendships of 10 users with 20 total friendships, each a different number of friendships. 10 users with an average of 2 friendships each.
- Let's us do scale testing. We can also test this for larger numbers - 100 users with an average of 2 friendships each. Assume we have 200 friendships. Nice thing about random distributino is we get some users with a lot of friends i.e. 6 friends. Large random sets will push you to test your edge cases.
- 100 80 is a dense graph we can test this on. 
```python
import pprint
sg = SocialGraph()
sg.populate_graph(10, 2)
print(f"Friendships: \n{pprint.pformat(sg.friendships)}")
```

## Step 2: Degrees of Separation
### get_all_social_paths Algorithm 
- Now that you have a graph full of users and friendships, you can crawl through their social graphs. 
- **Goal:** Takes a userID as an argument 
- Returns a dictionary containing every user in that user's extended network along with the shortest friendship path between each
- The key is the friend's ID and the value is the path 
- Shortest path is a KEYWORD that says you MUST USE BFT & BFS. We're doing a traversal, but we're also storing the shortest path. 


### BFS Algorithm 
1. Create a queue
2. Enqueue a _path_ to the start `user_id`
3. Create a dictionary to store visited vertices
    - Note: Why use a dict over a set?
4. Use `while` to loop until the queue is empty. While the  queue is not empty:
    - Dequeue/remove the first PATH from the queue
    - Grab the node from the end of the path
    - Check if that node has NOT been visited by seeing if it's in our `visited` dict
    - If it hasn't been visited, add it to the visited dictionary along with the path (because dequeue will be PATH from starting user to w/e user we're currently looking at)- `visited[current_id] = path`
5. Use a `for` loop to loop through every friend_id in a current user's friendship and enqueue a path to each friend 
    - Copy the path `path_copy = path.copy()`
    - Append each neighbor `path_copy.append(friend_id)`
    - Enqueue the path_copy `q.enqueue(path_copy)`
6. Return `visited` dict after all loops are complete

