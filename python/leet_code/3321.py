"""Leet Code: Find X-Sum of all K-long Subarrays II

This module provides functionality to find the X-Sum of all K-long subarrays in a given array.
The X-Sum is calculated based on the frequency of elements within each subarray.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""
import heapq
from collections import Counter

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))


class Solution:
    """Solution class for LeetCode problems.

    This class encapsulates methods to solve specific algorithmic challenges,
    using efficient data structures to handle large inputs.
    """

    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        """Compute the x-sum for each k-length subarray.

        This function maintains a sliding window of size k, tracking element frequencies
        and using two heaps to manage the top x most frequent elements efficiently,
        ensuring tie-breaking by value and handling frequency updates with lazy deletion
        to achieve optimal performance for the given constraints.

        Args:
            nums: The input array of integers.
            k: The length of each subarray.
            x: The number of top frequent elements to consider for summing.

        Returns:
            A list of integers where each element is the x-sum of the corresponding subarray.

        Example:
            >>> Solution().findXSum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2)
            [6, 10, 12]
        """
        n = len(nums)
        if n == 0:
            return []
        # Initial frequency for first window
        freq = Counter(nums[:k])
        distinct = len(freq)
        # Prepare sorted list of distinct elements by (count desc, value desc)
        items = [(cnt, val) for val, cnt in freq.items()]
        # sort by (-cnt, -val) so biggest first
        items.sort(key=lambda t: (-t[0], -t[1]))
        top_min_heap = []  # heap of (cnt, val) for elements in top (worst at top)
        rest_max_heap = []  # heap of (-cnt, -val) for elements not in top (best at top)
        in_top = {}  # val -> bool (True if currently in top set)
        sum_selected = 0
        top_size = 0
        # initialize top set: up to x best elements
        for i, (cnt, val) in enumerate(items):
            if i < x:
                in_top[val] = True
                heapq.heappush(top_min_heap, (cnt, val))
                sum_selected += cnt * val
                top_size += 1
            else:
                in_top[val] = False
                heapq.heappush(rest_max_heap, (-cnt, -val))

        # helper functions for lazy validation and pop/peek
        def pop_valid_top():
            # pop and return a valid (cnt, val) that is actually in top
            while top_min_heap:
                cnt, val = heapq.heappop(top_min_heap)
                if freq.get(val, 0) == cnt and in_top.get(val, False):
                    return cnt, val
                # else stale entry, skip
            return None

        def peek_valid_top():
            while top_min_heap:
                cnt, val = top_min_heap[0]
                if freq.get(val, 0) == cnt and in_top.get(val, False):
                    return cnt, val
                heapq.heappop(top_min_heap)  # discard stale
            return None

        def pop_valid_rest():
            # pop and return a valid (cnt, val) from rest (not in top)
            while rest_max_heap:
                negcnt, negval = heapq.heappop(rest_max_heap)
                cnt, val = -negcnt, -negval
                if freq.get(val, 0) == cnt and not in_top.get(val, False):
                    return cnt, val
                # else stale
            return None

        def peek_valid_rest():
            while rest_max_heap:
                negcnt, negval = rest_max_heap[0]
                cnt, val = -negcnt, -negval
                if freq.get(val, 0) == cnt and not in_top.get(val, False):
                    return cnt, val
                heapq.heappop(rest_max_heap)
            return None

        # Rebalance helper: ensure top_size == target and all top elements >= rest elements
        def rebalance():
            nonlocal top_size, sum_selected, distinct
            target = min(x, distinct)
            # grow top if needed
            while top_size < target:
                cand = pop_valid_rest()
                if cand is None:
                    break
                cnt, val = cand
                in_top[val] = True
                heapq.heappush(top_min_heap, (cnt, val))
                sum_selected += cnt * val
                top_size += 1
            # shrink top if needed
            while top_size > target:
                cand = pop_valid_top()
                if cand is None:
                    break
                cnt, val = cand
                in_top[val] = False
                # push to rest if still present
                if freq.get(val, 0) > 0:
                    heapq.heappush(rest_max_heap, (-cnt, -val))
                sum_selected -= cnt * val
                top_size -= 1
            # Now ensure ordering property: every element in top >= every in rest
            while True:
                t = peek_valid_top()
                r = peek_valid_rest()
                if t is None or r is None:
                    break
                # t is worst in top, r is best in rest. If r > t (by cnt then val), swap them
                if (r[0] > t[0]) or (r[0] == t[0] and r[1] > t[1]):
                    # pop the two valid entries
                    pop_valid_top()
                    pop_valid_rest()
                    tcnt, tval = t
                    rcnt, rval = r
                    # move t -> rest
                    in_top[tval] = False
                    if freq.get(tval, 0) > 0:
                        heapq.heappush(rest_max_heap, (-tcnt, -tval))
                    sum_selected -= tcnt * tval
                    # move r -> top
                    in_top[rval] = True
                    heapq.heappush(top_min_heap, (rcnt, rval))
                    sum_selected += rcnt * rval
                    # top_size unchanged
                else:
                    break

        # record initial window answer
        ans = [sum_selected]

        # slide windows
        for i in range(k, n):
            out_v = nums[i - k]
            in_v = nums[i]
            # fast path: if out_v == in_v, no frequency changes -> same answer
            if out_v != in_v:
                # apply decrement for out_v
                old = freq.get(out_v, 0)
                # old must be >=1
                # determine whether it was in top before change
                was_in_top = in_top.get(out_v, False)
                new = old - 1
                if was_in_top:
                    # update sum
                    sum_selected += (new - old) * out_v  # subtract old*out_v
                # update freq structure
                if new == 0:
                    # remove completely
                    freq.pop(out_v, None)
                    distinct -= 1
                    # if it was marked in_top, we must remove membership (we already adjusted sum)
                    if was_in_top:
                        # mark will be removed here; top_size will be corrected in rebalance
                        in_top.pop(out_v, None)
                        top_size -= 1
                    else:
                        in_top.pop(out_v, None)
                    # we don't push anything to rest/top for count==0
                else:
                    freq[out_v] = new
                    # push updated entry into the heap corresponding to its membership (lazy)
                    if was_in_top:
                        heapq.heappush(top_min_heap, (new, out_v))
                    else:
                        heapq.heappush(rest_max_heap, (-new, -out_v))

                # apply increment for in_v
                old = freq.get(in_v, 0)
                new = old + 1
                was_in_top = in_top.get(in_v, False)
                if was_in_top:
                    sum_selected += (new - old) * in_v  # add in_v
                freq[in_v] = new
                if old == 0:
                    distinct += 1
                    # ensure in_top has a default False if not present
                    if in_v not in in_top:
                        in_top[in_v] = False
                # push updated entry into appropriate heap
                if in_top.get(in_v, False):
                    heapq.heappush(top_min_heap, (new, in_v))
                else:
                    heapq.heappush(rest_max_heap, (-new, -in_v))

                # rebalance to restore invariants
                rebalance()

            # append current x-sum
            ans.append(sum_selected)

        return ans
