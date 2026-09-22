"""
FastAPI Service for LangGraph Agentic SDLC & BRD Generation
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List
from langgraph_agent.graph import create_sdlc_graph

app = FastAPI(
    title="LangGraph Agentic SDLC Service",
    description="Automated RFP-to-BRD generation pipeline orchestrated with stateful multi-agent workflows.",
    version="1.0.0"
)

graph = create_sdlc_graph()

class RFPRequest(BaseModel):
    rfp_title: str
    rfp_content: str

class BRDResponse(BaseModel):
    rfp_title: str
    total_requirements: int
    compliance_approved: bool
    sections: Dict[str, str]
    validation_errors: List[str]

@app.get("/health")
def health():
    return {"status": "healthy", "service": "langgraph-agentic-sdlc"}

@app.post("/api/v1/sdlc/generate-brd", response_model=BRDResponse)
def generate_brd(req: RFPRequest):
    try:
        initial_state = {
            "rfp_title": req.rfp_title,
            "raw_rfp_text": req.rfp_content,
            "parsed_requirements": [],
            "retrieved_context": [],
            "draft_brd_sections": {},
            "validation_errors": [],
            "compliance_approved": False,
            "current_step": "init",
            "iteration_count": 0
        }
        result = graph.invoke(initial_state)

        return BRDResponse(
            rfp_title=result.get("rfp_title"),
            total_requirements=len(result.get("parsed_requirements", [])),
            compliance_approved=result.get("compliance_approved", False),
            sections=result.get("draft_brd_sections", {}),
            validation_errors=result.get("validation_errors", [])
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
