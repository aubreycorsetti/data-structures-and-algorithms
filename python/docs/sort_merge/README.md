# Merge Sort
 Create a blog post explaining merge sort

## Blog

When it comes to sorting large datasets, one of the most efficient algorithms to use is Merge Sort. This divide and conquer algorithm breaks down an array into smaller sub-arrays, sorts each one, and then merges them back together in a specific order. In this post, we will walk through the steps of implementing Merge Sort in Python.

The first step in Merge Sort is to divide the input array in half. This can be done by finding the middle element and then splitting the array into two parts - one from the start to the middle, and the other from the middle to the end. Next, we'll recursively sort each sub-array by calling the merge sort function on them. This continues until we have individual elements in each sub-array, at which point they are considered to be sorted.

Now that all the sub-arrays are sorted, we can start merging them back together. We'll create a new array to hold the merged elements and compare the first element of each sub-array. The smallest element will be added to the new array and removed from its sub-array. This process continues until one of the sub-arrays is empty.

Finally, the new array containing all the elements in sorted order is returned as the final output. The implementation of merge sort in python can be done using loops and recursion. It is important to understand the concept of divide and conquer and how to merge the sub-arrays in a specific order.

Merge Sort is a popular and efficient algorithm that is widely used in many applications. Its divide and conquer approach makes it well-suited for sorting large arrays and lists. With the step by step implementation in python, it will be easy to sort large dataset and bring the data in desired format.
