def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char)-ord("a")
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence
    print(max_alphabet_index)


print(find_alphabet_occurrence_array("hello my name is sparta"))