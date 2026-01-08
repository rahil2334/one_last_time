from model.idea_analysis_engine import IdeaAnalysisEngine
from chatbot.insight_chatbot import InsightChatbot

def run_full_pipeline(user_text):
    # Dummy dataset texts (replace with Kaggle-loaded text column)
    dataset_texts = [
        "AI based healthcare diagnosis system",
        "Stock market prediction using machine learning",
        "Smart traffic management using IoT",
        "Fraud detection in banking systems"
    ]

    model = IdeaAnalysisEngine(dataset_texts)
    result = model.analyze_idea(user_text)

    chatbot = InsightChatbot()
    response = chatbot.generate_response(user_text, result)

    return response
