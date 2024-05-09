#!/usr/bin/python3

def validUTF8(data):
    # Helper function to check if a byte is a valid continuation byte
    def is_continuation(byte):
        return byte & 0b11000000 == 0b10000000
    
    # Iterate through the data
    i = 0
    while i < len(data):
        # Get the number of bytes for the current character
        if data[i] & 0b10000000 == 0:  # 1-byte character
            length = 1
        elif data[i] & 0b11100000 == 0b11000000:  # 2-byte character
            length = 2
        elif data[i] & 0b11110000 == 0b11100000:  # 3-byte character
            length = 3
        elif data[i] & 0b11111000 == 0b11110000:  # 4-byte character
            length = 4
        else:
            return False  # Invalid UTF-8 encoding
        
        # Check if the subsequent bytes are continuation bytes
        for j in range(1, length):
            if i + j >= len(data) or not is_continuation(data[i + j]):
                return False  # Invalid UTF-8 encoding
        
        # Move to the next character
        i += length
    
    return True

# Test cases (for testing purposes, you can include these in the main section)
if __name__ == "__main__":
    data1 = [65]
    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    data3 = [229, 65, 127, 256]
    print(validUTF8(data1))  # True
    print(validUTF8(data2))  # True
    print(validUTF8(data3))  # False
