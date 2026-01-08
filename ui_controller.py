from pipeline import run_full_pipeline

class UIController:
    def handle_input(self, user_input):
        return run_full_pipeline(user_input)
