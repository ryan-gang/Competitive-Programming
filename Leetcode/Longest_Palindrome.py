from collections import Counter


class Solution:
    # Runtime: 78 ms, faster than 5.96% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 22.54% of Python3 online submissions.
    # T : O(NLogN), S : O(N)
    # Not at all optimal, but very easy to understand elegant code.
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        even = [d[i] for i in d if not d[i] % 2]
        odd = [d[i] for i in d if d[i] % 2]
        odd.sort()
        max_odd = odd.pop() if odd else 0
        return sum(even) + max_odd + sum(odd) - len(odd)

    # Runtime: 61 ms, faster than 34.76% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 22.54% of Python3 online submissions.
    # T : O(N), S : O(1) (Theoretically only 26 x 2 keys are possible.)
    def longestPalindrome2(self, s: str) -> int:
        d, length, flag = Counter(s), 0, False
        for key in d:
            length += d[key]
            if d[key] % 2:
                # If the "value" of this char is odd, we won't be able to accommodate all the
                # instances of this char, in our palindrome. But we can accommodate value - 1
                # instances. (Which is even)
                # If the "value" is even, we can accommodate all the instances.
                flag = True
                length -= 1
        # But for one character with an odd number of instances we will be able to accommodate all
        # of its instances, we had previously added val - 1 times it, here we are adding the last
        # one. Ideally this would be done to the char with the max number of instances.
        # (This will go in the middle.)
        length += int(flag)

        return length


sol = Solution()
assert sol.longestPalindrome2(s="abccccdd") == 7
assert sol.longestPalindrome2(s="a") == 1
assert sol.longestPalindrome2(s="bb") == 2
assert (
    sol.longestPalindrome2(
        s="""civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"""
    )
    == 983
)
