#leecode training camp.  #47 
#https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/   find the median fo two sorted arrays
#idea from https://zhuanlan.zhihu.com/p/39129143 
#bugs  when A = [1,2,2] B = [1,2,3], can't passs

class Solution(object):
    """docstring for solution
        from the middle of A and B, moves both arrays and finds the crossing area
    """
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if m < 0 or n < 0:
            return print("error arguments")
        #make sure m <= n
        if m > n:
            m,n,A,B = n,m,B,A

        imin, imax = 0, m 
        jmin, jmax = 0, n
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = (jmin + jmax) // 2  
            #situation1  A-right is smaller than B-left, A-right moves forward right,
            #or B-left moves forward left (j changes with i)
            if(i < m and A[i] < B[j - 1]):
                imin += 1
                jmax -= 1
            #situation2  A-left is bigger than B-right, A-left moves forward left, 
            #or B-right moves forward right (j changes with i)
            elif(i > 0 and A[i - 1] > B[j]):
                imax -= 1
                jmin += 1
            #situation3  cross
            else:
                if i == 0:
                    leftOfMedian = B[j - 1]
                elif j == 0:
                    leftOfMedian = A[i - 1]
                else:
                    leftOfMedian = max(A[i - 1], B[j - 1]) 

                if i == m:
                    rightOfMedian = B[j]
                elif j == n:
                    rightOfMedian = A[i]
                else:
                    rightOfMedian = min(A[i], B[j])

                if (m + n) % 2 == 1:
                    return rightOfMedian
                else:
                    return (leftOfMedian + rightOfMedian) / 2.0

s = Solution()
A = [2,4,6]
B = [5,8]
median = s.findMedianSortedArrays(A,B)
print(median)

        