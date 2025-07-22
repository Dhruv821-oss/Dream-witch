import streamlit as st
from dream_decoder import DreamDecoder

st.set_page_config(page_title="🌙 Dream Decoder", layout="centered")
st.title("🌌 Dream Decoder")
st.subheader("Decode your dreams into symbolic meanings")

# Load decoder
decoder = DreamDecoder("dreams_interpretations.csv")

# Input box
user_dream = st.text_area("Enter your dream description here:")

if st.button("Decode"):
    if user_dream.strip() == "":
        st.warning("Please enter a dream to decode.")
    else:
        with st.spinner("Interpreting your dream..."):
            results = decoder.decode(user_dream)

        st.success("Interpretation complete!")
        for res in results:
            st.markdown(f"### 🌀 {res['symbol']}")
            st.markdown(f"**Meaning:** {res['interpretation']}")
            st.markdown(f"*Similarity: {res['similarity']:.2f}*")
            st.markdown("---")
