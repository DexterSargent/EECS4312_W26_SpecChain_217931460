"""generates tests from specs"""

import json
import os
import re
from groq import Groq

# Initialize Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

def generate_validation_tests():
    spec_path = 'spec/spec_auto.md'
    output_path = 'tests/tests_auto.json'
    
    if not os.path.exists(spec_path):
        print(f"Error: {spec_path} not found. Run Task 4.3 first.")
        return

    with open(spec_path, 'r', encoding='utf-8') as f:
        spec_content = f.read()

    # Extract requirement IDs and descriptions 
    req_ids = re.findall(r"Requirement ID:\s*(FR_auto_\d+)", spec_content)
    
    test_prompt = f"""
    You are a Software Quality Assurance Engineer. 
    Based on the following software specifications, generate at least one validation test scenario for EVERY requirement ID listed.

    SPECIFICATIONS:
    {spec_content}

    TASK:
    Generate a JSON object containing a list of test objects.
    
    OUTPUT FORMAT (STRICT JSON):
    {{
      "tests": [
        {{
          "test_id": "T_auto_1",
          "requirement_id": "FR_auto_1",
          "scenario": "Short descriptive title of the test",
          "steps": [
            "Step 1 description",
            "Step 2 description"
          ],
          "expected_result": "Clear description of the successful outcome"
        }}
      ]
    }}

    CONSTRAINTS:
    - Every ID in {req_ids} MUST have at least one test.
    - Steps must be clear, actionable, and logical.
    - The expected_result must directly validate the requirement's behavior.
    """

    print(f"Generating automated validation tests for {len(req_ids)} requirements...")
    
    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a QA engineer that outputs strictly valid JSON for test suites."},
                {"role": "user", "content": test_prompt}
            ],
            temperature=0.1,
            response_format={"type": "json_object"}
        )

        test_data = json.loads(completion.choices[0].message.content)

        # Save 
        os.makedirs('tests', exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, indent=4)
        
        print(f"Task 4.4 Complete. {len(test_data.get('tests', []))} tests saved to {output_path}")

    except Exception as e:
        print(f"API Error during test generation: {e}")

if __name__ == "__main__":
    generate_validation_tests()