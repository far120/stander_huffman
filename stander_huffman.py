class StandardHuffman:
    def __init__(self, data):
        self.data = data
        self.frequency = {}
        for char in data:
            if char in self.frequency:
                self.frequency[char] += 1
            else:
                self.frequency[char] = 1
        self.mean_frequency()
        self.Compresion() 
        
    def mean_frequency(self):
        totalchar = len(self.data)
        for char in self.frequency:
            self.frequency[char] /= totalchar
        print('Mean frequency: ', self.frequency)    
            
    def Compresion(self):
        arr = []
        for char, weight in self.frequency.items():
                arr.append([weight, [char, ""]])
       
        while len(arr) > 1:
            arr.sort() 
            l1 = arr.pop(0)  
            l2 = arr.pop(0)  
    
            for part in l1[1:]:
                part[1] = '0' + part[1]
                
            for part in l2[1:]:
                part[1] = '1' + part[1]
            
            arr.append([l1[0] + l2[0]] + l1[1:] + l2[1:])
            
    
        self.huffman_tree = arr[0][1:] 
        print("Huffman tree:", self.huffman_tree)
        
        self.huffman_codes = {}
        for char, bit_string in arr[0][1:]:
            self.huffman_codes[char] = bit_string
        self.huffman_codes = self.huffman_codes    
        compressed_data = ""
        for char in self.data:
            compressed_data += self.huffman_codes[char]
        print("Compressed data: ", compressed_data)
        
        self.Decompresion(compressed_data)
        self.compressed_data = compressed_data
     
     
       
    def Decompresion(self, code):
        decoded_text = ""
        current_code = ""
        
        code_to_char = {item[1]: item[0] for item in self.huffman_tree}
        
        for bit in code:
            current_code += bit
            if current_code in code_to_char:
                decoded_text += code_to_char[current_code]
                current_code = ""
        
        print("Decoded text: ", decoded_text)
        self.decoded_text = decoded_text
        
def main():
    #read from file
   with open("D:\ملفات\G3 t1 cs\datacomprasion\stander_huffman/input.txt", "r") as file:
    data = file.read().strip()
    huffman = StandardHuffman(data)
    
    # add compresed data to file
    with open("D:\ملفات\G3 t1 cs\datacomprasion\stander_huffman/compressed.txt", "w") as file:
        file.write(huffman.compressed_data)
    
   # add decompresed data to file
    with open("D:\ملفات\G3 t1 cs\datacomprasion\stander_huffman/decompressed.txt", "w") as file:
        file.write(huffman.decoded_text)


main()
