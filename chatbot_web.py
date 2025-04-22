import streamlit as st
import google.generativeai as genai

# Configure the Gemini API key
genai.configure(api_key="AIzaSyDULtJo3j7h8kOkLYxCAqlWHEnKy4gFSAI")  # Replace with your actual key

# Initialize the model
model = genai.GenerativeModel("gemini-2.0-flash")

# Streamlit app config

st.set_page_config(page_title="Gemini AI Chatbot", page_icon="chatbot.png")

# Sticky header CSS
st.markdown("""
    <style>
        .sticky-title {
            position: fixed;
            top: 0;
            
            
            
            align-items: center;
            width: 49%;
            align: center;
            border-radius: 10px;
           

            
            background-color: #21262d;
            z-index: 99;
            text-align: center;
           
            color: #c9d1d9;
        }
        .chat-body {
            padding-top: 100px; /* Space for the sticky title */
            
        }
    </style>
""", unsafe_allow_html=True)

# Sticky title
import base64
import streamlit as st

# Convert image to base64
def get_base64_img(path):
    with open(path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

# Base64 version of the chatbot image
chatbot_base64 = get_base64_img("chatbot.png")

# Sticky Title with the chatbot icon
st.markdown(f"""
   

    <div class="sticky-title">
            <br>
            <br>
        <h1 style=" align-items: center; font-size: 28px; color: white;">
            <img src="{chatbot_base64}" width="40" style="margin-right: 10px;">
            Gemini Chatbot
        </h1>
        <p style="color: #aaa;">Ask me anything! * i am using gemini-2.0-flash model *  Type 'exit' to end the chat.</p>
    </div>
""", unsafe_allow_html=True)

# Chat content container
st.markdown('<div class="chat-body">', unsafe_allow_html=True)

# Maintain chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for sender, message in st.session_state.messages:
    with st.chat_message(sender.lower()):
        st.markdown(message)

# Input box
user_input = st.chat_input("Type your message here...")

if user_input:
    if user_input.lower() == "exit":
        st.write("Chat ended.")
    else:
        st.session_state.messages.append(("You", user_input))
        with st.chat_message("user"):
            st.markdown(user_input)

        chat_history_prompt = ""
        for sender, message in st.session_state.messages:
            chat_history_prompt += f"{sender}: {message}\n"
        chat_history_prompt += f"You: {user_input}\nAI:"

        response = model.generate_content(chat_history_prompt)
        ai_response = response.text

        st.session_state.messages.append(("AI", ai_response))
        with st.chat_message("ai"):
            st.markdown(ai_response)

st.markdown('</div>', unsafe_allow_html=True)  # Close .chat-body
