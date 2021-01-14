# LRU-cache
  A cache is a high-speed data storage layer which stores a subset of data, typically transient in nature, so that future requests for that data are served up faster than is possible by accessing the data’s primary storage location. Caching allows you to efficiently reuse previously retrieved or computed data.Caching will enable you to make vastly better use of resources you already have, as well as making otherwise unattainable requirements feasible. Caches take advantage of locality of reference principle: recently requested data is likely to be requested again. 
  
 In nutshell, cache is like a short-time memory: it has limited amount of space, but is typically faster than the original data sourceand contains the most recently accessed items

LRU or Least Recently Used is one of the widely used cache eviction policies. It counts how often an item is needed and those that are least used are discarded first.

In order to implement an LRU Cache, following functionalities are required:
1. Get the key if it exists
2. Put the key
3. Delete the key when the number of keys reaches the threshold capacity of Cache.

Thinking of the data structures we can utilize - for 1 and 2 hashmap is the most efficient one and for 3 a doubly linked list would be the best option. Therefore, we can implement these functionalities with a time complexity of O(1) using a combination of two data structures.

COMPLEXITY ANALYSIS:
Time Complexity - O(1) for all functionalities.
Sapce Complexity - O(capacity)
