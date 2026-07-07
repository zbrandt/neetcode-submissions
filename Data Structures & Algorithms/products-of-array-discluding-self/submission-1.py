class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # works but redundant
        def prefix_prod(x):
            if len(x) == 1:
                return x

            # create pairs x_0 * x_1, x_2 * x_3, ...
            pairs = []
            for i in range(0, len(x) - 1, 2):
                pairs.append(x[i] * x[i + 1])

            # recursively apply prefix sum on the pairs
            z = prefix_prod(pairs)

            # reconstruct prefix sums x_0, z_0, z_0 * x_2, z_1, z_1 * x_4, ... 
            y = [x[0]]
            for i in range(1, len(x)):
                if i % 2 == 1:
                    y.append(z[i // 2])
                else:
                    y.append(z[(i // 2) - 1] * x[i])
            
            return y
        
        # prefix = prefix_prod(nums)
        # suffix = list(reversed(prefix_prod(list(reversed(nums)))))

        # output = []
        # for i in range(len(nums)):
        #     if i == 0:
        #         output.append(suffix[i + 1])
        #     elif i == len(nums) - 1:
        #         output.append(prefix[i - 1])
        #     else:
        #         output.append(prefix[i - 1] * suffix[i + 1])
        
        n = len(nums)
        prefix = [0] * n   # prefix[i] = product of all nums left of i
        suffix = [0] * n   # suffix[i] = product of all nums right of i
        output = [0] * n   # output[i] = prefix[i] * suffix[i] 

        prefix[0] = suffix[n - 1] = 1
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        for i in range(n):
            output[i] = prefix[i] * suffix[i]

        return output
            