import streamlit as st
import joblib

# Load trained AI model
model = joblib.load("dna_model.pkl")

# Feature extraction
def extract_features(sequence):
    sequence = sequence.upper()

    a = sequence.count("A") / len(sequence)
    t = sequence.count("T") / len(sequence)
    g = sequence.count("G") / len(sequence)
    c = sequence.count("C") / len(sequence)
    gc = (g + c) * 100

    return [a, t, g, c, gc]

# Website title
st.title("🧬 AI-Based DNA Sequence Analyzer")

st.write("Enter a DNA sequence to predict its class.")

# DNA input
sequence = st.text_input("Enter DNA Sequence")

if st.button("Analyze DNA"):
    sequence = sequence.upper().strip()

    if sequence and all(base in "ATGC" for base in sequence):
        features = extract_features(sequence)
        prediction = model.predict([features])

        st.success("DNA Analysis Completed!")
        st.write("DNA Sequence:", sequence)
        st.write("Predicted Class:", prediction[0])

    else:
        st.error("Invalid DNA sequence. Enter only A, T, G and C.")