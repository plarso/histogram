import matplotlib.pyplot as plt
from collections import Counter

# Path to the dictionary file
dictionary_file = "/usr/share/dict/words"

# Read the file and count the occurrences of each letter
with open(dictionary_file, 'r') as file:
    word_list = file.read().split()
    letter_counts = Counter(''.join(word_list).lower())  # Convert to lowercase

# Prepare the data for the histogram
letters = sorted(letter_counts.keys())
counts = [letter_counts[letter] for letter in letters]

# Generate the histogram
plt.bar(letters, counts)

# Customize the plot
plt.xlabel('Letters')
plt.ylabel('Occurrences')
plt.title('Letter Occurrences in Dictionary')
plt.xticks(rotation=90)

# Display the plot
plt.tight_layout()
plt.show()
