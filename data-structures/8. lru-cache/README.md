# LRU (Least-Recently-Used) Cache

## Bloomberg Question
Web browser design:
Design and implement a web browser which supports the functionality that at any given instance you can efficiently tell the top 5 visited websites on basis of number of visits. This question was a variant of LRU cache and it can be optimally implemented using a map and doubly linked list. See below for design template:


## What's the goal?
- Implement an LRU cache using a hash table and DLL

## Terminology

#### Caches
- **Caches**- Cache is memory that can speed up access to frequently used information  by keeping copies of data in a fast, local store
- **Cache Hit**- When the data you want IS in the cach already (Hit a homem run! Win!)
- **Cache Miss**- When you have to go to primary storage to get the data

#### LRU
- **LRU Cache**- Caches are limited in size compared to primary storage so an LRU cache _discards_ the _least-recently-used_ item in the cache when it's full

#### Building an LRU Cache
- Need a **hash table** to quickly look up cache entries by key (e.g. lookup key "A", we get access to the entry)
- Need cache entries in a **doubly-linked list** ordered from _most-recently used_ (head) to _least-recently used_ (tail). 
    -  Makes it easy to remove them from the head and tail - O(1) for both



## Putting Entries in a Cache
1. Allocate a new entry
2. Move to the head of the list - next entry will move over to the head of the list
3. Add hash table entry- hookup next and previous pointers as appropriate

## Getting Entries from a Cache
1. Move the accessed element to the _head_ of the list (MRU - most recently used)
2. Return a pointer to that entry


## Deleting from the LRU Cache 
- Let's say the cache is full at this point. Too many items in cache and we want to discard the _least-recently used_ item 
1. If the cache is overfull, simply delete the _tail_ entry from BOTH the DLL and from the hash table


## Challenge
- What are some applications of LRU caches?
- How would you add functinoality to the cache (in psuedocode) to remove entries that are older than a cutoff age from the cache? O(n) time is OK
- How would you remove entries as above in O(1) time?



## LRU Cache
An LRU (Least Recently Used) cache is an in-memory storage structure that adheres to the Least Recently Used caching strategy.

In essence, you can think of an LRU cache as a data structure that keeps track of the order in which elements (which take the form of key-value pairs) it holds are added and updated. The cache also has a max number of entries it can hold. This is important because once the cache is holding the max number of entries, if a new entry is to be inserted, another pre-existing entry needs to be evicted from the cache. Because the cache is using a least-recently used strategy, the oldest entry (the one that was added/updated the longest time ago) is removed to make space for the new entry.

So what operations will we need on our cache? We'll certainly need some sort of set operation to add key-value pairs to the cache. Newly-set pairs will get moved up the priority order such that every other pair in the cache is now one spot lower in the priority order that the cache maintains. The lowest-priority pair will get removed from the cache if the cache is already at its maximal capacity. Additionally, in the case that the key already exists in the cache, we simply want to overwrite the old value associated with the key with the newly-specified value.

We'll also need a get operation that fetches a value given a key. When a key-value pair is fetched from the cache, we'll go through the same priority-increase dance that also happens when a new pair is added to the cache.

Note that the only way for entries to be removed from the cache is when one needs to be evicted to make room for a new one. Thus, there is no explicit remove method.

Given the above spec, try to get a working implementation that passes the tests. What data structure(s) might be good candidates with which to build our cache on top of? Hint: Since our cache is going to be storing key-value pairs, we might want to use a structure that is adept at handling those.

Once you've gotten the tests passing, it's time to analyze the runtime complexity of your get and set operations. There's a way to get both operations down to sub-linear time. In fact, we can get them each down to constant time by picking the right data structures to use.

Here are you some things to think about with regards to optimizing your implementation: If you opted to use a dictionary to work with key-value pairs, we know that dictionaries give us constant access time, which is great. It's cheap and efficient to fetch pairs. A problem arises though from the fact that dictionaries don't have any way of remembering the order in which key-value pairs are added. But we definitely need something to remember the order in which pairs are added. Can you think of some ways to get around this constraint?