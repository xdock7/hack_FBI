import time

# Define available commands
commands = {
    "help": "Check available commands",
    "meme": "Get a meme",
    "hack": "Hack FBI",
    "exit": "Quit program"}

def display_commands():
    """Display available commands"""
    for key, value in commands.items():
        print(f"{key} - {value}")

def hack_fbi():
    """Simulate hacking FBI"""
    for n in range(100):
        print(f"Hacking FBI {n}%")
        time.sleep(0.3)
    print("FBI hacked successfully!")

def main():
    while True:
        i = input('Command (type "help" to check available commands): ').lower()
        if i == "help":
            display_commands()
            #time.sleep(5)
        elif i == "hack":
            hack_fbi()
            input()
        elif i == "meme":
            print("[1](https://www.youtube.com/watch?v=BbeeuzU5Qc8)")
            time.sleep(5)
        elif i == "exit":
            exit()
        else:
            print("Invalid command. Please try again.")
            time.sleep(3)

if __name__ == "__main__":
    main()
