import openai 

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        modeL="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()

if __name__=="_main_":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
        
