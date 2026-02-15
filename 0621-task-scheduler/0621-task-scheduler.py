class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_freq = max_count = 0
        for task, freq in count.items():
            if freq > max_freq:
                max_freq = freq
                max_count = 1
            elif freq == max_freq:
                max_count += 1

        return max(max_freq + n * (max_freq - 1) + max_count - 1, len(tasks))

        