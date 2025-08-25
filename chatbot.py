import re
import random
from textblob import TextBlob
from datetime import datetime
import json

class EmpatheticChatbot:
    def __init__(self):
        self.name = "ARIA"  # Adaptive Response & Intelligence Assistant
        self.conversation_history = []
        self.user_mood_history = []
        
        # Response templates based on emotional states
        self.response_templates = {
            'very_positive': {
                'greetings': ["That's wonderful to hear! ", "I'm so glad you're feeling great! ", "Your positivity is contagious! "],
                'acknowledgments': ["I can sense your enthusiasm! ", "Your excitement comes through clearly! ", "That sounds amazing! "],
                'questions': ["What's been making you feel so positive today? ", "I'd love to hear more about what's going well! "]
            },
            'positive': {
                'greetings': ["It's great to connect with you! ", "I'm happy to chat! ", "Nice to meet you! "],
                'acknowledgments': ["That sounds good! ", "I'm glad to hear that! ", "That's nice! "],
                'questions': ["What can I help you with today? ", "What's on your mind? "]
            },
            'neutral': {
                'greetings': ["Hello! How can I help you today? ", "Hi there! ", "Good to meet you! "],
                'acknowledgments': ["I understand. ", "I see. ", "Got it. "],
                'questions': ["What would you like to talk about? ", "How can I assist you? "]
            },
            'negative': {
                'greetings': ["I'm here to help and listen. ", "I want to support you through this. ", "I'm glad you reached out. "],
                'acknowledgments': ["I can hear that you're going through something difficult. ", "That sounds really challenging. ", "I understand this must be hard for you. "],
                'questions': ["Would you like to talk about what's bothering you? ", "How can I best support you right now? ", "Is there anything specific I can help with? "]
            },
            'very_negative': {
                'greetings': ["I'm really sorry you're going through this. ", "I'm here for you, and I want to help. ", "Thank you for trusting me with your feelings. "],
                'acknowledgments': ["I can feel how much pain you're experiencing. ", "This sounds incredibly difficult and overwhelming. ", "Your feelings are completely valid. "],
                'questions': ["Would it help to talk through what's happening? ", "What kind of support do you need right most? ", "How long have you been feeling this way? "]
            }
        }
        
        # Supportive response patterns
        self.supportive_responses = {
            'anger': [
                "I can sense your frustration. It's completely understandable to feel this way.",
                "Your anger is valid. Sometimes things just don't go the way we hope.",
                "I hear how upset you are. Take a deep breath - I'm here to listen."
            ],
            'sadness': [
                "I'm sorry you're feeling this way. Sadness can be really overwhelming.",
                "It's okay to feel sad. Your emotions are important and valid.",
                "I wish I could take some of that sadness away. You don't have to go through this alone."
            ],
            'anxiety': [
                "I can sense you're feeling anxious. That must be really uncomfortable.",
                "Anxiety can be so difficult to manage. You're being brave by talking about it.",
                "I'm here with you. Let's take this one step at a time."
            ],
            'frustration': [
                "I can tell you're really frustrated. That's such a difficult feeling.",
                "Frustration is exhausting. I appreciate you sharing this with me.",
                "I hear your frustration loud and clear. What's been the hardest part?"
            ]
        }
        
        # Conversation starters and follow-ups
        self.conversation_starters = [
            "What's been on your mind lately?",
            "How has your day been treating you?",
            "What would you like to explore together?",
            "I'm here to listen - what's important to you right now?"
        ]

    def analyze_sentiment(self, text):
        """Analyze sentiment using TextBlob with enhanced emotional detection"""
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        # Enhanced emotion detection using keywords
        emotions = self.detect_specific_emotions(text.lower())
        
        # Classify overall sentiment
        if polarity > 0.3:
            sentiment = 'very_positive' if polarity > 0.6 else 'positive'
        elif polarity < -0.3:
            sentiment = 'very_negative' if polarity < -0.6 else 'negative'
        else:
            sentiment = 'neutral'
            
        return {
            'sentiment': sentiment,
            'polarity': polarity,
            'subjectivity': subjectivity,
            'emotions': emotions,
            'intensity': abs(polarity)
        }

    def detect_specific_emotions(self, text):
        """Detect specific emotions using keyword matching"""
        emotion_keywords = {
            'anger': ['angry', 'furious', 'mad', 'irritated', 'annoyed', 'pissed', 'rage', 'hate'],
            'sadness': ['sad', 'depressed', 'down', 'lonely', 'crying', 'tears', 'heartbroken', 'miserable'],
            'anxiety': ['anxious', 'worried', 'nervous', 'scared', 'panic', 'stress', 'overwhelmed', 'afraid'],
            'joy': ['happy', 'excited', 'thrilled', 'delighted', 'cheerful', 'ecstatic', 'overjoyed'],
            'frustration': ['frustrated', 'stuck', 'blocked', 'confused', 'lost', 'helpless']
        }
        
        detected_emotions = []
        for emotion, keywords in emotion_keywords.items():
            if any(keyword in text for keyword in keywords):
                detected_emotions.append(emotion)
                
        return detected_emotions

    def generate_empathetic_response(self, user_input, sentiment_analysis):
        """Generate a response that adapts to the user's emotional state"""
        sentiment = sentiment_analysis['sentiment']
        emotions = sentiment_analysis['emotions']
        intensity = sentiment_analysis['intensity']
        
        response_parts = []
        
        # Start with an empathetic acknowledgment
        if emotions:
            # Address specific emotions first
            primary_emotion = emotions[0]  # Take the first detected emotion
            if primary_emotion in self.supportive_responses:
                response_parts.append(random.choice(self.supportive_responses[primary_emotion]))
        else:
            # Use general sentiment-based response
            response_parts.append(random.choice(self.response_templates[sentiment]['acknowledgments']))
        
        # Add content-specific response
        content_response = self.generate_content_response(user_input, sentiment_analysis)
        if content_response:
            response_parts.append(content_response)
        
        # Add a follow-up question or supportive statement
        if sentiment in ['negative', 'very_negative']:
            response_parts.append(random.choice(self.response_templates[sentiment]['questions']))
        elif sentiment in ['positive', 'very_positive']:
            response_parts.append("I'd love to hear more about what's going well!")
        else:
            response_parts.append("What else is on your mind?")
        
        return " ".join(response_parts)

    def generate_content_response(self, user_input, sentiment_analysis):
        """Generate a content-specific response based on what the user is talking about"""
        text_lower = user_input.lower()
        
        # Common topics and appropriate responses
        if any(word in text_lower for word in ['work', 'job', 'boss', 'colleague']):
            if sentiment_analysis['polarity'] < 0:
                return "Work stress can be really draining. It sounds like you're dealing with some challenges there."
            else:
                return "It's great to hear things are going well at work!"
                
        elif any(word in text_lower for word in ['family', 'parent', 'mom', 'dad', 'sibling']):
            if sentiment_analysis['polarity'] < 0:
                return "Family relationships can be so complex and emotionally charged."
            else:
                return "Family connections can bring such joy and meaning to our lives."
                
        elif any(word in text_lower for word in ['friend', 'friendship', 'social']):
            if sentiment_analysis['polarity'] < 0:
                return "Friendship challenges can feel really isolating and painful."
            else:
                return "Good friendships are such a blessing - they make everything better."
        
        elif any(word in text_lower for word in ['health', 'sick', 'doctor', 'medical']):
            return "Health concerns can be so worrying. Taking care of yourself is really important."
            
        return ""

    def update_mood_history(self, sentiment_analysis):
        """Track user's emotional patterns over the conversation"""
        mood_entry = {
            'timestamp': datetime.now().isoformat(),
            'sentiment': sentiment_analysis['sentiment'],
            'polarity': sentiment_analysis['polarity'],
            'emotions': sentiment_analysis['emotions']
        }
        self.user_mood_history.append(mood_entry)

    def get_mood_trend(self):
        """Analyze if the user's mood is improving or declining"""
        if len(self.user_mood_history) < 3:
            return "stable"
            
        recent_scores = [entry['polarity'] for entry in self.user_mood_history[-3:]]
        
        if len(recent_scores) >= 3:
            # Compare the trend over the last 3 messages
            trend_change = recent_scores[-1] - recent_scores[0]
            if trend_change > 0.3:
                return "improving"
            elif trend_change < -0.3:
                return "declining"
        
        return "stable"

    def chat(self, user_input):
        """Main chat method that processes input and generates empathetic responses"""
        if not user_input.strip():
            return "I'm here and listening. What would you like to share?"
        
        # Analyze sentiment
        sentiment_analysis = self.analyze_sentiment(user_input)
        
        # Update mood tracking
        self.update_mood_history(sentiment_analysis)
        
        # Generate empathetic response
        response = self.generate_empathetic_response(user_input, sentiment_analysis)
        
        # Store conversation
        self.conversation_history.append({
            'timestamp': datetime.now().isoformat(),
            'user_input': user_input,
            'sentiment_analysis': sentiment_analysis,
            'bot_response': response
        })
        
        # Check for mood trends and add supportive comments if needed
        mood_trend = self.get_mood_trend()
        if mood_trend == "declining" and len(self.conversation_history) > 3:
            response += "\n\nI've noticed you might be having a tough time. Remember, it's okay to reach out for additional support if you need it."
        elif mood_trend == "improving" and len(self.conversation_history) > 3:
            response += " I'm glad to sense some positive shift in how you're feeling."
        
        return response

    def get_conversation_summary(self):
        """Provide a summary of the conversation and emotional journey"""
        if not self.conversation_history:
            return "We haven't started chatting yet!"
        
        sentiments = [entry['sentiment_analysis']['sentiment'] for entry in self.conversation_history]
        emotions = []
        for entry in self.conversation_history:
            emotions.extend(entry['sentiment_analysis']['emotions'])
        
        summary = f"Conversation Summary:\n"
        summary += f"- Total exchanges: {len(self.conversation_history)}\n"
        summary += f"- Predominant emotions: {', '.join(set(emotions)) if emotions else 'neutral'}\n"
        summary += f"- Overall sentiment journey: {' → '.join(sentiments)}\n"
        summary += f"- Current mood trend: {self.get_mood_trend()}\n"
        
        return summary

