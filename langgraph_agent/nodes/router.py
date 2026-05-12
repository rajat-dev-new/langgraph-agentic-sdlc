from typing import Literal
from langgraph_agent.state import SDLCGraphState

def requirement_router_edge(state: SDLCGraphState) -> Literal["retriever", "brd_synthesizer"]:
    """
    Conditional edge evaluator.
    If requirements contain specialized security or infrastructure demands,
    routes through knowledge retrieval first; otherwise direct synthesis.
    """
    requirements = state.get("parsed_requirements", [])
    has_complex_security = any(r.get("category") == "SECURITY" for r in requirements)
    
    if has_complex_security:
        return "retriever"
    return "brd_synthesizer"
