import streamlit as st

from ui.state import ensure_session_defaults
from ui.pages.landing import landing_page
from ui.pages.workspace import workspace

def main():
    """Main application entry point."""
    st.set_page_config(
        page_title="HPQ Lattice Protein Folding",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    ensure_session_defaults()

    if st.session_state["view"] == "landing":
        landing_page()
    else:
        workspace()

if __name__ == "__main__":
    main()