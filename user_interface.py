import streamlit as st
from user_manual_agent import UserManualAgent

class UserInterface:
    def __init__(self):
        self.user_manual_agent = UserManualAgent()
        self.display_interface()
    
# Function to cycle through messages
    def display_interface(self):
        # Streamlit app
        st.title("User Manual Agent")
        st.write("Ask any questions you have about your appliances :sunglasses:")

        # Input text box for user query
        user_query = st.text_input("Enter your question:")

        # Button to submit the query
        if st.button("Submit"):
            if user_query:
                with st.spinner("Fetching response..."):
                    response = self.user_manual_agent(user_query)
                    st.markdown("**Response**: \n\n")
                    st.write(response.response_gen)
                    
            else:
                st.write("Please enter a question.")


if __name__ == "__main__":
    ui = UserInterface()