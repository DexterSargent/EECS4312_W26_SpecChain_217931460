"""cleans raw data & make clean dataset"""
import json
import re
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from num2words import num2words

try:
    nltk.data.find('corpora/stopwords')
    nltk.data.find('corpora/wordnet')
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('punkt')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    # Remove empty entries
    if not text:
        return ""
    
    # Remove punctuation, special characters, and emojis
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Convert numbers to text
    text = re.sub(r'\d+', lambda x: num2words(int(x.group(0))), text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # Convert all words to lowercase
    text = text.lower()
    
    # Remove stop words
    words = text.split()
    words = [w for w in words if w not in stop_words]
    
    # Lemmatize the reviews
    words = [lemmatizer.lemmatize(w) for w in words]
    
    return " ".join(words)

def process_dataset(input_path, output_path):
    """Reads raw JSONL, cleans entries, and saves the results."""
    if not os.path.exists(input_path):
        print(f"Error: Raw data file {input_path} not found.")
        return

    cleaned_data = []
    seen_contents = set()
    
    print("Starting cleaning process...")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            review = json.loads(line)
            raw_content = review.get('content', '')
            
            # Ensure no duplicates
            if not raw_content or raw_content in seen_contents:
                continue
            
            cleaned_content = clean_text(raw_content)
            
            # Ensure no extremely short reviews
            if len(cleaned_content.split()) < 3:
                continue
            
            # Keep only necessary fields
            minimized_review = {
                "reviewId": review.get("reviewId"),
                "content": cleaned_content,
                "score": review.get("score"),
                "content_original": raw_content
            }
            
            seen_contents.add(raw_content)
            cleaned_data.append(minimized_review)

    with open(output_path, 'w', encoding='utf-8') as f:
        for entry in cleaned_data:
            f.write(json.dumps(entry) + '\n')
            
    print(f"Cleaning complete. Saved {len(cleaned_data)} unique reviews to {output_path}.")

if __name__ == "__main__":
    RAW_FILE = 'data/reviews_raw.jsonl'
    CLEAN_FILE = 'data/reviews_clean.jsonl'
    
    process_dataset(RAW_FILE, CLEAN_FILE)