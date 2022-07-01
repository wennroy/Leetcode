# 繁琐步骤
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def isPrime(n):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False

            return True

        count_prime = 0
        for i in range(2, n + 1):
            if isPrime(i):
                count_prime += 1

        if count_prime != 0:
            prime_res = 1
            non_prime_res = 1
            for i in range(2, count_prime + 1):
                prime_res *= i
            for i in range(2, n - count_prime + 1):
                non_prime_res *= i
            return (prime_res * non_prime_res) % (10 ** 9 + 7)
        else:
            return 1


# 标准答案
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        numPrimes = sum(self.isPrime(i) for i in range(1, n + 1))
        return self.factorial(numPrimes) * self.factorial(n - numPrimes) % (10 ** 9 + 7)

    def isPrime(self, n: int) -> int:
        if n == 1:
            return 0
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return 0
        return 1

    def factorial(self, n: int) -> int:
        res = 1
        for i in range(1, n + 1):
            res *= i
            res %= (10 ** 9 + 7)
        return res
'''
一个小细节，标答在函数中就多次对10**9+7取模，这说明对10 **9 +7取模不会影响最后的结果，而且可以省空间。

A few distributive properties of modulo are as follows:
1. ( a + b ) % c = ( ( a % c ) + ( b % c ) ) % c
2. ( a * b ) % c = ( ( a % c ) * ( b % c ) ) % c
3. ( a – b ) % c = ( ( a % c ) - ( b % c ) ) % c ( see notes at bottom )
4. ( a / b ) % c NOT EQUAL TO ( ( a % c ) / ( b % c ) ) % c
So, modulo is distributive over +, * and - but not / .

Credit from: https://www.hackerearth.com/practice/notes/abhinav92003/why-output-the-answer-modulo-109-7/

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/prime-arrangements/solution/zhi-shu-pai-lie-by-leetcode-solution-i6g1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''