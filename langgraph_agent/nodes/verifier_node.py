from typing import Dict, Any, List
from langgraph_agent.state import SDLCGraphState

def verifier_node(state: SDLCGraphState) -> Dict[str, Any]:
    """
    Quality and compliance gate verifying that the generated BRD conforms to enterprise standards.
    """
    brd = state.get("draft_brd_sections", {})
    errors: List[str] = []

    if not brd.get("executive_summary"):
        errors.append("Executive summary section is missing.")
    if not brd.get("scope_of_work"):
        errors.append("Scope of work is missing or unpopulated.")
    if not brd.get("architecture_standards"):
        errors.append("Architectural compliance standards are undefined.")

    approved = len(errors) == 0
    iteration = state.get("iteration_count", 0) + 1

    return {
        "validation_errors": errors,
        "compliance_approved": approved,
        "iteration_count": iteration,
        "current_step": "verified"
    }
