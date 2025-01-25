import streamlit as st
from user_manual_agent import UserManualAgent

@st.cache_resource
def initialize_agent():
    user_manual_agent = UserManualAgent()
    return user_manual_agent


# Function to cycle through messages
def display_interface(user_manual_agent):
    # Streamlit app
    st.title("User Manual Agent")
    st.write("Ask any questions you have about your appliances :sunglasses:")

    # Input text box for user query
    user_query = st.text_input("Enter your question:")

    # Button to submit the query
    if st.button("Submit"):
        if user_query:
            with st.spinner("Fetching response..."):
                response = user_manual_agent.query(user_query)
                st.markdown("**Response**: \n\n")
                st.write_stream(response.response_gen)
                
        else:
            st.write("Please enter a question.")

user_manual_agent = initialize_agent()
display_interface(user_manual_agent)
