import re
from typing import List, Dict, Any
from langgraph_agent.state import SDLCGraphState, RequirementItem

def rfp_parser_node(state: SDLCGraphState) -> Dict[str, Any]:
    """
    Parses unstructured RFP markdown/text into structured requirement items.
    """
    raw_text = state.get("raw_rfp_text", "")
    requirements: List[RequirementItem] = []
    
    # Extract requirement blocks or lines
    lines = raw_text.splitlines()
    req_counter = 1
    for line in lines:
        line = line.strip()
        if line.startswith("-") or line.startswith("*") or re.match(r"^\d+\.", line):
            clean_req = re.sub(r"^[-*\d.]+\s*", "", line)
            if len(clean_req) > 10:
                category = "SECURITY" if any(w in clean_req.lower() for w in ["auth", "token", "pkce", "oidc", "encrypt"]) else "FUNCTIONAL"
                priority = "HIGH" if any(w in clean_req.lower() for w in ["must", "critical", "mandatory", "shall"]) else "MEDIUM"
                
                requirements.append({
                    "req_id": f"REQ-{req_counter:03d}",
                    "category": category,
                    "description": clean_req,
                    "priority": priority,
                    "technical_constraints": ["API Schema Validation", "OIDC/OAuth 2.0 Compliance"] if category == "SECURITY" else ["RESTful Standard"]
                })
                req_counter += 1

    if not requirements:
        requirements.append({
            "req_id": "REQ-001",
            "category": "FUNCTIONAL",
            "description": "General system operational capability.",
            "priority": "HIGH",
            "technical_constraints": ["Standard Microservice Architecture"]
        })

    return {
        "parsed_requirements": requirements,
        "current_step": "rfp_parsed"
    }
