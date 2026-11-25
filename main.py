# Private PC Agent - v0.1 Starter
# Goal: AI that never leaves your PC. No cloud. No tracking.

def main():
    print("Private PC Agent - v0.1")
    print("No cloud. No tracking. No monthly fee.")
    print("---------------------------------------")
    print("This is the starting point.")
    print("Next: Add offline AI model support.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Stay private. Goodbye!")
            break
        print(f"Agent: I heard you - '{user_input}'")
        print("Agent: [Offline mode - AI model coming in v0.2]")

if __name__ == "__main__":
    main()
