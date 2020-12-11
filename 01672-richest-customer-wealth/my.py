class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(lambda account: sum(account), accounts))
