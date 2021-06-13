'''
The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your set of integers in non-decreasing order, then:

If your set contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted set ,  is the median.
If your set contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted set ,  is the median.
Given an input stream of  integers, perform the following task for each  integer:

Add the  integer to a running list of integers.
Find the median of the updated list (i.e., for the first element through the  element).
Print the updated median on a new line. The printed value must be a double-precision number scaled to  decimal place (i.e.,  format).
Example

Sorted          Median
[7]             7.0
[3, 7]          5.0
[3, 5, 7]       5.0
[2, 3, 5, 7]    4.0
Each of the median values is stored in an array and the array is returned for the main function to print.
'''

from heapq import heappop, heappush, heapify

import heapq

def addNum(num, lowers, highers):
    if not lowers or num < -lowers[0]:
        heapq.heappush(lowers,-num)
    else:
        heapq.heappush(highers,num)
    
def rebalance(lowers, highers):
    if len(lowers) - len(highers) >= 2:
        heapq.heappush(highers,-heapq.heappop(lowers))
    elif len(highers) - len(lowers) >= 2:
        heapq.heappush(lowers,-heapq.heappop(highers))

def getMedian(lowers, highers):
    if len(lowers) == len(highers):
        return (-lowers[0] + highers[0])/2
    if len(lowers) > len(highers):
        return float(-lowers[0])
    else:
        return float(highers[0])


def runningMedian(a):
    lowers = [] 
    highers = [] 
    heapify(lowers)
    heapify(highers)
    result = []
    
    for v in a:
        addNum(v, lowers, highers)
        rebalance(lowers, highers)            
        median = round(getMedian(lowers, highers),1)
        result.append(median)

    return result