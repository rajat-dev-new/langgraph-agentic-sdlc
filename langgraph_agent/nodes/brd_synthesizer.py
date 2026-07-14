from typing import Dict, Any
from langgraph_agent.state import SDLCGraphState

def brd_synthesizer_node(state: SDLCGraphState) -> Dict[str, Any]:
    """
    Synthesizes structured BRD sections by cross-referencing parsed requirements and technical context.
    """
    title = state.get("rfp_title", "Enterprise System Request")
    reqs = state.get("parsed_requirements", [])
    context = state.get("retrieved_context", [])

    req_summary = "\n".join([f"- [{r['req_id']}] ({r['priority']}) {r['description']}" for r in reqs])
    context_summary = "\n".join([f"- {c}" for c in context]) if context else "- General industry best practices"

    sections = {
        "executive_summary": f"Business Requirements Document for {title}. Synthesized via LangGraph Agent Mesh.",
        "scope_of_work": f"Identified {len(reqs)} key business requirements across functional and security domains.\n{req_summary}",
        "architecture_standards": f"Aligned with corporate governance standards:\n{context_summary}",
        "acceptance_criteria": "All API endpoints must pass automated pytest suites, Trivy vulnerability scans, and adhere to OIDC authentication."
    }

    return {
        "draft_brd_sections": sections,
        "current_step": "brd_drafted"
    }
