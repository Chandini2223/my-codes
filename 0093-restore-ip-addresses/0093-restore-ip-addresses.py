class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def backtrack(start, parts, path):
            if parts == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
            if start >= len(s):
                return

            for l in range(1, 4):
                if start + l > len(s):
                    break
                part = s[start:start + l]
                if (part.startswith('0') and l > 1) or int(part) > 255:
                    continue
                backtrack(start + l, parts + 1, path + [part])

        backtrack(0, 0, [])
        return res
