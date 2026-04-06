"""imports or reads your raw dataset; if you scraped, include scraper here"""
import json
from google_play_scraper import Sort, reviews_all

APP_ID = 'de.moodpath.android'

def gather_reviews():
    print(f"Starting review collection for {APP_ID}...")
    result = reviews_all(
        APP_ID,
        sleep_milliseconds=1000,
        lang='en', 
        country='us', 
        sort=Sort.NEWEST, 
    )

    reviews_to_save = result[:5000]

    with open('data/reviews_raw.jsonl', 'w', encoding='utf-8') as f:
        for review in reviews_to_save:
            f.write(json.dumps(review, default=str) + '\n')
            
    print(f"Successfully collected {len(reviews_to_save)} reviews.")
    print("Saved to: data/reviews_raw.jsonl")

if __name__ == "__main__":
    gather_reviews()