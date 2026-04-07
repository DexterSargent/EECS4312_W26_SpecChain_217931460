"""automated persona generation pipeline"""
import json
import os
import time
from groq import Groq

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def load_reviews(file_path):
    reviews = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    reviews.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return reviews

def run_task_4_1_and_4_2():
    manual_groups_path = 'data/review_groups_manual.json'
    cleaned_reviews_path = 'data/reviews_clean.jsonl'
    output_groups_path = 'data/review_groups_auto.json'
    output_personas_path = 'personas/personas_auto.json'
    prompt_path = 'prompts/prompt_auto.json'

    manual_data = load_json(manual_groups_path)
    all_reviews = load_reviews(cleaned_reviews_path)

    if not manual_data or not all_reviews:
        print("Error: Required input files missing.")
        return

    manual_themes = [g['theme'] for g in manual_data.get('groups', [])]
    
    # Seed Batch (First 100) to define themes
    seed_batch = [{"id": r["reviewId"], "text": r["content"]} for r in all_reviews[:100]]
    
    seed_prompt = f"""
    You are a Software Requirements Engineer. 
    Manual Reference Themes for context: {json.dumps(manual_themes)}

    TASK:
    1. Analyze the provided reviews and identify 5 distinct user themes.
    2. These should be similar in spirit to the manual themes but derived from the data.
    3. Categorize these 100 reviews into those 5 themes.

    OUTPUT FORMAT (STRICT JSON):
    {{
      "themes": ["Theme Name 1", "Theme Name 2", ...],
      "groups": [
        {{
          "group_id": "auto_G1",
          "theme": "Theme Name",
          "review_ids": ["uuid1", "uuid2"],
          "example_reviews": ["Full text of review 1", "Full text of review 2"]
        }}
      ]
    }}
    
    CONSTRAINTS:
    - Each group MUST have at least 10 review_ids.
    - Provide 2 distinct example_reviews per group.

    REVIEWS: {json.dumps(seed_batch)}
    """

    print("Executing Task 4.1: Automated Review Grouping...")
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": seed_prompt}],
        temperature=0.1,
        response_format={"type": "json_object"}
    )
    
    seed_results = json.loads(completion.choices[0].message.content)
    defined_themes = seed_results.get('themes', [])
    final_groups = seed_results.get('groups', [])

    # Batch processing to avoid rate limits
    batch_size = 100
    max_reviews = min(1000, len(all_reviews))
    for i in range(100, max_reviews, batch_size):
        current_batch = [{"id": r["reviewId"], "text": r["content"]} for r in all_reviews[i:i+batch_size]]
        print(f"Sorting batch {i} to {i+len(current_batch)}...")

        batch_prompt = f"Categorize these reviews into: {json.dumps(defined_themes)}. Return JSON {{'categorized': [{{'group_id': 'auto_G1', 'review_id': 'uuid'}}]}}. REVIEWS: {json.dumps(current_batch)}"

        batch_comp = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[{"role": "user", "content": batch_prompt}],
            temperature=0.1,
            response_format={"type": "json_object"}
        )
        
        batch_data = json.loads(batch_comp.choices[0].message.content)
        for item in batch_data.get('categorized', []):
            for group in final_groups:
                if group['group_id'] == item['group_id']:
                    group['review_ids'].append(item['review_id'])

    # Save Grouping Results
    os.makedirs('data', exist_ok=True)
    with open(output_groups_path, 'w', encoding='utf-8') as f:
        json.dump({"groups": final_groups}, f, indent=4)

    # Persona Generation
    print("Executing Task 4.2: Automated Persona Generation...")
    
    persona_prompt = f"""
    You are a Software Requirements Engineer. Generate 5 detailed personas based on these groups.
    
    GROUPS DATA: {json.dumps(final_groups, indent=2)}
    
    OUTPUT FORMAT (STRICT JSON):
    {{
      "personas": [
        {{
          "id": "auto_P1",
          "name": "Catchy Name",
          "description": "Detailed profile summary",
          "derived_from_group": "auto_G1",
          "goals": ["goal 1", "goal 2"],
          "pain_points": ["pain 1", "pain 2"],
          "context": ["Usage scenario 1", "Usage scenario 2"],
          "constraints": ["Technical or personal limitation"],
          "evidence_reviews": ["UUID_from_review_ids_1", "UUID_from_review_ids_2"]
        }}
      ]
    }}
    """

    persona_comp = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": persona_prompt}],
        temperature=0.2,
        response_format={"type": "json_object"}
    )
    
    # Save the prompt used
    os.makedirs('prompts', exist_ok=True)
    with open(prompt_path, 'w', encoding='utf-8') as f:
        json.dump({
            "step_4_1_prompt": seed_prompt,
            "step_4_2_prompt": persona_prompt
        }, f, indent=4)

    # Save Personas
    os.makedirs('personas', exist_ok=True)
    with open(output_personas_path, 'w', encoding='utf-8') as f:
        json.dump(json.loads(persona_comp.choices[0].message.content), f, indent=4)

    print(f"Success. Files saved to {output_groups_path} and {output_personas_path}")

if __name__ == "__main__":
    run_task_4_1_and_4_2()