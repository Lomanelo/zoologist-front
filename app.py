import streamlit as st
import requests
from transformers import pipeline
from langchain.tools import tool
from langchain.chat_models import init_chat_model
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from IPython.display import Markdown
import streamlit as st
import requests
from langchain_core.messages import HumanMessage, SystemMessage
from utils_model import penguin_prediction

api = st.secrets["OPEN_AI_KEY"]
url = st.secrets["API_URL"]


model = init_chat_model("gpt-4o-mini", model_provider="openai", api_key=api)

tools = [penguin_prediction]



"""
# Zoologist front
"""

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
"""
)

"""
## Here we would like to add some controllers in order to ask the user to input the characteristics of the penguin. We need to know all the inputs required by our model to make a prediction.

1. Let's ask for:
- island (the location where the penguin lives: Biscoe, Dream or Torgersen)
- bill length (in mm)
- bill depth (in mm)
- flipper length (in mm)
- body mass (in g)
- sex ("Male" or "Female")
"""
agent = create_agent(model=model, tools=tools)

query = st.text_input("query")


if st.button('click me'):


    response = agent.invoke({"messages": [HumanMessage(content=query), SystemMessage(content="you are only allowed to answer penguin related questions or predictions.")]})
    st.write(response["messages"][4].content)

    if response["messages"][3].content.lower() == "gentoo":
        st.image("peng_images/gentoo.png")

    elif response["messages"][3].content.lower() == "adelie":
        st.image("peng_images/adelie.png")

    elif response["messages"][3].content.lower() == "chinstrap":
        st.image("peng_images/chinstrap.png")

else:
    st.write('I was not clicked 😞')
