# Simple Python Chatbot using only basics

# Base knowledge stored in a dictionary
knowledge_base = {
    "hello": "Hello there! How can I help you?",
    "how are you": "I’m doing great, thanks for asking!",
    "good job": "oh thanks <3",
    "bye": "Goodbye! Have a nice day."
}

# To store user's name (once entered)
user_data = {"name": None}

def chatbot():
    print("Bot: Hi! What's your name?")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        # 1. Store name if not yet saved
        if user_data["name"] is None:
            user_data["name"] = user_input.title()
            print(f"Bot: Nice to meet you, {user_data['name']}! How can I help?")
            continue
        
        # 2. Check for exit
        if user_input in ["bye", "exit", "quit"]:
            print(f"Bot: Bye {user_data['name']}! Take care.")
            break
        
        # 3. Math operations detection
        if "+" in user_input:
            numbers = user_input.split("+")
            try:
                total = sum(int(n.strip()) for n in numbers)
                print(f"Bot: The sum is {total}")
            except ValueError:
                print("Bot: Please enter valid numbers for addition.")
            continue
        
        if "-" in user_input:
            numbers = user_input.split("-")
            try:
                result = int(numbers[0].strip())
                for n in numbers[1:]:
                    result -= int(n.strip())
                print(f"Bot: The result is {result}")
            except ValueError:
                print("Bot: Please enter valid numbers for subtraction.")
            continue
        
        # 4. Known questions from knowledge base
        if user_input in knowledge_base:
            print(f"Bot: {knowledge_base[user_input]}")
        
        # 5. Unknown questions
        else:
            print("Bot: Sorry, I don't know the answer to that.")

# Run chatbot
chatbot()
