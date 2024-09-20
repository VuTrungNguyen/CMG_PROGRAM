import csv
import json
import re

# Path to the uploaded file
file_path = 'US_qbank.jsonl'
output_csv = 'endoscopy_questions.csv'

def fix_encoding(text):
    try:
        # Try to encode the text as latin1 and decode it back as utf-8
        return text.encode('latin1').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        # If it fails, return the text as is
        return text
    
# Load the dataset
asthma_questions = []

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = fix_encoding(line)
            question = json.loads(line)
            # Check if the word 'asthma' appears in the question text (case-insensitive)
            if 'endoscopy' in question['question'].lower():
                asthma_questions.append(question)
except UnicodeDecodeError:
    print("Encoding error: The file may contain non-UTF-8 encoded characters.")

# Output the first few asthma-related questions and total count
print(asthma_questions[:5], len(asthma_questions))  # Show first 5 entries and total count

# Write the asthma-related questions to CSV
with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['question', 'answer_detail', 'answer']  # Adjust field names based on JSON structure
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for question in asthma_questions:
        options = question.get('options', {})
        answer_label = question.get('answer', '').strip()
        answer = options.get(answer_label, '') if options else ''
        writer.writerow({
            'question': question['question'],
            'answer_detail': answer,
            'answer': answer_label,
        })

print(f"Endoscopy-related questions saved to {output_csv}")
