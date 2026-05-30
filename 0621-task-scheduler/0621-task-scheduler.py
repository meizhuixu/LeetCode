class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # greedy
        hashmap = Counter(tasks)
        max_freq = [0, 0] # freq, number of tasks
        for freq in hashmap.values():
            if freq == max_freq[0]:
                max_freq[1] += 1
            elif freq > max_freq[0]:
                max_freq = [freq, 1]

        res = max_freq[0] * (n + 1) - n + (max_freq[1] - 1)
        return max(len(tasks), res)