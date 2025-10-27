# Mood2Emoji — Kid-Safe Text Mood Detector 😎

Mood2Emoji is a friendly Streamlit app that reads short student messages and replies with 😃 😐 😞. It blocks the use of harsh language and calms all-caps shouting. Perfect for Codingal learners aged 12–16.

## How It Works
1. **Safety check:** Spot bad words or ALL CAPS and replace them with a neutral response.
2. **Sentiment score:** Use TextBlob to decide if the message feels positive, neutral, or negative.
3. **Emoji response:** Show a matching emoji plus a one-line explanation; Teacher Mode also reveals a Graphviz flow chart.

## Setup Instructions
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 60-Minute Classroom Plan
| Time | Teacher Actions | Student Activities |
| --- | --- | --- |
| 0–10 min | Introduce sentiment analysis by asking “How do words make us feel?” | Share sample sentences and moods. |
| 10–25 min | Demo Mood2Emoji and explain the safety filters. | Predict which emoji will appear before running the app. |
| 25–45 min | Walk through the code: safety check → sentiment → emoji logic. | Explore variations in `inputs` and note changes. |
| 45–55 min | Toggle Teacher Mode to show the flow chart. | Sketch their own decision flow on paper. |
| 55–60 min | Recap AI ethics and real-world uses. | Reflect on what surprised them and share one improvement idea. |

## Safety Features
- Blocks common bad words and swaps them for a calm message.
- Softens shouting by lowering the tone and showing 😐 instead.
- Falls back to neutral when the mood is unclear.

## Learning Outcomes
- Understand how simple sentiment analysis works with Python.
- Learn to build Streamlit apps that respond to user input.
- Discuss digital empathy and responsible AI design.

## Known Limitations
- Cannot detect sarcasm, slang, or very long stories.
- Does not include corpus of all harsh/bad words a student might use.
- Works best with short English sentences.

---

### I hope this small project helps students see how AI can understand and respond in simple steps.

---
## Author & Credits
Built by Khaja Moinuddin Shaik Mohammed for Codingal Curriculum Developer Intern Assignment.
