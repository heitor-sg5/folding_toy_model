import streamlit as st

from core.config import DEFAULT_PARAMS

def ensure_session_defaults():
    """Initialize default session state values."""
    st.session_state.setdefault("view", "landing")
    st.session_state.setdefault("results", [])
    st.session_state.setdefault("current_run_index", 0)
    st.session_state.setdefault("current_step_index", 0)
    st.session_state.setdefault("color_mode", "Hydrophobicity")
    st.session_state.setdefault("params", DEFAULT_PARAMS.copy())