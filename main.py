import google.generativeai as genai

# Configure your API key
genai.configure(api_key="YOUR_API_KEY_HERE")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-pro-latest")


def ask_edugenie(question):
    response = model.generate_content(
        f"You are EduGenie, a Google Gemini powered learning assistant. Please answer the following question: {question}"
    )
    return response.text


# Example usage
if __name__ == "__main__":
    while True:
        user_question = input("Ask EduGenie a question (or type 'quit' to exit): ")
        if user_question.lower() == "quit":
            break
        answer = ask_edugenie(user_question)
        print("\nEduGenie:", answer)
        print("-" * 50)
      
