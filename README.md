### EECS4312 Course Project

This repository contains the course project for **EECS 4312 (Software Requirements)**. The project explores the transformation of informal user feedback into structured, testable software representations through three distinct pipelines: **Manual**, **Automated**, and **Hybrid**.

## Application Studied

**App Name:** MindDoc
The application was selected because my last name begins with S. It is a mental health resource used to track mood patterns and provide clinical insights.

## Dataset Summary

- **Final Dataset Size:** 4286 cleaned reviews.
- **Collection Method:** Extracted from the Google Play Store using the google-play-scraper.
- **Data Storage:** Raw data is stored in `data/reviews_raw.jsonl` and preprocessed data in `data/reviews_clean.jsonl`.

## Repository Structure

The repository is organized into the following folders as per the project requirements:

- `data/`: Contains raw, cleaned, and grouped review data.
- `personas/`: Stores manual, automated, and hybrid persona JSON files.
- `spec/`: Contains Markdown specifications for all three pipelines.
- `tests/`: Includes validation test scenarios in JSON format.
- `metrics/`: Stores calculated performance metrics and the final summary.
- `src/`: All Python scripts for cleaning, generation, and metric computation.
- `prompts/`: Documentation of the LLM prompts used for the automated pipeline.
- `reflection/`: Contains the final analytical summary and reflection.

## How to Run

To reproduce the automated pipeline results, follow these steps in order:

# 1. Activate your virtual environment

# On macOS/Linux:

source venv/bin/activate

# On Windows:

.\venv\Scripts\activate

# 2. Install required dependencies

pip install groq google-play-scraper nltk num2words

# 3. Export your Groq API Key

# Replace 'your_key_here' with your actual Groq API key

export GROQ_API_KEY='your_key_here'

# 4. Validate the repository structure

python src/00_validate_repo.py

# 5. Execute the full automated pipeline

python src/run_all.py