def main():
    """Interactive chatbot session"""
    print("🤖 Welcome to ARIA - your Adaptive Response & Intelligence Assistant")
    print("I'm here to listen and respond with empathy. Type 'quit' to exit or 'summary' for conversation overview.\n")
    
    chatbot = EmpatheticChatbot()
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print(f"\n{chatbot.name}: Thank you for chatting with me. Take care of yourself! 💙")
            break
            
        elif user_input.lower() == 'summary':
            print(f"\n{chatbot.name}: {chatbot.get_conversation_summary()}\n")
            continue
            
        elif not user_input:
            continue
            
        response = chatbot.chat(user_input)
        print(f"\n{chatbot.name}: {response}\n")

if __name__ == "__main__":
    # Example usage and testing
    print("🤖 EMPATHETIC CHATBOT OUTPUT EXAMPLES")
    print("=" * 60)
    print("This shows how ARIA adapts responses based on emotional state:\n")
    
    bot = EmpatheticChatbot()
    
    # Test different emotional inputs with detailed output
    test_scenarios = [
        {
            "input": "I'm having the worst day ever. Everything is going wrong!",
            "description": "😠 NEGATIVE EMOTION (Frustration/Anger)"
        },
        {
            "input": "I just got promoted at work! I'm so excited!",
            "description": "😊 POSITIVE EMOTION (Joy/Excitement)"
        },
        {
            "input": "I don't know what to do. I feel lost and confused.",
            "description": "😐 NEUTRAL WITH CONFUSION"
        },
        {
            "input": "My dog passed away yesterday. I can't stop crying.",
            "description": "😢 VERY NEGATIVE (Sadness/Grief)"
        },
        {
            "input": "I'm really anxious about my presentation tomorrow.",
            "description": "😰 NEGATIVE EMOTION (Anxiety)"
        },
        {
            "input": "Things are okay, I guess. Just another normal day.",
            "description": "😐 NEUTRAL EMOTION"
        }
    ]
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"{i}. {scenario['description']}")
        print("-" * 40)
        print(f"👤 User: {scenario['input']}")
        
        # Get the response
        response = bot.chat(scenario['input'])
        print(f"🤖 ARIA: {response}")
        
        # Show the sentiment analysis details
        last_analysis = bot.conversation_history[-1]['sentiment_analysis']
        print(f"📊 Analysis: {last_analysis['sentiment']} sentiment")
        print(f"   Polarity: {last_analysis['polarity']:.2f} | Emotions: {last_analysis['emotions']}")
        print()
    
    # Show conversation summary
    print("📝 CONVERSATION SUMMARY")
    print("=" * 30)
    print(bot.get_conversation_summary())
    
    # Show mood trend example
    print("\n🎭 MOOD TREND TRACKING EXAMPLE")
    print("=" * 35)
    
    # Create a new bot to show mood progression
    trend_bot = EmpatheticChatbot()
    mood_progression = [
        "I'm feeling pretty good today!",
        "Actually, something just happened that upset me...",
        "Now I'm really frustrated. This is getting worse.",
        "I don't think I can handle this anymore."
    ]
    
    for msg in mood_progression:
        response = trend_bot.chat(msg)
        print(f"👤 User: {msg}")
        print(f"🤖 ARIA: {response}")
        print()
    
    print("\n" + "=" * 60)
    print("💡 To start an interactive session, uncomment the main() call")
    print("   or run: python chatbot.py")
    
    # Uncomment the line below to start interactive session
    # main()