import random
import sys

def print_ascii_banner():
    # 90s-style ASCII banner
    print(r"""
          
    """)
    print("Welcome to Dungeons, Dungeons, and More Dungeons!")
    print("Prepare to embark on a perilous quest...\n")

def print_instructions():
    print("\n=== INSTRUCTIONS ===")
    print("1. Each player starts with 20 HP (health points) and 3 Magic Points.")
    print("2. Actions each turn: attack (roll a die for damage), magic (stronger, but uses Magic Points), or heal.")
    print("3. Defeat the monster before it defeats you!")
    print("4. Have fun storming the dungeon!\n")

def main_menu():
    while True:
        print("=== MAIN MENU ===")
        print("1) Start Game")
        print("2) Instructions")
        print("3) Exit\n")

        choice = input("Choose an option (1-3): ").strip()
        if choice == '1':
            # Start the game
            return
        elif choice == '2':
            # Print instructions
            print_instructions()
        elif choice == '3':
            # Exit the program
            sys.exit("Goodbye, adventurer!")
        else:
            print("\nInvalid selection. Please choose again.\n")


class DungeonsGame:
    def __init__(self):
        """
        Initialize the game with players, health, and dice sets.
        """
        self.players = []
        self.current_player = 0
        self.dice = [4, 6, 8, 10, 12, 20]  # Standard RPG dice
        self.monster_health = random.randint(10, 50)
        print("A monstrous threat emerges from the shadows...")

    def add_player(self, name):
        """Add a new player to the game."""
        self.players.append({"name": name, "health": 20, "magic_points": 3})
        print(f"{name} has joined the game!")

    def roll_dice(self):
        """Roll a random die from the set."""
        dice_choice = random.choice(self.dice)
        roll = random.randint(1, dice_choice)
        print(f"Rolled a D{dice_choice}: {roll}")
        return roll

    def player_turn(self):
        """Handle the current player's turn."""
        player = self.players[self.current_player]
        print(f"\nIt's {player['name']}'s turn!")
        print(f"Health: {player['health']}, Magic Points: {player['magic_points']}")
        
        action = input("Choose an action (attack, magic, heal): ").lower()
        if action == "attack":
            damage = self.roll_dice()
            self.monster_health -= damage
            print(f"{player['name']} dealt {damage} damage to the monster! Monster health: {self.monster_health}")
        elif action == "magic":
            if player["magic_points"] > 0:
                damage = self.roll_dice() + 5
                self.monster_health -= damage
                player["magic_points"] -= 1
                print(f"{player['name']} cast a spell for {damage} damage! Monster health: {self.monster_health}")
            else:
                print("You have no magic points left!")
        elif action == "heal":
            heal = self.roll_dice()
            player["health"] += heal
            print(f"{player['name']} healed for {heal} points! Health: {player['health']}")
        else:
            print("Invalid action or not enough magic points.")

        # Check if monster is defeated
        if self.monster_health <= 0:
            print("\nThe monster is defeated! You win!")
            sys.exit(0)

        # Pass the turn to the next player
        self.current_player = (self.current_player + 1) % len(self.players)

    def play(self):
        """Start the game."""
        while len(self.players) < 2:
            name = input("Enter player name: ")
            self.add_player(name)

        print("\nThe dungeon awaits! A monster appears!")
        while True:
            self.player_turn()


def main():
    # Print the fancy ASCII banner
    print_ascii_banner()
    # Show the main menu
    main_menu()
    # Once user selects "Start Game", we proceed:
    game = DungeonsGame()
    game.play()

if __name__ == "__main__":
    main()
