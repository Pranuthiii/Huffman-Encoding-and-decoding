**Problem Statement: Huffman Coding for Efficient Data Compression**

In the era of digital communication and storage, efficient data compression algorithms play a crucial role in optimizing resource utilization and transmission speed. Huffman coding, a widely adopted technique, helps achieve this by assigning shorter codes to more frequently occurring characters in a given dataset. This minimizes the overall length of the encoded data, reducing storage requirements and enhancing data transfer efficiency. Your task is to develop a Python program that leverages Huffman coding to compress and decompress user-inputted strings. The program should include components such as a `Node` class for constructing the Huffman tree, functions to build the tree and generate codes, and an interface for encoding and decoding. The goal is to create a versatile and user-friendly tool that showcases the importance of Huffman coding in the realm of data compression. Ensure adherence to PEP 8 style guidelines, provide informative user prompts, and thoroughly test the program's functionality with diverse datasets.

1. **User Input and Tree Construction:**
   - Prompt the user to enter a string for encoding.
   - Utilize the input to construct a Huffman tree based on character frequencies.

2. **Huffman Code Generation:**
   - Generate Huffman codes for each character in the constructed tree.
   - Ensure shorter codes for more frequently occurring characters.

3. **String Encoding:**
   - Encode the user-inputted string using the generated Huffman codes.
   - Output the compressed data for further analysis.

4. **String Decoding (Optional):**
   - Provide an option for the user to decode the encoded string.
   - Verify the integrity of the decoding process and output the original string.

5. **Documentation and Stylistic Guidelines:**
   - Follow PEP 8 style guidelines for clean and readable code.
   - Include informative comments and documentation for each component.

6. **Testing and Optimization:**
   - Rigorously test the program with various input scenarios.
   - Optimize the program for efficiency in terms of time and space complexity.
