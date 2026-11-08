from functools import lru_cache

def read_input():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        graph: dict[str, list[str]] = {}
        for line in lines:
            parts = line.strip().split()
            key = parts[0][:-1]
            graph[key] = parts[1:]
        return graph


def solve(graph: dict[str, list[str]]):
    start = 'svr'
    end = 'out'

    @lru_cache(None)
    def dfs(node: str, has_dac: bool, has_fft: bool) -> int:
        if node == 'dac':
            has_dac = True
        if node == 'fft':
            has_fft = True

        if node == end:
            return 1 if has_dac and has_fft else 0

        total = 0
        for child in graph[node]:
            total += dfs(child, has_dac, has_fft)
        return total

    return dfs(start, False, False)


if __name__ == "__main__":
    print(solve(read_input()))
