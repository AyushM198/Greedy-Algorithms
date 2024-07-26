import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For heap comparison based on frequency
    def __lt__(self, other):
        return self.freq < other.freq

def buildHuffmanTree(chars, freq):
    # Create a priority queue (min-heap)
    min_heap = [Node(c, f) for c, f in zip(chars, freq)]
    heapq.heapify(min_heap)

    while len(min_heap) > 1:
        # Extract two nodes with the smallest frequencies
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)

        # Create a new internal node with these two nodes as children
        internal_node = Node(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right

        # Add the new internal node to the priority queue
        heapq.heappush(min_heap, internal_node)

    # The remaining node is the root of the Huffman Tree
    return min_heap[0]

def generateHuffmanCodes(root, prefix='', code_map=None):
    if code_map is None:
        code_map = {}

    if root is not None:
        if root.char is not None:
            code_map[root.char] = prefix
        generateHuffmanCodes(root.left, prefix + '0', code_map)
        generateHuffmanCodes(root.right, prefix + '1', code_map)

    return code_map

def printHuffmanCodes(codes):
    for char, code in sorted(codes.items()):
        print(code, end=' ')
    print()

# Example usage
S = "abcdef"
f = [5, 9, 12, 13, 16, 45]

# Build Huffman Tree
root = buildHuffmanTree(S, f)

# Generate Huffman Codes
codes = generateHuffmanCodes(root)

# Print Huffman Codes
printHuffmanCodes(codes)
