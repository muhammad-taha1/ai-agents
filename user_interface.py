import streamlit as st
from user_manual_agent import UserManualAgent
import time


# Function to cycle through messages
placeholder = st.empty()

def cycle_messages(messages, delay=10):    
    for message in messages:
        placeholder.markdown(f"<h2 style='color:orange;'>{message}</h2>", unsafe_allow_html=True)
        time.sleep(delay)

# Messages to cycle through
messages = ["Waking up AI agent...", "Almost there...", "Just a moment..."]

# Initialize the UserManualAgent with cycling messages
if 'agent' not in st.session_state:
    with st.spinner(""):
        st.session_state.agent = UserManualAgent()
        cycle_messages(messages)
        # agent = UserManualAgent()


placeholder.empty()  # Clear the placeholder

# Streamlit app
st.title("User Manual Agent")
st.write("Ask any questions you have about your appliances :sunglasses:")

# Input text box for user query
user_query = st.text_input("Enter your question:")

# Button to submit the query
if st.button("Submit"):
    if user_query:
        with st.spinner("Fetching response..."):
            response = st.session_state.agent.query(user_query)
            st.markdown("**Response**: \n\n")
            st.write_stream(response.response_gen)
            
    else:
        st.write("Please enter a question.")