import random

teams = {
    "Arsenal": {"budget": 80000000, "players": ["Saka", "Saliba", "Rice"]},
    "Chelsea": {"budget": 75000000, "players": ["Palmer", "Caicedo", "James"]}
}

player_stats = {
    "Saka": {"rating": 89, "goals": 15},
    "Saliba": {"rating": 85, "goals": 2},
    "Rice": {"rating": 90, "goals": 8},
    "Palmer": {"rating": 87, "goals": 14},
    "Caicedo": {"rating": 84, "goals": 4},
    "James": {"rating": 82, "goals": 1}
}


def simulate_match(home_team, away_team):
    home_total = 0
    away_total = 0

    for player in teams[home_team]["players"]:
        home_total += player_stats[player]["rating"]

    for player in teams[away_team]["players"]:
        away_total += player_stats[player]["rating"]

    home_avg = home_total / len(teams[home_team]["players"])
    away_avg = away_total / len(teams[away_team]["players"])

    home_goals = 0
    away_goals = 0

    for _ in range(90):
        if random.random() < 0.02 + (home_avg - away_avg) / 1000:
            home_goals += 1
        if random.random() < 0.02 + (away_avg - home_avg) / 1000:
            away_goals += 1

    return home_goals, away_goals


def show_teams():
    print("\nTeams:")
    for team_name, team_data in teams.items():
        print(f"- {team_name} (budget: ${team_data['budget']:,})")


def show_players():
    print("\nPlayers:")
    for team_name, team_data in teams.items():
        print(f"\n{team_name}:")
        for player in team_data["players"]:
            print(f"- {player}: rating {player_stats[player]['rating']}, goals {player_stats[player]['goals']}")


while True:
    print("\n====== Football Manager ======")
    print("1. Show Teams")
    print("2. Show Players")
    print("3. Simulate Match")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_teams()
    elif choice == "2":
        show_players()
    elif choice == "3":
        home_team = input("Home team: ")
        away_team = input("Away team: ")
        home_goals, away_goals = simulate_match(home_team, away_team)
        print(f"\n{home_team} {home_goals} - {away_goals} {away_team}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")

