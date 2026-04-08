"""computes metrics: coverage/traceability/ambiguity/testability"""

import json
import os
import re
import sys

def calculate_metrics(pipeline_type="auto"):
    # File Paths 
    paths = {
        "reviews": "data/reviews_clean.jsonl",
        "groups": f"data/review_groups_{pipeline_type}.json",
        "personas": f"personas/personas_{pipeline_type}.json",
        "spec": f"spec/spec_{pipeline_type}.md",
        "tests": f"tests/tests_{pipeline_type}.json",
        "output": f"metrics/metrics_{pipeline_type}.json"
    }

    # 1. Dataset Size
    total_reviews = 0
    if os.path.exists(paths["reviews"]):
        with open(paths["reviews"], 'r', encoding='utf-8') as f:
            total_reviews = sum(1 for line in f)

    # 2. Persona Count
    personas = []
    if os.path.exists(paths["personas"]):
        with open(paths["personas"], 'r', encoding='utf-8') as f:
            data = json.load(f)
            personas = data.get("personas", [])
    persona_count = len(personas)

    # 3. Requirements Count & Traceability
    req_ids = []
    req_with_persona = 0
    ambiguous_reqs = 0
    vague_terms = ["fast", "easy", "better", "user-friendly", "seamless", "intuitive", "robust"]
    
    if os.path.exists(paths["spec"]):
        with open(paths["spec"], 'r', encoding='utf-8') as f:
            content = f.read()

            req_ids = re.findall(r"Requirement ID:\s*(\S+)", content)
            
            sections = re.split(r"# Requirement ID:", content)[1:]
            for section in sections:
                if "Source Persona:" in section and "[" not in section:
                    req_with_persona += 1

                if any(term in section.lower() for term in vague_terms):
                    ambiguous_reqs += 1
    
    req_count = len(req_ids)

    # 4. Tests Count
    tests = []
    tested_req_ids = set()
    if os.path.exists(paths["tests"]):
        with open(paths["tests"], 'r', encoding='utf-8') as f:
            data = json.load(f)
            tests = data.get("tests", [])
            for t in tests:
                tested_req_ids.add(t.get("requirement_id"))
    test_count = len(tests)

    # 5. Review Coverage
    covered_reviews = set()
    if os.path.exists(paths["groups"]):
        with open(paths["groups"], 'r', encoding='utf-8') as f:
            data = json.load(f)
            for g in data.get("groups", []):
                covered_reviews.update(g.get("review_ids", []))
    
    # --- Final Metric Calculations ---
    
    # Traceability links: Sum of all inter-artifact connections
    # (Review->Group) + (Persona->Group) + (Req->Persona) + (Test->Req)
    traceability_links = len(covered_reviews) + persona_count + req_with_persona + test_count

    metrics = {
        "dataset_size": total_reviews,
        "persona_count": persona_count,
        "requirements_count": req_count,
        "tests_count": test_count,
        "traceability_links": traceability_links,
        "review_coverage_ratio": round(len(covered_reviews) / total_reviews, 4) if total_reviews > 0 else 0,
        "traceability_ratio": round(req_with_persona / req_count, 4) if req_count > 0 else 0,
        "testability_rate": round(len(tested_req_ids) / req_count, 4) if req_count > 0 else 0,
        "ambiguity_ratio": round(ambiguous_reqs / req_count, 4) if req_count > 0 else 0
    }

    # Save
    os.makedirs('metrics', exist_ok=True)
    with open(paths["output"], 'w', encoding='utf-8') as f:
        json.dump(metrics, f, indent=4)
    
    print(f"Metrics for {pipeline_type} pipeline saved to {paths['output']}")
    return metrics

if __name__ == "__main__":

    p_type = sys.argv[1] if len(sys.argv) > 1 else "auto"
    calculate_metrics(p_type)