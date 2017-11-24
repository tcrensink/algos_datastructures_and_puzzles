#naive algo ideas in this file.  Come back to these when you know what exists already.

# Simple n log(n): 
# array is seprated into subarrays, sorted, unsorted.  Choose the next unosorted element; to find it's place in the sorted sub array, compare with the value of element at the bisection to narrow down it's place.

# as you sort an array, guess the index of the next element based on the sorted histogram and "gradient descent"/bisect to its correct location.  

# How does sorting EV compare if you have inequal bisections?  E.g., random bisection comparison point?

# Algo idea 1:
# guess index of elements by linearly interpolating between min and max values.  Use this to "pre-sort" your array
# improvement: infer distribution by calculating moments as you do linear scan, then place elements accordingly/probabilistically

# Algo idea 2:
# don't sort by pairwise comparisons; use stochastic algorithm to "shake" the array into sorted order, moving many elements in each timestep.

# Algo idea 3:
# a simple improvement on insertion sort to make it O(nlogn): do sequential bisections (not linear scan) through sorted sub-array to place element.

# Presort according to length in some base.  You now have m bins of length in some new base b, but it costs ~O(log(d)) to make that conversion, where d is the number of digits

