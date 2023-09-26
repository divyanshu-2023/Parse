def parse_encoded_string(encoded_str):
    parts = encoded_str.split('0')
    
    if len(parts) == 3:
        return {
            "first_name": parts[0],
            "last_name": parts[1],
            "id": parts[2]
        }
    else:
        return None

encoded_str = "John000Doe000123"
result = parse_encoded_string(encoded_str)
print(result)
