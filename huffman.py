import heapq
from collections import Counter

class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

def build_huffman_tree(freq_table):
    heap = [[weight, Node(symbol=char)] for char, weight in freq_table.items()]
    
    while len(heap) > 1:
        lo = min(heap, key=lambda x: x[0])
        heap.remove(lo)
        hi = min(heap, key=lambda x: x[0])
        heap.remove(hi)
        merged_node = Node(frequency=lo[0] + hi[0])
        merged_node.left = lo[1]
        merged_node.right = hi[1]
        heap.append([merged_node.frequency, merged_node])
    
    return heap[0][1]

def generate_huffman_codes(node, current_code="", huffman_codes=None):
    if huffman_codes is None:
        huffman_codes = {}
    
    if node.symbol is not None:
        huffman_codes[node.symbol] = current_code
    if node.left is not None:
        generate_huffman_codes(node.left, current_code + "0", huffman_codes)
    if node.right is not None:
        generate_huffman_codes(node.right, current_code + "1", huffman_codes)
    
    return huffman_codes

def huffman_encode(data, huffman_codes):
    encoded_data = "".join(huffman_codes[char] for char in data)
    return encoded_data

def huffman_decode(encoded_data, root):
    decoded_data = ""
    current_node = root

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.symbol is not None:
            decoded_data += current_node.symbol
            current_node = root  # Reset to the root for the next symbol
    
    return decoded_data

def main():
    input_data = input("Enter your data to be encoded: ")
    frequency_table = Counter(input_data)
    huffman_tree_root = build_huffman_tree(frequency_table)
    huffman_codes = generate_huffman_codes(huffman_tree_root)
    encoded_data = huffman_encode(input_data, huffman_codes)
    decoded_data = huffman_decode(encoded_data, huffman_tree_root)

    print("Input Data:", input_data)
    print("Encoded Data:", encoded_data)
    
    x = input("Do you want to decode your data? ")
    if x.lower() in ('yes', 'y'):
        print("Decoded Data:", decoded_data)
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
