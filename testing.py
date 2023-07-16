def insert_value_at_index(string, value, index):
    if index < 0 or index > len(string):
        # Handle invalid index
        return string

    return string[:index] + value + string[index:]

original_string = "Hello world"
new_string = insert_value_at_index(original_string, "!", 7)
print(new_string)  # Output: Hello! world




