import csv
import os
from datetime import datetime
from typing import Dict, List, Optional, Any

class GameStatsManager:
    def __init__(self):
        self.file_path = 'character_stats.csv'
        self.history_file_path = 'game_history.csv'

        # Base commander data with their specific stats
        self.characters: Dict[int, Dict[str, Any]] = {            
            1: {
                "name": "Jim Raynor",
                "specific_stats": {
                    "Healing Received from Medics": int,
                    "Damage Dealt by Hyperion": int
                }
            },
            2: {
                "name": "Kerrigan",
                "specific_stats": {
                    "Assimilated Resourced Collected": int,
                    "Damage Dealt by Kerrigan": int
                }
            },
            3: {
                "name": "Artanis",
                "specific_stats": {
                    "Damage Absorbed by Shield Overcharge": int,
                    "Damage Dealt by Spear of Adun": int
                }
            },
            4: {
                "name": "Swann",
                "specific_stats": {
                    "Healing Received from Science Vessels": int,
                    "Damage Dealt by Drakken Laser Drill": int
                }
            },
            5: {
                "name": "Zagara",
                "specific_stats": {
                    "Damage Done by Frenzied Units": int,
                    "Damage Done by Banelings and Scourge": int
                }
            },
            6: {
                "name": "Vorazun",
                "specific_stats": {
                    "Damage Dealt to Units in a Black Hole": int,
                    "Damage Dealt by Cloaked Units": int
                }
            },
            7: {
                "name": "Karax",
                "specific_stats": {
                    "Units Made during Chrono Wave": int,
                    "Danage Dealt by Spear of Adun": int
                }
            },
            8: {
                "name": "Alarak",
                "specific_stats": {
                    "Life Sacrificed to Alarak": int,
                    "Damage Dealt by Alarak": int
                }
            },
            9: {
                "name": "Abathur",
                "specific_stats": {
                    "Healing Received from Abathur": int,
                    "Damage Dealt by Ultimate Evolutions": int
                }
            },
            10: {
                "name": "Nova",
                "specific_stats": {
                    "Damage Healed and Prevented by Nova": int,
                    "Damage Dealt by Nova": int
                }
            },
            11: {
                "name": "Stukov",
                "specific_stats": {
                    "Damage Done by Monstrosities": int,
                    "Damage Dealt by Infested Infantry": int
                }
            },
            12: {
                "name": "Fenix",
                "specific_stats": {
                    "Damage Dealt by Fenix Suits": int,
                    "Damage Dealt by Champions": int
                }
            },
            13: {
                "name": "Dehaka",
                "specific_stats": {
                    "Damage Dealt by Dehaka": int,
                    "Total Supply Consumed By Dehaka": int
                }
            },
            14: {
                "name": "Hans & Horner",
                "specific_stats": {
                    "Total Scrap Resources Collected": int,
                    "Damage Dealt by Mag Mines": int
                }
            },
            15: {
                "name": "Tychus",
                "specific_stats": {
                    "Damage Dealt by Fenix Suits": int,
                    "Damage Dealt by Champions": int
                }
            },
            16: {
                "name": "Zeratul",
                "specific_stats": {
                    "Damage Dealt by Fenix Suits": int,
                    "Damage Dealt by Champions": int
                }
            },
            17: {
                "name": "Stetmann",
                "specific_stats": {
                    "Units Overloaded": int,
                    "Damage Dealt by Gary": int
                }
            },
            18: {
                "name": "Mengsk",
                "specific_stats": {
                    "Damage Dealt by Troopers": int,
                    "Damage Dealt by Royal Guards": int
                }
            }
        }

        self.maps: Dict[int, str] = {
            1: "Chain of Ascension", 2: "Cradle of Death",
            3: "Dead of Night", 4: "Lock & Load",
            5: "Malware", 6: "Miner Evacuation",
            7: "Mist Opportunities", 8: "Oblivion Express",
            9: "Part and Parcel", 10: "Rifts to Korhal",
            11: "Scythe of Amon", 12: "Temple of the Past",
            13: "The Vermillion Problem", 14: "Void Launch",
            15: "Void Thrashing"
        }

        self.prestiges = [1, 2, 3]

    def initialize_csv(self) -> None:
        """Initialize CSV files with proper error handling."""
        try:
            if not os.path.exists(self.file_path):
                with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Character", "Prestige", "Win", "Loss"])
                    for char_data in self.characters.values():
                        for prestige in self.prestiges:
                            writer.writerow([char_data["name"], prestige, 0, 0])
                        writer.writerow([f"{char_data['name']} Total", "", 0, 0])
                print(f"Successfully created {self.file_path}")

            if not os.path.exists(self.history_file_path):
                # Create header with base fields first
                header = [
                    "Date",
                    "Character",
                    "Prestige",
                    "Map",
                    "Units and Structures Killed",
                    "Units Produced",
                    "Resources Collected",
                    "Win/Loss"
                ]

                # Add commander-specific fields
                commander_specific_fields = []
                for char_data in self.characters.values():
                    commander_specific_fields.extend(char_data["specific_stats"].keys())

                # Remove duplicates while preserving order
                commander_specific_fields = list(dict.fromkeys(commander_specific_fields))
                header.extend(commander_specific_fields)

                with open(self.history_file_path, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                print(f"Successfully created {self.history_file_path}")

        except PermissionError:
            print(f"Error: Unable to create files. Please check folder permissions.")
        except Exception as e:
            print(f"Error initializing CSV files: {str(e)}")

    def get_commander_specific_stats(self, character_number: int) -> Dict[str, int]:
        """Prompt for and collect commander-specific statistics."""
        stats = {}
        char_data = self.characters[character_number]

        print(f"\nEnter {char_data['name']}-specific statistics:")
        for stat_name in char_data["specific_stats"].keys():
            while True:
                try:
                    value = int(input(f"Enter {stat_name}: "))
                    if value < 0:
                        print("Please enter a non-negative number.")
                        continue
                    stats[stat_name] = value
                    break
                except ValueError:
                    print("Please enter a valid number.")

        return stats

    def record_game_history(self, character_number: int, prestige_level: int,
                          map_name: str, kills: int, units_produced: int,
                          resources_collected: int, win_or_loss: str,
                          commander_stats: Dict[str, int]) -> bool:
        """Record game history with commander-specific stats."""
        try:
            date = datetime.now().strftime("%Y-%m-%d")
            char_data = self.characters[character_number]

            # Read existing header
            with open(self.history_file_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                header = next(reader)

            # Initialize all columns with empty strings
            row = [""] * len(header)

            # Fill in the base stats
            base_stats = {
                "Date": date,
                "Character": char_data["name"],
                "Prestige": prestige_level,
                "Map": map_name,
                "Units and Structures Killed": kills,
                "Units Produced": units_produced,
                "Resources Collected": resources_collected,
                "Win/Loss": win_or_loss
            }

            # Update row with base stats
            for i, column in enumerate(header):
                if column in base_stats:
                    row[i] = base_stats[column]

            # Update row with commander-specific stats
            for i, column in enumerate(header):
                if column in commander_stats:
                    row[i] = commander_stats[column]

            # Append the new row to the history file
            with open(self.history_file_path, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(row)

            return True

        except Exception as e:
            print(f"Error recording game history: {str(e)}")
            return False

    def update_stats(self, character_number: int, prestige_level: int, result: int) -> Optional[tuple]:
        """Update character statistics with error handling."""
        try:
            if character_number not in self.characters:
                raise ValueError(f"Invalid character number: {character_number}")
            if prestige_level not in self.prestiges:
                raise ValueError(f"Invalid prestige level: {prestige_level}")
            if result not in [1, 2]:
                raise ValueError("Result must be 1 (win) or 2 (loss)")

            character_name = self.characters[character_number]["name"]

            # Read current stats
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                header = next(reader)  # Skip header row
                stats = list(reader)

            # Find and update the correct row
            character_total_wins = 0
            character_total_losses = 0
            updated = False

            for i, row in enumerate(stats):
                if row[0] == character_name:
                    if row[1] == str(prestige_level):  # Update specific prestige stats
                        wins = int(row[2])
                        losses = int(row[3])
                        if result == 1:
                            wins += 1
                        else:
                            losses += 1
                        stats[i] = [character_name, prestige_level, wins, losses]
                        updated = True
                    elif row[1] == "":  # Update total stats
                        character_total_wins = int(row[2])
                        character_total_losses = int(row[3])
                        if result == 1:
                            character_total_wins += 1
                        else:
                            character_total_losses += 1
                        stats[i] = [f"{character_name} Total", "", character_total_wins, character_total_losses]

            if not updated:
                raise ValueError(f"Could not find stats entry for {character_name} prestige {prestige_level}")

            # Write updated stats back to file
            with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(stats)

            return (character_total_wins, character_total_losses)

        except Exception as e:
            print(f"Error updating stats: {str(e)}")
            return None

    def view_stats(self) -> None:
        """View character statistics."""
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                print("\nCharacter Statistics:")
                print("=" * 50)
                for row in reader:
                    if row[1] == "":  # Total stats row
                        print(f"{row[0]}: {row[2]} wins, {row[3]} losses\n")
                    else:  # Prestige-specific stats
                        print(f"{row[0]} (Prestige {row[1]}): {row[2]} wins, {row[3]} losses")
        except Exception as e:
            print(f"Error viewing stats: {str(e)}")

def main():
    manager = GameStatsManager()
    manager.initialize_csv()

    while True:
        try:
            # Validate action input
            while True:
                try:
                    action = int(input("\nWould you like to (1) play or (2) check stats? (Enter 1 or 2): "))
                    if action in [1, 2]:
                        break
                    else:
                        print("Invalid input. Please enter 1 to play or 2 to check stats.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value: 1 to play or 2 to check stats.")

            # If user chooses to play
            if action == 1:
                # Character selection
                print("\nSelect a character by entering their number:")
                for num, char_data in manager.characters.items():
                    print(f"{num}: {char_data['name']}")

                # Validate character number input
                while True:
                    try:
                        character_number = int(input("Enter character number: "))
                        if character_number in manager.characters:
                            break
                        else:
                            print("Invalid character number. Please enter a valid number from the list.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value in the character range.")

                # Validate prestige level input
                while True:
                    try:
                        prestige_level = int(input("Enter prestige level (1-3): "))
                        if prestige_level in [1, 2, 3]:
                            break
                        else:
                            print("Invalid prestige level. Please enter 1, 2, or 3.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value (1, 2, or 3) for the prestige level.")

                # Map selection
                print("\nSelect a map by entering the map number:")
                for num, map_name in manager.maps.items():
                    print(f"{num}: {map_name}")

                # Validate map choice input
                while True:
                    try:
                        map_choice = int(input("Enter map number: "))
                        if map_choice in manager.maps:
                            break
                        else:
                            print("Invalid map selection. Please enter a valid map number from the list.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value for the map number.")

                # Validate game result input
                while True:
                    try:
                        result = int(input("Enter result (win(1)/loss(2)): "))
                        if result in [1, 2]:
                            break
                        else:
                            print("Invalid input. Please enter 1 for win or 2 for loss.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value: 1 for win or 2 for loss.")

                # Collect game stats
                # Validate total units and structures killed
                while True:
                    try:
                        kills = int(input("Enter total units and structures killed: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")

                # Validate units produced
                while True:
                    try:
                        units_produced = int(input("Enter units produced: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")

                # Validate resources collected
                while True:
                    try:
                        resources_collected = int(input("Enter resources collected: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")

                # Get commander-specific stats
                commander_stats = manager.get_commander_specific_stats(character_number)

                # Update stats and record history
                update_result = manager.update_stats(character_number, prestige_level, result)
                if update_result:
                    total_wins, total_losses = update_result
                    print(f"Stats updated successfully! Total: {total_wins} wins, {total_losses} losses")

                    result_text = "win" if result == 1 else "loss"
                    history_result = manager.record_game_history(
                        character_number, prestige_level,
                        manager.maps[map_choice], kills,
                        units_produced, resources_collected,
                        result_text, commander_stats
                    )

                    if history_result:
                        print("Game history recorded successfully!")

            elif action == 2:
                # View character stats
                manager.view_stats()

        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

        # Continue or exit
        continue_program = int(input("Would you like to continue? (yes(1)/no(2)): "))
        while continue_program not in [1, 2]:
            print("Invalid input. Please enter 1 to continue or 2 to exit.")
            continue_program = int(input("Would you like to continue? (yes(1)/no(2)): "))
        if continue_program == 2:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()