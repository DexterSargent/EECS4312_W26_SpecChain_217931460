"""generates structured specs from personas"""

import json
import os
from groq import Groq

# Initialize Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

def generate_specifications():
    persona_path = 'personas/personas_auto.json'
    output_path = 'spec/spec_auto.md'
    
   
    os.makedirs('spec', exist_ok=True)

    # Load personas 
    if not os.path.exists(persona_path):
        print(f"Error: {persona_path} not found. Run Task 4.2 first.")
        return

    with open(persona_path, 'r', encoding='utf-8') as f:
        persona_data = json.load(f)
    
    personas = persona_data.get('personas', [])

    spec_prompt = f"""
    You are a Senior Requirements Engineer. 
    Based on the following automated personas, generate a structured software specification.

    INPUT PERSONAS:
    {json.dumps(personas, indent=2)}

    TASK:
    Generate at least 10 functional requirements (2 per persona).
    The output MUST strictly follow this Markdown format for EVERY requirement:

    # Requirement ID: [Unique ID, e.g., FR_auto_1]
    - Description: [Clear description of system behavior]
    - Source Persona: [Name of the persona]
    - Traceability: [Derived from review group ID, e.g., auto_G1]
    - Acceptance Criteria: [Measurable "Given/When/Then" or equivalent criteria]

    CONSTRAINTS:
    - Do not include any conversational filler. 
    - Ensure every requirement is traceable to the 'derived_from_group' of the persona.
    """

    print(f"Generating automated specifications using {MODEL}...")
    
    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a requirements engineer that outputs valid Markdown specs."},
                {"role": "user", "content": spec_prompt}
            ],
            temperature=0.2
        )

        spec_content = completion.choices[0].message.content

        # Save 
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(spec_content)
        
        print(f"Task 4.3 Complete. Specifications saved to {output_path}")

    except Exception as e:
        print(f"API Error during specification generation: {e}")

if __name__ == "__main__":
    generate_specifications()