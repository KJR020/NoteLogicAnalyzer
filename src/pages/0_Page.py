from typing import Any

import numpy as np

import streamlit as st


st.set_page_config(page_title="Animation Demo", page_icon="📹")
st.markdown("# Animation Demo")
st.sidebar.header("Animation Demo")
st.write(
    """This app shows how you can use Streamlit to build cool animations.
It displays an animated fractal based on the the Julia Set. Use the slider
to tune different parameters."""
)
