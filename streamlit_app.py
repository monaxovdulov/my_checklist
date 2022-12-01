import streamlit as st


dice_type = st.sidebar.selectbox('Type of dice', ('coin', 'tetrahedron', 'nonagon', 'dice'))
st.write("Hello word!")
st.write(dice_type)
