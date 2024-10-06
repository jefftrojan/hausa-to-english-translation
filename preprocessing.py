import re

# List of common Hausa words
hausa_words = set(['na', 'ya', 'ta', 'da', 'a', 'wa', 'ka', 'ce', 'ne', 'ba', 'shi', 'su', 'yi', 'ko', 'ma', 'za', 'mu', 'kuma', 'amma', 'sai', 'don', 'yana', 'tana', 'yin', 'wani', 'wata', 'kowa', 'duk', 'gida', 'yaro', 'mace', 'mutum', 'allah', 'kudi', 'abinci', 'ruwa', 'rana', 'dare', 'yini', 'gobe', 'jiya', 'yanzu', 'can', 'nan', 'wannan', 'wancan', 'sannu', 'yaya'])

def is_likely_hausa(text):
    words = text.lower().split()
    hausa_word_count = sum(1 for word in words if word in hausa_words)
    return hausa_word_count / len(words) > 0.3  # at least 30% of words should be in our Hausa word list

def process_file(filename):
    hausa_sentences = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Remove line numbers and leading/trailing whitespace
            clean_line = re.sub(r'^\d+:\s*', '', line.strip())
            if is_likely_hausa(clean_line):
                hausa_sentences.append(clean_line)
    
    return hausa_sentences

filename = 'hausa_dataset.txt'
hausa_data = process_file(filename)

print(f"Total Hausa sentences extracted: {len(hausa_data)}")
print("Sample sentences:")
for sentence in hausa_data[:5]:
    print(sentence)

# Save our processed data
with open('processed_hausa_data.txt', 'w', encoding='utf-8') as outfile:
    for sentence in hausa_data:
        outfile.write(sentence + '\n')