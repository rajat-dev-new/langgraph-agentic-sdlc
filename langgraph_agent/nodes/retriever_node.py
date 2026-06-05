from typing import Dict, Any, List
from langgraph_agent.state import SDLCGraphState

# Simulated corporate architectural knowledge repository
ARCHITECTURE_KNOWLEDGE_BASE = [
    "Enterprise Standard: All external authentication must enforce Okta OIDC Authorization Code Flow with PKCE.",
    "Storage Policy: Relational datasets must persist to Amazon RDS PostgreSQL Multi-AZ with encrypted EBS volumes.",
    "Caching Policy: Session and transient tokens must utilize AWS ElastiCache Redis clustering.",
    "Container Standard: All container images must pass automated Trivy vulnerability scanning without High or Critical CVEs."
]

def retriever_node(state: SDLCGraphState) -> Dict[str, Any]:
    """
    RAG retrieval node that injects relevant corporate standards based on requirements.
    """
    requirements = state.get("parsed_requirements", [])
    injected_context: List[str] = []

    for req in requirements:
        desc = req.get("description", "").lower()
        if "auth" in desc or "security" in desc or "sso" in desc:
            injected_context.append(ARCHITECTURE_KNOWLEDGE_BASE[0])
        if "database" in desc or "persist" in desc:
            injected_context.append(ARCHITECTURE_KNOWLEDGE_BASE[1])
        if "cache" in desc or "session" in desc:
            injected_context.append(ARCHITECTURE_KNOWLEDGE_BASE[2])

    if not injected_context:
        injected_context.append("Standard enterprise cloud compliance guidelines apply.")

    return {
        "retrieved_context": list(set(injected_context)),
        "current_step": "context_retrieved"
    }
