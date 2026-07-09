from src.chatbot import ChatBot

chatbot = ChatBot()

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    answer = chatbot.ask(question)

    print("\nAssistant:\n")
    print(answer)