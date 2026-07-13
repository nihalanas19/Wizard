import random
import time

while True:
    print("==========================")
    print("⚽ FOOTBALL CAREER SIMULATOR")
    print("==========================")

    player_name = input("Enter your player's name: ")
    position = input("Enter your player's position (striker, midfielder, defender, goalkeeper): ").lower()

    print()
    print("Generating career...")
    time.sleep(2)

    print("👤 Player Name:", player_name)
    print("📌 Position:", position)
    print()

    if position == "striker":
        print("🎯 Career Goals:", random.randint(500, 1200))
        print("🤝 Career Assists:", random.randint(100, 400))
        print("🏆 Career Trophies:", random.randint(5, 40))

    elif position == "midfielder":
        print("🎯 Career Goals:", random.randint(100, 400))
        print("🤝 Career Assists:", random.randint(300, 900))
        print("🏆 Career Trophies:", random.randint(5, 40))

    elif position == "defender":
        print("🛡️ Career Tackles:", random.randint(1000, 4000))
        print("🚧 Career Clearances:", random.randint(1000, 5000))
        print("🏆 Career Trophies:", random.randint(5, 40))

    elif position == "goalkeeper":
        print("🧤 Career Saves:", random.randint(1000, 5000))
        print("🥅 Clean Sheets:", random.randint(100, 600))
        print("🏆 Career Trophies:", random.randint(5, 40))

    else:
        print("❌ Invalid position!")

    print()

    again = input("Play again? (yes/no): ").lower()

    if again == "no":
        print("👋 Thanks for playing!")
        break

    print()
    time.sleep(1)