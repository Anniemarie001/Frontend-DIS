import streamlit as st
import requests

# Streamlit UI
st.title("Document Classification")
st.write("Upload a document (PDF, PNG, JPEG, JPG) to classify it into one of the predefined categories.")

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpeg", "jpg"])

if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    
    st.write("File uploaded. Sending for classification...")
    
    # Send file to the Flask backend for classification
    response = requests.post("http://127.0.0.1:5000/classify", files={"file": (uploaded_file.name, uploaded_file, uploaded_file.type)})
    
    if response.status_code == 200:
        results = response.json()
        
        st.write("Classification Results:")
        for result in results:
            st.write(f"Filename: {result['filename']}")
            st.write(f"Page: {result['page']}")
            #st.write(f"Predicted Category Index: {result['predicted_category_index']}")
            st.write(f"Predicted Category: {result['predicted_category']}")
            st.write(f"Confidence Score: {result['confidence_score']:.4f}")
    else:
        st.write("An error occurred during classification.")
        st.write(response.text)
