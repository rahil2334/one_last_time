class InsightChatbot:
    def generate_response(self, idea, model_result):
        confidence = model_result["confidence_score"]
        risk = model_result["risk_level"]

        explanation = (
            "High feasibility idea." if risk == "LOW"
            else "Moderate feasibility idea." if risk == "MEDIUM"
            else "High risk idea."
        )

        suggestions = {
            "LOW": ["Proceed with development", "Prepare prototype"],
            "MEDIUM": ["Improve uniqueness", "Market research needed"],
            "HIGH": ["Re-evaluate idea", "Reduce complexity"]
        }

        return {
            "idea": idea,
            "confidence_score": confidence,
            "risk_level": risk,
            "explanation": explanation,
            "suggestions": suggestions[risk]
        }
