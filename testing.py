

def insert_value_at_index(string, value, index):
    if index < 0 or index > len(string):
        # Handle invalid index
        return string

    value = string[:index] + value + string[index + 1:]
    return value



original_string = "Hello world"
new_string = insert_value_at_index(original_string, "!", 7)
print(new_string)  # Output: Hello! world




