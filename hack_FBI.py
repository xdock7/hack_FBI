import time
import random

# available commands
commands = {"help":"Show available commands",
            "meme":"Mysterious",
            "hack":"Hack somebody",
            "exit":"Quit console window"
            }

# list of memes
memes = (["https://shorturl.at/berB9", "https://rb.gy/erd9xz", "https://rb.gy/hv64c3", "https://rb.gy/i0ik1q"])
ranmemes = random.choice(memes)

# help
def available_commands():
    for key,value in commands.items():
        print(f"{key} - {value}")

# fake hacking part, force uppercase for victims
def hack():
    victims = input("Who do you want to hack? : ").upper()
    print("Command accepted, start hacking...")
    time.sleep(0.4)
    for n in range(100):
        print(f"Hacking {victims} {n+1}%")
        time.sleep(0.2)
    print(f"{victims} hacked successfully!")

# define of the list of memes
def memes():
    print(ranmemes)

# Register user input
def main():
        while True:
            i = input("Command: ").lower()
            if i == 'help':
                available_commands()
            elif i == 'meme':
                memes()
            elif i == 'hack':
                hack()
            elif i == 'exit':
                exit()
            else:
                print("An error occured, sorry :(")


if __name__ == "__main__":
    main()