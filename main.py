class Solution:
    def subarray(self, arr, target):
        # code here
        n = len(arr)
        for i in range(n):
            current_sum = 0
            for j in range(i,n):
                current_sum = current_sum + arr[j]
            if current_sum == target :
                print(f"[{i},{j}]")
sol1 = Solution()
sol1.subarray([12, 18, 5, 11, 30, 5], 69)