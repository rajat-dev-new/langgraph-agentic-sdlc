from typing import List, Dict, Any, Optional, TypedDict

class RequirementItem(TypedDict):
    req_id: str
    category: str
    description: str
    priority: str
    technical_constraints: List[str]

class SDLCGraphState(TypedDict):
    rfp_title: str
    raw_rfp_text: str
    parsed_requirements: List[RequirementItem]
    retrieved_context: List[str]
    draft_brd_sections: Dict[str, str]
    validation_errors: List[str]
    compliance_approved: bool
    current_step: str
    iteration_count: int
