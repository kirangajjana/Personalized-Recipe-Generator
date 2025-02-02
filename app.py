from dotenv import load_dotenv
import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory

# Load environment variables
load_dotenv()

# Get the API key from the .env file
apikey = os.getenv("gemini")

# Initialize the Google Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=apikey)

# Create the prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", 
         "You are a knowledgeable Personalized-Recipe-Generator. Please respond with a structured recipe including the following details:\n"
         "- Ingredients: List of ingredients required.\n"
         "- Cooking Time: How long it will take to cook the recipe.\n"
         "- Instructions: Detailed steps for preparation.\n"
         "\n"
         "### **Output Format**\n"
         "- Use bullet points for clarity.\n"
         "- Provide structured answers.\n"
         "- If any information is unavailable, respond with: 'As of now, I don't have specific details on that.'\n"
         "The user will ask for a recipe, and you should respond with the relevant information in a structured format."
        ),
        
        MessagesPlaceholder(variable_name="chat_history"),
        
        ("human", "{input}")
    ]
)



# Set up the Streamlit interface
st.title("Personalized-Recipe-Generator")

with st.sidebar:
    st.write('Welcome to Personalized-Recipe-Generator')

st.subheader("I am your Personalized-Recipe-Generator. Please ask anything to know your recipe")

# Get user input
input = st.text_input("Enter your query here")

# Initialize history storage
history_chat = StreamlitChatMessageHistory()

# Set up the chain with history
chain = prompt_template | llm | StrOutputParser()

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: history_chat,  # Pass the actual history_chat object
    input_messages_key="input",
    history_messages_key="chat_history"
)

# Handle button press
if st.button("Generate your response"):
    if input:
        with st.spinner("Generating your response, Please wait..."):
            # Invoke the chain with the provided input and history
            response = chain_with_history.invoke({"input": input}, config={"configurable": {"session_id": "kiran123"}})
            st.write(response)
    else:
        st.warning("Please enter a query to generate a response.")
