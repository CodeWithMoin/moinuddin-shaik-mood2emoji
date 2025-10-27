"""
Mood2Emoji — A kid-safe Text Mood Detector
Author: Moinuddin Shaik
Built using Streamlit + TextBlob for Codingal Curriculum Developer Intern Assignment
"""

import streamlit as st
from textblob import TextBlob
import graphviz

# Kid-safe vocabulary filters used by the safety gate
BAD_WORDS = {
    "stupid", "idiot", "hate", "dumb", "kill", "die",
    "ugly", "trash", "bully", "insane", "crazy", "fool",
}

# Low-stakes rules that let students see obvious mood clues instantly
POSITIVE_CLUES = {"happy", "great", "awesome", "excited", "love", "fun"}
NEGATIVE_CLUES = {"sad", "upset", "angry", "tired", "scared", "worried"}


def is_appropriate(text: str) -> bool:
    """Return False if the text contains blocked classroom words."""
    lowered = text.lower()
    return not any(bad in lowered for bad in BAD_WORDS)


def apply_rule_clues(words: set[str]):
    """Return an emoji/message when obvious clue words appear."""
    if words & POSITIVE_CLUES:
        return "😀", "Sounds happy!"
    if words & NEGATIVE_CLUES:
        return "😞", "Sounds sad."
    return None


def analyze_sentiment(text: str):
    """Core logic: clean → safety → rule clues → TextBlob fallback."""
    text = text.strip()

    if len(text.split()) < 2:
        return "😐", "Please write a full short sentence."

    if not is_appropriate(text):
        return "😐", "Let's keep our language kind and school-safe."

    if text.isupper() and text:
        return "😐", "Please write in a calm tone."

    words = {w.strip(".,!?").lower() for w in text.split()}
    clue = apply_rule_clues(words)
    if clue:
        return clue

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0.2:
        return "😀", "Sounds happy!"
    if sentiment < -0.2:
        return "😞", "Sounds sad."
    return "😐", "Seems neutral."


def mood_to_emoji(text: str):
    """Public helper used by the Streamlit UI."""
    return analyze_sentiment(text)


# Streamlit Interface
st.title("😎 Mood2Emoji")
st.caption("A kid-safe text mood detector for ages 12–16")

sentence = st.text_input(
    "Enter a short sentence:",
    placeholder="I’m excited for the science fair!"
)

if st.button("Detect Mood"):
    emoji, message = mood_to_emoji(sentence)
    st.markdown(f"## {emoji} {message}")

if st.sidebar.toggle("Teacher Mode", value=False):
    st.subheader("How it works")
    st.graphviz_chart(graphviz.Source('''
        digraph Mood2Emoji {
            rankdir=LR;
            node [shape=box, style="rounded"];
            A [label="Student Text"];
            B [label="Safety Check"];
            C [label="Keyword Check"];
            D [label="Sentiment (TextBlob)"];
            E [label="Emoji 😀 😐 😞"];
            A -> B -> C -> D -> E;
        }
    '''))

st.markdown("---")
st.caption("Built by Moinuddin Shaik · For demo/education only · No data stored.")
