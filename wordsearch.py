import os
import random
import time

os.system('cls' if os.name == 'nt' else 'clear')

def clear_screen():
    a = random.uniform(1, 3)
    b = 0
    while b < a:
        print("Searching..", end="\r")
        time.sleep(0.25)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.25)
        print("Searching...", end="\r")
        os.system('cls' if os.name == 'nt' else 'clear')
        b += 0.45

clear_screen()

os.system('cls' if os.name == 'nt' else 'clear')

print("Found: ", "\n\n\n\n\n\n\n")
time.sleep(0.75)

matrix = [
    ["F", "Y", "Y", "B", "Y", "B", "C", "H", "I", "C", "K", "E", "N", "P", "O", "X", "V"],
    ["R", "Z", "B", "I", "D", "E", "N", "G", "U", "E", "F", "E", "V", "E", "R", "F", "A"],
    ["K", "W", "Q", "R", "L", "P", "M", "E", "A", "S", "E", "L", "E", "S", "O", "L", "A"],
    ["E", "O", "C", "D", "Q", "N", "W", "B", "E", "J", "M", "U", "M", "P", "S", "L", "T"],
    ["R", "H", "O", "F", "B", "E", "P", "C", "E", "J", "N", "T", "V", "G", "L", "A", "Z"],
    ["A", "Z", "M", "L", "R", "U", "V", "E", "I", "T", "I", "S", "F", "E", "L", "I", "L"],
    ["T", "R", "M", "U", "O", "M", "U", "X", "W", "Y", "I", "X", "B", "L", "H", "M", "Y"],
    ["I", "O", "O", "E", "N", "O", "M", "B", "N", "A", "A", "U", "E", "S", "U", "P", "M"],
    ["T", "S", "N", "H", "C", "N", "K", "D", "N", "R", "R", "N", "U", "Z", "C", "E", "E"],
    ["I", "E", "C", "S", "H", "I", "K", "N", "H", "R", "O", "R", "U", "R", "H", "T", "D"],
    ["S", "O", "O", "Q", "I", "A", "H", "T", "L", "M", "H", "Z", "D", "G", "L", "I", "I"],
    ["E", "L", "L", "T", "T", "L", "N", "R", "L", "T", "T", "O", "U", "I", "A", "G", "S"],
    ["Q", "A", "D", "O", "I", "A", "L", "A", "T", "T", "T", "X", "A", "F", "M", "O", "E"],
    ["Y", "Z", "T", "K", "S", "D", "S", "I", "K", "S", "X", "S", "E", "B", "Y", "Y", "A"],
    ["P", "I", "N", "K", "E", "Y", "E", "X", "T", "L", "M", "A", "B", "V", "D", "M", "S"],
    ["S", "M", "A", "L", "L", "P", "O", "X", "S", "I", "Y", "R", "Q", "F", "I", "W", "E"],
    ["M", "E", "N", "I", "N", "G", "I", "T", "I", "S", "S", "S", "W", "Z", "A", "R", "O"]
]

words = ["ANTHRAX", "IMPETIGO", "SALMONELLA",
         "CHICKENPOX", "MUMPS", "THRUSH",
         "DENGUEFEVER", "MEASELES", "BIRDFLUE",
         "SARS", "ROSEOLA", "PINKEYE", "KERATITIS",
         "CHLAMYDIA", "TONSILLITIS", "RUBELLA",
         "MENINGITIS", "FLUE", "BRONCHITIS",
         "SMALLPOX", "PNEUMONIA", "LYMEDISEASE",
         "COMMONCOLD", "UVEITIS"]

def find_words(matrix, words):
    rows = len(matrix)
    cols = len(matrix[0])
    highlighted_positions = []
    words_found_count = 0

    print("WORDS FOUND:\n")

    for word in words:
        word_length = len(word)
        found = False

        for row in range(rows):
            row_str = "".join(matrix[row])
            if word in row_str:
                start_index = row_str.index(word)
                end_index = start_index + word_length - 1
                for col in range(start_index, end_index + 1):
                    highlighted_positions.append((row, col, '\033[91m'))
                found = True

        for col in range(cols):
            col_str = "".join(matrix[row][col] for row in range(rows))
            if word in col_str:
                start_index = col_str.index(word)
                end_index = start_index + word_length - 1
                for row in range(start_index, end_index + 1):
                    highlighted_positions.append((row, col,                    '\033[32m'))
                found = True

        for row in range(rows - word_length + 1):
            for col in range(cols - word_length + 1):
                diagonal_str = "".join(matrix[row + i][col + i] for i in range(word_length))
                if word in diagonal_str:
                    start_index = diagonal_str.index(word)
                    end_index = start_index + word_length - 1
                    for i in range(start_index, end_index + 1):
                        highlighted_positions.append((row + i, col + i, '\033[94m'))
                    found = True

        for row in range(rows - word_length + 1):
            for col in range(word_length - 1, cols):
                diagonal_str = "".join(matrix[row + i][col - i] for i in range(word_length))
                if word in diagonal_str:
                    start_index = diagonal_str.index(word)
                    end_index = start_index + word_length - 1
                    for i in range(start_index, end_index + 1):
                        highlighted_positions.append((row + i, col - i, '\033[94m'))  
                    found = True

        for row in range(word_length - 1, rows):
            for col in range(cols - word_length + 1):
                diagonal_str = "".join(matrix[row - i][col + i] for i in range(word_length))
                if word in diagonal_str:
                    start_index = diagonal_str.index(word)
                    end_index = start_index + word_length - 1
                    for i in range(start_index, end_index + 1):
                        highlighted_positions.append((row - i, col + i, '\033[94m'))  
                    found = True

        if found:
            words_found_count += 1
        else:
            print(f"WORD NOT FOUND: {word}")

    for row in range(rows):
        for col in range(cols):
            found_flag = False
            for pos_row, pos_col, color_code in highlighted_positions:
                if row == pos_row and col == pos_col:
                    print(color_code + '\033[1m' + matrix[row][col] + '\033[0m', end=' ')
                    found_flag = True
                    break
            if not found_flag:
                print(matrix[row][col], end=' ')
        print()

    return words_found_count

words_found_count = find_words(matrix, words)
print(f"\nNumber of words found: {words_found_count}")
