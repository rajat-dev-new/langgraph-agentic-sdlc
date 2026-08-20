"""
LangGraph Multi-Agent StateGraph Definition
"""
from langgraph_agent.state import SDLCGraphState
from langgraph_agent.nodes.rfp_parser import rfp_parser_node
from langgraph_agent.nodes.router import requirement_router_edge
from langgraph_agent.nodes.retriever_node import retriever_node
from langgraph_agent.nodes.brd_synthesizer import brd_synthesizer_node
from langgraph_agent.nodes.verifier_node import verifier_node

class MockCompiledGraph:
    """
    Pure Python execution graph simulating LangGraph's StateGraph execution loop.
    Enables zero-dependency execution across environments while maintaining identical node interfaces.
    """
    def invoke(self, initial_state: SDLCGraphState) -> SDLCGraphState:
        state = dict(initial_state)
        
        # Step 1: RFP Parsing
        p_res = rfp_parser_node(state)
        state.update(p_res)

        # Step 2: Conditional routing
        next_step = requirement_router_edge(state)

        # Step 3: Retrieval if routed
        if next_step == "retriever":
            r_res = retriever_node(state)
            state.update(r_res)

        # Step 4: Synthesis
        s_res = brd_synthesizer_node(state)
        state.update(s_res)

        # Step 5: Verification Gate
        v_res = verifier_node(state)
        state.update(v_res)

        return state

def create_sdlc_graph():
    return MockCompiledGraph()
