# g4g
<h1>Geeks for Geeks</h1>

<h2>Contents:</h2>

<h3>Searching:</h3>
<ul>
<li>LinearSearch
<li>BinarySearch
<li>InterpolationSearch (Binary)
<li>JumpSearch - (Jump + linear)
<li>FibonacciSearch
<li>ExponentialSearch - (Jump + Binary)
</ul>
<h3>Sorting:</h3>
<ul>
<li>SelectionSort - O(n^2) time and < O(n) swaps - select minimum element & put it in front (position fixed and element is found)
<li>BubbleSort - O(n^2) time and < n(n+1)/2 swaps - swap adjacent elements
<li>MergeSort - O(nLogn) time
<li>QuickSort - O(nLogn) time and more swaps - single partition and three way partition (element is fixed and position is found)
<li>InsertionSort - O(n^2) stable, in-place and online sort (left sub array is sorted and element is inserted in the sorted array )
<li>HeapSort - O(nLogn) time and O(1) space - inplace and not stable sort
<li>CountingSort - O(n+k) time and O(n+k) space -stable and non comparison sort
<li>RadixSort (CountingSort)
<li>BucketSort (InsetionSort)
<li>ShellSort (InsetionSort)
<li>TimSort (InsertionSort and MergeSort)
<li>CombSort (BubbleSort)
<li>PigeionholeSort (CountingSort)
<li>CycleSort
<li>CocktailSort (BubbleSort)
<li>StrandSort (MergeSort)
<li>BitonicSort
<li>PancakeSort
<li>BinaryInsertionSort    (BinarySearch and Insertion Sort)
<li>BogoSort / PermutationSort
<li>GnomeSort
<li>StoogeSort
<li>TreeSort
</ul>


<h3>DataStructure:</h3>
<ul>
<li>BinarySearchTree - create tree, traverse tree ((inorder, preorder, postorder) - DFS, levelorder -(BFS)), search tree, delete node
<li>Queue (list) - Enqueue, Dequeue, Qfront, Qrear
<li>Queue (collections.deque) - append, popleft
<li>Queue (queue.Queue) - maxsize, put, get, put_nowait, get_nowait, full, empty, qsize
<li>Graph - Adjacency Matrix Representation, Adjacency List Representation - addVertex, addEdge, removeVertex, removeEdge, listVertex, listEdge, printGraph, traverse graph(BFS, DFS) recursive or queue/stack impl
<li>heapq - heapify, heappush, heappop, heappushpop, heapreplace, nlargest, nsmallest
<li>Heap (PriorityQueue) - (MinHeap, MaxHeap) - insertKey, deleteKey, decreaseKey or increaseKey, extractMin or extractMax, getMin or getMax
<li>BinomialHeap - insert, merge, getMin, extractMin, deleteKey, decreaseKey
<li>FibonacciHeap - insert, consolidate, extractMin, deleteKey, decreaseKey
</ul>

<h3>Algorithm</h3>
<ul>
<li>DutchNationalFlag 
<li>Kosaraju's Algorithm - Strongly Connected Components [MotherVertex]
<li>Floyds's Warshall Algorithm - Finding the shortest path between two vertex [TransitiveClosure]
<li>Sieve Of Eratrosthenes [Prime Numbers]
<li>DijkstrasAlgorithm [Shortest Path AdjMatrix and AdjList using PriorityQueue]
<li>BellmanFordAlgorithm (Detect Negative Cycle)
<li>TopologicalSortAlgorithm - DAG topological sort using DFS
<li>JohnsonsAlgorithm - All Shortest Path in negative weighted graph O(v2LogV + VE)
<li>KahnsAlgorithm - TopologicalSort in DAG using indegree of vertex
<li>PrimsAlgorithm - Minimum Spanning Tree of the connected graph
<li>UnionFindAlgorithm - Union of disjoint Sets, find element in which disjoint set
<li>KruskalsAlgorithm - Minimum Spanning Tree of the undirected connected weighted graph using UnionFind.
<li>KMPAlgorithm - Kunth Morris Pratt (KMP) - search pattern in text in O(n) using pattern preprocessing - longest proper prefix which is suffix.
<li>RabinKarpAlgorithm - search pattern in text using hashing method O(n+m) to O(nm)
</ul>


<h3>Problem</h3>
<ul>
<li>CountNodesInTreeLevel
<li>MotherVertex in Graph
<li>TransitiveClosure of Graph (Reachability of vertex)
<li>CountPath From A to B in Graph (Reachability number and path)
<li>Minimum Vertex to traverse the entire matrix on given condition
<li>Shortest Path for 4 digit Prime number with edges each other differ by single digit
<li>Graph vertex with k cores or edges
<li>Detect directed Graph Cycles
<li>Print all Topological Sort in DAG
<li>Assign Direction to few undirected edges in DAG and remain DAG
<li>Detect is there a negative cycle in Graph
<li>Maximum edges added to DAG and it remain DAG
<li>Bipartite Graph - edges formed from two disjoint sets, only even length cycle
<li>LongestPath (maximum weight)  in DAG
<li>Longest Path (maximum weight) in undirect acyclic graph
<li>Binary Palindrome of length n with k substring repeated using dfs
<li>Find free slots from two calendar given slot duration 
<li>Median of Array Stream - InsertionSort O(n^2) and Heap(nLogn)
</ul>

<h3>Dynamic Programming</h3>
<ul>
<li>Nth Ugly Number
<li>Fibonacci Number
<li>Knapsack Problem - RecursionMethod O(2^n), TabulationMethod(BottomUp) O(n*w), MemoizationMethod(TopUp) O(n*w)
<li>Longest Common Subsequence
<li>Longest Increasing Subsequence - O(nLogn) using CeilBinarySearch , o(n^2) using DP
<li>Edit Distance of two strings
<li>Minimum absolute difference of subset sum
<li>Number of ways to cover distance
<li>Longest Path in Matrix
<li>Subset sum 
<li>Optimal Game Strategy
<li>Minimum Insertion to form Palindrome
<li>Boolean Parenthesize
</ul>