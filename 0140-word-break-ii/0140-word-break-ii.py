class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            res = []
            if start == len(s):
                return [""]

            for word in wordSet:
                if s.startswith(word, start):
                    sub_sentences = dfs(start + len(word))
                    for sub in sub_sentences:
                        if sub == "":
                            res.append(word)
                        else:
                            res.append(word + " " + sub)

            memo[start] = res
            return res

        return dfs(0)
