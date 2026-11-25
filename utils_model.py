from langchain.tools import tool
import requests
import streamlit as st

url = st.secrets["API_URL"]

@tool(parse_docstring=True)
def penguin_prediction(island:str,
                       bill_length_mm: float,
                       bill_depth_mm: float,
                       flipper_length_mm: float,
                       body_mass_g: float,
                       sex: str):
    """predicts and returns which kind of penguin from params given by user.

    if given seperated amounts with no explanation, take them as arguments in order of appearance.

    Args:
        island: the island of the penguin.
        bill_length_mm: length of the penguin bill in milimiters.
        bill_depth_mm: depth of the penguin bill in milimeters.
        flipper_length_mm: length of the flipper of the penguin in milimiters.
        body_mass_g: mass of the body of the penguin in grams.
        sex: the sex of the penguin.

    Returns:
        the the type of penguin
    """


    params = {"island": island, "bill_length_mm": bill_length_mm, "bill_depth_mm": bill_depth_mm, "flipper_length_mm": flipper_length_mm, "body_mass_g": body_mass_g, "sex": sex}
    prediction = requests.get(url, params=params).json()["prediction"]
    return prediction
