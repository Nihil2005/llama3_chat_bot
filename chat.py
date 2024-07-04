from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


llm = Ollama(model="llama3")

def chatbot():
    print("Welcome! I'm a chatbot. You can ask me questions.")
    print("Type 'exit' to end the conversation.")

    try:
        while True:
            text_input = input("You: ")

            if text_input.lower() == 'exit':
                print("Chatbot: Goodbye!")
                break

          
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful assistant. Your name is Nihil. You were built by the Nihil company."),
                ("user", f"User query: {text_input}")
            ])

      
            output_parser = StrOutputParser()

          
            chain = prompt | llm | output_parser


            response = chain.invoke({"query":text_input})
            print("Nihil:", response)

    except KeyboardInterrupt:
        print("\nChatbot: Interrupted. Goodbye!")

if __name__ == "__main__":
    chatbot()
