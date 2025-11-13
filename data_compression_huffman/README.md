# Data Compression: Huffman Coding

Huffman coding builds a prefix-free binary code that minimizes the expected code length given symbol frequencies. It is a classic lossless compression method.

Key ideas:

- Build a binary tree by repeatedly merging the two least frequent nodes.
- Assign 0/1 on edges to form codes.
- Encode and decode using the code map.