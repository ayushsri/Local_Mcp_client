from agent import build_agent

def main():
    agent = build_agent()
    print("\n🤖 MCP Local Agent Ready. Ask a question:\n")
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = agent.chat(user_input)
        print("Agent:", response)

if __name__ == "__main__":
    main()
