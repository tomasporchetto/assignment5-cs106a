

def insert_value_at_index(string, value, index):
    if index < 0 or index > len(string):
        # Handle invalid index
        return string

    return string[:index] + value + string[index:]

def replace_letter_in_dashes(status, word, letter):
    count = 0
    new_status = ''
    times_letter_in_word = word.count(letter)

    for i in range(times_letter_in_word):

        index_ocurrance = word.find(letter,count)
        lett = status[index_ocurrance]
        new_status = insert_value_at_index(status, letter, count) 
        count += (index_ocurrance + 1)
        if i == times_letter_in_word: return new_status



original_string = "Hello world"
new_string = insert_value_at_index(original_string, "!", 7)
print(new_string)  # Output: Hello! world




