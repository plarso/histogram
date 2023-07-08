from collections import Counter

# Path to the dictionary file
dictionary_file = "/usr/share/dict/words"

# Read the file and count the occurrences of each letter
with open(dictionary_file, 'r') as file:
    word_list = file.read().split()
    word_list = [word.lower() for word in word_list]  # Convert words to lowercase
    letter_counts = Counter(''.join(word_list))

# Generate the histogram
max_count = max(letter_counts.values())  # Get the maximum letter count
sorted_letters = sorted(letter_counts.keys())  # Sort letters alphabetically

# Display the histogram
for letter in sorted_letters:
    count = letter_counts[letter]
    bar = '|' * int(count * 360 / max_count)  # Adjust the width of the bars. A multiplier of 360 works well on my monitor, but you decrease the multiplier to shorten the bars or increase it to lengthen the bars.
    print(f"{letter}: {bar} ({count})")
