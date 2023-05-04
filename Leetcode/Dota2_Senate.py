from collections import deque


class Solution:
    # Runtime: 120 ms, faster than 18.96%.
    # Memory Usage: 16.4 MB, less than 15.60%.
    # T : O(N), S : O(N)
    # Total votes possible is N. So we iterate over our main loop N times max.
    # More ways to solve it here : https://leetcode.com/problems/dota2-senate/editorial/
    def predictPartyVictory(self, senate: str) -> str:
        """
        For every senator, we first add them to our stack, if there already
        exists opponent senators, our current senator will be banned. So we pop
        off once, emulating a ban, and pop off again, and then push it to our
        queue. The prev senator is eligible to vote again, this is an emulation
        of that. And to not add or remove to the string, we convert it into a
        stack, and keep pushing new entries to the back. So the last one in the
        queue is actually the winner.
        """
        stack: deque[str] = deque()
        queue = deque(senate)  # Vote from left to right.

        banned = idx = 0
        n = len(senate)
        while banned < n - 1 and idx < len(queue):
            stack.append(queue[idx])  # Add curr senator for voting.
            while len(stack) > 1 and stack[-1] != stack[-2]:  # If opponent senator already present
                stack.pop()  # Current senator is banned.
                queue.append(stack.pop())  # Prev one is added back to queue for voting again.
                banned += 1
            idx += 1

        d = {"R": "Radiant", "D": "Dire"}

        return d[queue[-1]]

    # LC 5.
    def predictPartyVictory1(self, senate: str) -> str:
        # Eligible Senators of each party
        r_count = senate.count("R")
        d_count = len(senate) - r_count

        # Floating Ban Count
        d_floating_ban = 0
        r_floating_ban = 0

        # Queue of Senators
        q = deque(senate)

        # While any party has eligible Senators
        while r_count and d_count:
            # Pop the senator with turn
            curr = q.popleft()

            # If eligible, float the ban on the other party, enqueue again.
            # If not, decrement the floating ban and count of the party.
            if curr == "D":
                if d_floating_ban:
                    d_floating_ban -= 1
                    d_count -= 1
                else:
                    r_floating_ban += 1
                    q.append("D")
            else:
                if r_floating_ban:
                    r_floating_ban -= 1
                    r_count -= 1
                else:
                    d_floating_ban += 1
                    q.append("R")

        # Return the party with eligible Senators
        return "Radiant" if r_count else "Dire"


if __name__ == "__main__":
    sol = Solution()
    assert (sol.predictPartyVictory(senate="RDRDD")) == "Radiant"
    assert (sol.predictPartyVictory(senate="RDD")) == "Dire"
    assert (sol.predictPartyVictory(senate="RD")) == "Radiant"
    assert (sol.predictPartyVictory(senate="RRR")) == "Radiant"
    assert (sol.predictPartyVictory(senate="DDR")) == "Dire"
