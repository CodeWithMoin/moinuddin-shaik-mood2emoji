"""
Mood2Emoji — A kid-safe Text Mood Detector
Author: Moinuddin Shaik
Built using Streamlit + TextBlob for Codingal Curriculum Developer Intern Assignment
"""

import streamlit as st
from textblob import TextBlob
import graphviz

# Basic classroom-safe word filter
BAD_WORDS = [
    "stupid", "idiot", "hate", "dumb", "kill", "die",
    "ugly", "trash", "bully", "insane", "crazy", "fool"
]


# Check if the text contains any bad words
def is_appropriate(text):
    text = text.lower()
    for word in BAD_WORDS:
        if word in text:
            return False
    return True

# Convert the text to an emoji and a message
def mood_to_emoji(text):
    
    # Clean the text
    text = text.strip()
    
    # Check if the text is too short
    if len(text.split()) < 2:
        return "😐", "Please write a full short sentence."

    # Check if the text contains any bad words
    if not is_appropriate(text):
        return "😐", "Let's keep our language kind and school-safe."
    
    # Check tone - avoid yelling
    if text.isupper():
        return "😐", "Please write in a normal tone."
    
    # Analyze mood using TextBlob
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    # Determine the mood based on the sentiment
    if sentiment > 0.2:
        return "😀", "Sounds happy!"
    elif sentiment < -0.2:
        return "😞", "Sounds sad."
    else:
        return "😐", "Seems neutral."

# Streamlit Interface
st.title("😎 Mood2Emoji")
st.caption("A kid-safe text mood detector for ages 12–16")

text = st.text_input("Enter a short sentence:", placeholder="e.g., I’m excited for the science fair!")

if st.button("Detect Mood"):
    emoji, message = mood_to_emoji(text)
    st.markdown(f"## {emoji} {message}")

if st.sidebar.toggle("Teacher Mode", value=False):
    st.subheader("How it works")
    st.graphviz_chart(graphviz.Source('''
        digraph Mood2Emoji {
            rankdir=LR;
            node [shape=box, style="rounded"];
            A [label="User Text"];
            B [label="Safety Check"];
            C [label="Sentiment (TextBlob)"];
            D [label="Emoji 😀 😐 😞"];
            A -> B -> C -> D;
        }
    '''))
    
st.markdown("---")
st.caption("Built by Moinuddin Shaik · For demo/education only · No data stored.")