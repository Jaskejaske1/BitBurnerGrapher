"""
Algorithmic Stock Trader IV
You are attempting to solve a Coding Contract. You have 10 tries remaining, after which the contract will self-destruct.


You are given the following array with two elements:

[5, [185,160,46,34,4,75,196,164,46]]

The first element is an integer k. The second element is an array of stock prices (which are numbers) where the i-th element represents the stock price on day i.

Determine the maximum possible profit you can earn using at most k transactions. A transaction is defined as buying and then selling one share of the stock. Note that you cannot engage in multiple transactions at once. In other words, you must sell the stock before you can buy it again.

If no profit can be made, then the answer should be 0.


If your solution is an empty string, you must leave the text box empty. Do not use "", '', or ``.
"""

def maxProfit(k: int, prices: list[int]) -> int:
    if not prices or k <= 0:
        return 0

    n = len(prices)
    if k >= n // 2:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

    dp = [[0] * n for _ in range(k + 1)]

    for i in range(1, k + 1):
        max_diff = -prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
            max_diff = max(max_diff, dp[i - 1][j] - prices[j])

    return dp[k][n - 1]

# Example usage
if __name__ == "__main__":
    k = 5
    prices = [185, 160, 46, 34, 4, 75, 196, 164, 46]
    result = maxProfit(k, prices)
    print(f"The maximum possible profit is: {result}")