def find_and_split(arr, pattern):
    for i, sub_sequence in enumerate(arr):
        if pattern in sub_sequence:
            left_part = sub_sequence[:sub_sequence.index(pattern)]
            right_part = sub_sequence[sub_sequence.index(pattern) + len(pattern):]

            # Update the original array with the two parts
            arr.pop(i)
            arr.extend([left_part, right_part])

            # Continue the process for the right part
            find_and_split(arr, pattern)
            break

# Example usage
big_array = [''
            ]

pattern_to_find = 'ATGATG'

find_and_split(big_array, pattern_to_find)

# Print the modified array
for sub_sequence in big_array:
    print(sub_sequence)
