import csv
import random

def prepare_for_manual_translation(input_file, output_file, sample_size=1000):
    with open(input_file, 'r', encoding='utf-8') as infile:
        hausa_sentences = [line.strip() for line in infile if line.strip()]
    
    # Randomly sample sentences if there are more than sample_size
    if len(hausa_sentences) > sample_size:
        hausa_sentences = random.sample(hausa_sentences, sample_size)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile, delimiter='\t')
        writer.writerow(['Hausa', 'English'])  # Header
        
        for sentence in hausa_sentences:
            writer.writerow([sentence, ''])  # Empty English column for manual translation
    
    print(f"Prepared {len(hausa_sentences)} sentences for manual translation.")
    print(f"Please open '{output_file}' and fill in the English translations.")

# Usage
input_file = 'processed_hausa_data.txt'
output_file = 'hausa_for_manual_translation.tsv'
prepare_for_manual_translation(input_file, output_file)