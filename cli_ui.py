from controller.ui_controller import UIController

controller = UIController()

while True:
    idea = input("Enter your idea (or exit): ")
    if idea.lower() == "exit":
        break

    result = controller.handle_input(idea)
    print(result)
