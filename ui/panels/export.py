import json
import streamlit as st

def export_tools():
    """Render export tools for downloading results."""
    results = st.session_state.get("results", [])
    if not results:
        return

    st.markdown("**Export**")
    current_idx = st.session_state.get("current_run_index", 0)
    current = results[current_idx]

    # Single run trajectory JSON
    traj_json = json.dumps(current["trajectory"], indent=2)
    st.download_button(
        "Download current trajectory (JSON)",
        data=traj_json,
        file_name=f"trajectory_run_{current_idx+1}.json",
        mime="application/json",
    )

    # All final structures
    structures = {
        f"run_{i+1}": r["structure"] for i, r in enumerate(results)
    }
    structures_json = json.dumps(structures, indent=2)
    st.download_button(
        "Download all final structures (JSON)",
        data=structures_json,
        file_name="final_structures.json",
        mime="application/json",
    )