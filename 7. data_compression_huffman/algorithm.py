from heapq import heappush, heappop
from collections import Counter

class Node:
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freqs):
    heap = []
    for sym, f in freqs.items():
        heappush(heap, Node(f, symbol=sym))
    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        heappush(heap, Node(a.freq + b.freq, left=a, right=b))
    return heap[0]

def build_codes(node, prefix="", codes=None):
    if codes is None:
        codes = {}
    if node.symbol is not None:
        codes[node.symbol] = prefix or "0"
    else:
        build_codes(node.left, prefix+"0", codes)
        build_codes(node.right, prefix+"1", codes)
    return codes

def huffman_encode(s, codes):
    return ''.join(codes[ch] for ch in s)

def huffman_decode(bits, tree):
    out = []
    node = tree
    for b in bits:
        node = node.left if b == '0' else node.right
        if node.symbol is not None:
            out.append(node.symbol)
            node = tree
    return ''.join(out)

if __name__ == "__main__":
    text = "this is an example of a huffman tree"
    freqs = Counter(text)
    tree = build_huffman_tree(freqs)
    codes = build_codes(tree)
    encoded = huffman_encode(text, codes)
    decoded = huffman_decode(encoded, tree)
    print("Codes:", codes)
    print("Encoded length:", len(encoded))
    print("Decoded matches:", decoded == text)