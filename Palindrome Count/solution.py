from collections import defaultdict

def palinCount(string: str) -> int:
    # write your code here
    n=len(string)
    mask =0
    count = defaultdict(int)
    count[0] = 1
    ans =0
    for ch in string:
        mask^=(1<<(ord(ch)-ord('a')))
        ans +=count[mask]
        for b in range(26):
            ans += count[mask ^ (1<<b)]
        count[mask] +=1
    return ans
    pass
