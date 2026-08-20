from langgraph_agent.graph import create_sdlc_graph

def test_sdlc_graph_execution():
    graph = create_sdlc_graph()
    sample_rfp = """
    - 1. System must enforce Okta OIDC authentication with PKCE.
    - 2. Database transactions must persist to Amazon RDS PostgreSQL.
    - 3. Real-time caching using Redis ElastiCache is required.
    """
    initial_state = {
        "rfp_title": "Enterprise Banking RFP",
        "raw_rfp_text": sample_rfp,
        "parsed_requirements": [],
        "retrieved_context": [],
        "draft_brd_sections": {},
        "validation_errors": [],
        "compliance_approved": False,
        "current_step": "init",
        "iteration_count": 0
    }

    final_state = graph.invoke(initial_state)

    assert len(final_state["parsed_requirements"]) >= 3
    assert final_state["compliance_approved"] is True
    assert "executive_summary" in final_state["draft_brd_sections"]
    assert "scope_of_work" in final_state["draft_brd_sections"]
    assert len(final_state["retrieved_context"]) > 0

if __name__ == "__main__":
    test_sdlc_graph_execution()
    print("Graph execution test passed successfully!")
