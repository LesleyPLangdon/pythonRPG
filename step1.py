import random

# --- PLAYER SETUP ---
player_name = input("Enter your character's name: ")
player_health = 100
player_attack = 10
enemies_defeated = 0

print(f"\nWelcome, {player_name}! Your adventure begins...\n")

# --- FUNCTIONS ---

def generate_enemy():
    enemy_types = ["Goblin", "Orc", "Skeleton"]
    enemy = random.choice(enemy_types)
    health = random.randint(20, 40)
    attack = random.randint(5, 12)
    return enemy, health, attack


def battle(player_health, player_attack, enemy, enemy_health, enemy_attack):
    print(f"\n⚔️ A {enemy} appears!")

    while enemy_health > 0 and player_health > 0:
        print(f"\nYour Health: {player_health}")
        print(f"{enemy} Health: {enemy_health}")

        choice = input("Do you want to (fight/run)? ").lower()

        if choice == "fight":
            # Player attacks
            damage = random.randint(5, player_attack)
            enemy_health -= damage
            print(f"You hit the {enemy} for {damage} damage!")

            if enemy_health <= 0:
                print(f"You defeated the {enemy}!")
                return player_health, True

            # Enemy attacks
            damage = random.randint(3, enemy_attack)
            player_health -= damage
            print(f"The {enemy} hits you for {damage} damage!")

        elif choice == "run":
            chance = random.randint(1, 2)
            if chance == 1:
                print("You escaped successfully!")
                return player_health, False
            else:
                print("You failed to escape!")
                damage = random.randint(3, enemy_attack)
                player_health -= damage
                print(f"The {enemy} hits you for {damage} damage!")

        else:
            print("Invalid choice. Try again.")

    return player_health, False


# --- MAIN GAME LOOP ---
while player_health > 0:
    print("\nYou are exploring the world...")

    event = random.randint(1, 2)

    if event == 1:
        enemy, enemy_health, enemy_attack = generate_enemy()
        player_health, defeated = battle(
            player_health, player_attack, enemy, enemy_health, enemy_attack
        )

        if defeated:
            enemies_defeated += 1

    else:
        print("Nothing happens...")

    # --- WIN CONDITION ---
    if enemies_defeated >= 3:
        print(f"\n🏆 Congratulations, {player_name}! You defeated 3 enemies and won!")
        break

# --- GAME OVER ---
if player_health <= 0:
    print(f"\n💀 {player_name}, you have been defeated. Game Over.")