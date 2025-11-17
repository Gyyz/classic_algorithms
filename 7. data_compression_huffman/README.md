# Data Compression: Huffman Coding

Huffman coding builds a prefix-free binary code that minimizes the expected code length given symbol frequencies. It is a classic lossless compression method.

Key ideas:

- Build a binary tree by repeatedly merging the two least frequent nodes.
- Assign 0/1 on edges to form codes.
- Encode and decode using the code map.

Overview

- Optimal prefix code given symbol frequencies; minimizes expected bits per symbol.
- Common in file compression and as a building block for larger codecs.

Algorithm Steps

1. Count symbol frequencies; build min-heap of nodes.
2. Repeatedly merge two lowest-frequency nodes into a parent.
3. Assign 0/1 along edges; derive code map by traversing tree.

Complexity

- Build `O(n log n)` using a heap, where `n` is number of symbols.
- Encoding/decoding linear in message length.

Pros / Cons

- Pros: simple, optimal for given frequency model; prefix-free guarantees unique decodability.
- Cons: needs frequency model; not optimal under other constraints (e.g., arithmetic coding is tighter for probabilistic models).

Usage Example

```python
from algorithm import huffman_encode, huffman_decode
codes = huffman_encode(message)
decoded = huffman_decode(codes, encoded_bits)
```