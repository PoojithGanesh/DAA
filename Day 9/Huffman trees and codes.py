import heapq
def huffman_coding(chars, freqs):
    heap = [[f, [c, ""]] for c, f in zip(chars, freqs)]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo, hi = heapq.heappop(heap), heapq.heappop(heap)
        for node in lo[1:]:
            node[1] = '0' + node[1]
        for node in hi[1:]:
            node[1] = '1' + node[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heap[0][1:], key=lambda x: x[0])
# Test Case 1
chars1, freqs1 = ['a', 'b', 'c', 'd'], [5, 9, 12, 13]
print(huffman_coding(chars1, freqs1))  # Output: [('a', '110'), ('b', '10'), ('c', '0'), ('d', '111')]
# Test Case 2
chars2, freqs2 = ['f', 'e', 'd', 'c', 'b', 'a'], [5, 9, 12, 13, 16, 45]
print(huffman_coding(chars2, freqs2))  # Output: [('a', '0'), ('b', '101'), ('c', '100'), ('d', '111'), ('e', '1101'), ('f', '1100')]
