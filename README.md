# 🤖 ARIA - Empathetic Chatbot
**ARIA (Adaptive Response & Intelligence Assistant)** is an empathetic chatbot that analyzes users' emotional states and adapts its responses accordingly. Unlike traditional chatbots that provide static responses, ARIA understands emotions and provides contextually appropriate, supportive interactions.

## ✨ Features
- **🎭 Emotion Recognition**: Detects specific emotions like anger, sadness, anxiety, joy, and frustration
- **📊 Sentiment Analysis**: Uses TextBlob to analyze sentiment polarity and emotional intensity
- **🔄 Adaptive Responses**: Adjusts tone, language, and support level based on user's emotional state
- **📈 Mood Tracking**: Monitors emotional patterns throughout conversations
- **🎯 Context Awareness**: Recognizes topics (work, family, health) for more relevant responses
- **💙 Empathetic Communication**: Validates emotions and provides appropriate support
- **📝 Conversation Memory**: Tracks conversation history and provides summaries

## 🚀 Quick Start
### Prerequisites

```bash
pip install textblob
```

### Installation
1. Clone or download the `empathetic_chatbot.py` file
2. Install dependencies
3. Run the chatbot:

```bash
python empathetic_chatbot.py
```

## 💬 Usage Examples

### Interactive Mode
Uncomment the `main()` function call to start a live chat session:

```
🤖 Welcome to ARIA - your Adaptive Response & Intelligence Assistant
You: I'm really stressed about my job interview tomorrow
🤖 ARIA: I can sense you're feeling anxious. That must be really uncomfortable. Work stress can be really draining. How can I best support you right now?
```

### Demo Mode
Run as-is to see example conversations with detailed emotional analysis:

```
👤 User: I'm having the worst day ever. Everything is going wrong!
🤖 ARIA: Your feelings are completely valid. What kind of support do you need right now?
📊 Analysis: very_negative sentiment | Polarity: -0.81 | Emotions: ['anger', 'frustration']
```

## 🎯 How It Works

### 1. Emotion Detection
```python
# Detects specific emotions using keyword matching
emotions = ['anger', 'sadness', 'anxiety', 'joy', 'frustration']
```

### 2. Sentiment Analysis
```python
# Uses TextBlob for sentiment polarity (-1 to 1)
sentiment = analyze_sentiment(user_input)
```

### 3. Adaptive Response Generation
```python
# Selects appropriate response template based on emotional state
if sentiment == 'very_negative':
    response = supportive_templates['very_negative']
```

### 4. Mood Tracking
```python
# Monitors emotional trends over conversation
mood_trend = get_mood_trend()  # 'improving', 'declining', or 'stable'
```

## 📋 Commands

- **Interactive Chat**: Type messages to chat with ARIA
- **`summary`**: View conversation summary and emotional journey
- **`quit`** / **`exit`**: End the conversation

## 🎭 Emotional States & Responses

| Emotion State | Response Style | Example |
|---------------|----------------|---------|
| **Very Positive** | Enthusiastic, celebratory | "That's wonderful to hear! Your positivity is contagious!" |
| **Positive** | Warm, encouraging | "It's great to connect with you!" |
| **Neutral** | Balanced, open | "Hello! How can I help you today?" |
| **Negative** | Supportive, validating | "I can hear that you're going through something difficult." |
| **Very Negative** | Deeply empathetic, crisis-aware | "I'm really sorry you're going through this. I'm here for you." |

## 📊 Technical Details

### Sentiment Classification
- **Very Positive**: Polarity > 0.6
- **Positive**: Polarity > 0.3
- **Neutral**: -0.3 ≤ Polarity ≤ 0.3
- **Negative**: Polarity < -0.3
- **Very Negative**: Polarity < -0.6

### Emotion Keywords
```python
emotions = {
    'anger': ['angry', 'furious', 'mad', 'irritated', 'rage'],
    'sadness': ['sad', 'depressed', 'crying', 'heartbroken'],
    'anxiety': ['anxious', 'worried', 'nervous', 'panic', 'stress'],
    'joy': ['happy', 'excited', 'thrilled', 'delighted'],
    'frustration': ['frustrated', 'stuck', 'confused', 'helpless']
}
```

## 🔧 Customization

### Adding New Emotions
```python
emotion_keywords = {
    'your_emotion': ['keyword1', 'keyword2', 'keyword3']
}

supportive_responses = {
    'your_emotion': ["Empathetic response template"]
}
```

### Modifying Response Templates
- Edit the `response_templates` dictionary to customize how ARIA responds to different emotional states.

### Adjusting Sensitivity
- Modify polarity thresholds in the `analyze_sentiment()` method to make emotion detection more or less sensitive.

## 📈 Sample Output
```
📝 CONVERSATION SUMMARY
- Total exchanges: 5
- Predominant emotions: anxiety, frustration, joy
- Overall sentiment journey: negative → positive → neutral → negative → improving
- Current mood trend: stable
```

## 🤝 Contributing
- Feel free to enhance ARIA by:
- Adding more sophisticated NLP models
- Implementing crisis detection
- Adding multilingual support
- Creating personality traits
- Improving context understanding

## 📄 License
- This project is open source and available under the MIT License.

## 🆘 Support
- For mental health support, please reach out to:
- **Crisis Text Line**: Text HOME to 741741
- **National Suicide Prevention Lifeline**: 988
- **Your local mental health services**

---

**Built with ❤️ for emotional well-being and human connection.**
