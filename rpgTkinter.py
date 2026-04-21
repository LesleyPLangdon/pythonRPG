import tkinter as tk
import random

# ── constants ────────────────────────────────────────────────────────────────
BG        = "#1a1a2e"
PANEL     = "#16213e"
ACCENT    = "#e94560"
TEXT      = "#eaeaea"
MUTED     = "#8888aa"
GREEN     = "#4ecca3"
YELLOW    = "#f5a623"
BTN_BG    = "#0f3460"
BTN_HOV   = "#e94560"
FONT_MAIN = ("Courier New", 12)
FONT_HEAD = ("Courier New", 14, "bold")
FONT_BIG  = ("Courier New", 18, "bold")

# ── game state ────────────────────────────────────────────────────────────────
state = {
    "screen": "name",          # name | explore | battle | gameover | win
    "player_name": "",
    "player_health": 100,
    "player_attack": 10,
    "enemies_defeated": 0,
    "enemy_name": "",
    "enemy_health": 0,
    "enemy_attack": 0,
}

# ── helpers ───────────────────────────────────────────────────────────────────
def generate_enemy():
    enemy_types = ["Goblin", "Orc", "Skeleton"]
    name   = random.choice(enemy_types)
    health = random.randint(20, 40)
    attack = random.randint(5, 12)
    return name, health, attack

def log(msg, color=TEXT):
    log_box.config(state="normal")
    log_box.insert("end", msg + "\n", color)
    log_box.see("end")
    log_box.config(state="disabled")

def clear_log():
    log_box.config(state="normal")
    log_box.delete("1.0", "end")
    log_box.config(state="disabled")

def update_stats():
    stats_label.config(
        text=(
            f"  {state['player_name']}   "
            f"HP: {state['player_health']}   "
            f"ATK: {state['player_attack']}   "
            f"Defeated: {state['enemies_defeated']}/3"
        )
    )

def show_buttons(*buttons):
    """Hide all action buttons then show the requested ones."""
    for btn in all_buttons:
        btn.pack_forget()
    for btn in buttons:
        btn.pack(side="left", padx=6, pady=8)

# ── screens ───────────────────────────────────────────────────────────────────
def show_name_screen():
    clear_log()
    state["screen"] = "name"
    log("╔══════════════════════════════╗", ACCENT)
    log("║      DUNGEON ADVENTURE       ║", ACCENT)
    log("╚══════════════════════════════╝", ACCENT)
    log("")
    log("Enter your hero's name below,", MUTED)
    log("then press  Begin Adventure.", MUTED)
    name_frame.pack(pady=6)
    show_buttons()

def begin_adventure():
    name = name_entry.get().strip()
    if not name:
        log("\n  ⚠  Please enter a name first.", YELLOW)
        return
    state["player_name"]      = name
    state["player_health"]    = 100
    state["player_attack"]    = 10
    state["enemies_defeated"] = 0
    name_frame.pack_forget()
    update_stats()
    show_explore_screen()

def show_explore_screen():
    state["screen"] = "explore"
    clear_log()
    log(f"You are exploring the dungeon, {state['player_name']}...", TEXT)
    log("")
    log("What will you do?", MUTED)
    show_buttons(btn_explore, btn_rest)

def do_explore():
    event = random.randint(1, 2)
    if event == 1:
        start_battle()
    else:
        log("")
        log("You wander the corridors... nothing happens.", MUTED)

def do_rest():
    heal = random.randint(5, 15)
    state["player_health"] = min(100, state["player_health"] + heal)
    update_stats()
    log("")
    log(f"You rest for a moment and recover {heal} HP.", GREEN)

# ── battle ────────────────────────────────────────────────────────────────────
def start_battle():
    name, hp, atk = generate_enemy()
    state["enemy_name"]   = name
    state["enemy_health"] = hp
    state["enemy_attack"] = atk
    state["screen"]       = "battle"
    clear_log()
    log(f"⚔  A wild {name} appears!", ACCENT)
    log(f"   {name} — HP: {hp}  ATK: {atk}", MUTED)
    log("")
    print_battle_status()
    show_buttons(btn_fight, btn_run)

def print_battle_status():
    log(f"Your HP : {state['player_health']}", GREEN)
    log(f"{state['enemy_name']} HP : {state['enemy_health']}", ACCENT)
    log("")

def do_fight():
    enemy = state["enemy_name"]

    # player attacks
    dmg = random.randint(5, state["player_attack"])
    state["enemy_health"] -= dmg
    log(f"You strike the {enemy} for {dmg} damage!", GREEN)

    if state["enemy_health"] <= 0:
        log(f"You defeated the {enemy}!", YELLOW)
        state["enemies_defeated"] += 1
        update_stats()
        if state["enemies_defeated"] >= 3:
            show_win_screen()
        else:
            log("")
            show_explore_screen()
        return

    # enemy attacks back
    dmg = random.randint(3, state["enemy_attack"])
    state["player_health"] -= dmg
    log(f"The {enemy} hits you for {dmg} damage!", ACCENT)
    update_stats()

    if state["player_health"] <= 0:
        show_gameover_screen()
        return

    log("")
    print_battle_status()

def do_run():
    enemy = state["enemy_name"]
    if random.randint(1, 2) == 1:
        log("You escaped successfully!", GREEN)
        log("")
        show_explore_screen()
    else:
        log("You failed to escape!", ACCENT)
        dmg = random.randint(3, state["enemy_attack"])
        state["player_health"] -= dmg
        log(f"The {enemy} hits you for {dmg} damage!", ACCENT)
        update_stats()
        if state["player_health"] <= 0:
            show_gameover_screen()
            return
        log("")
        print_battle_status()

# ── end screens ───────────────────────────────────────────────────────────────
def show_gameover_screen():
    state["screen"] = "gameover"
    clear_log()
    log("╔══════════════════════════════╗", ACCENT)
    log("║          GAME  OVER          ║", ACCENT)
    log("╚══════════════════════════════╝", ACCENT)
    log("")
    log(f"{state['player_name']}, you have been defeated.", MUTED)
    log(f"Enemies defeated: {state['enemies_defeated']}", MUTED)
    show_buttons(btn_restart)

def show_win_screen():
    state["screen"] = "win"
    clear_log()
    log("╔══════════════════════════════╗", YELLOW)
    log("║         YOU  WIN!            ║", YELLOW)
    log("╚══════════════════════════════╝", YELLOW)
    log("")
    log(f"Congratulations, {state['player_name']}!", TEXT)
    log("You defeated 3 enemies and saved the dungeon!", GREEN)
    show_buttons(btn_restart)

def do_restart():
    state["player_name"] = ""
    name_entry.delete(0, "end")
    show_name_screen()

# ── build UI ──────────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("Dungeon Adventure")
root.configure(bg=BG)
root.resizable(False, False)

# title bar
title_bar = tk.Frame(root, bg=ACCENT, pady=6)
title_bar.pack(fill="x")
tk.Label(title_bar, text="⚔  DUNGEON ADVENTURE", font=FONT_BIG,
         bg=ACCENT, fg=BG).pack()

# stats bar
stats_label = tk.Label(root, text="", font=FONT_MAIN,
                       bg=PANEL, fg=GREEN, anchor="w", padx=8, pady=4)
stats_label.pack(fill="x")

# log / output area
log_frame = tk.Frame(root, bg=BG, padx=12, pady=8)
log_frame.pack(fill="both", expand=True)

log_box = tk.Text(log_frame, width=52, height=18, font=FONT_MAIN,
                  bg=PANEL, fg=TEXT, insertbackground=TEXT,
                  relief="flat", state="disabled", wrap="word",
                  padx=10, pady=10)
log_box.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(log_frame, command=log_box.yview, bg=PANEL)
scrollbar.pack(side="right", fill="y")
log_box.config(yscrollcommand=scrollbar.set)

# text color tags
for tag, color in [("normal", TEXT), (TEXT, TEXT), (ACCENT, ACCENT),
                   (GREEN, GREEN), (YELLOW, YELLOW), (MUTED, MUTED)]:
    log_box.tag_config(tag, foreground=color)

# name entry row
name_frame = tk.Frame(root, bg=BG)
tk.Label(name_frame, text="Name:", font=FONT_MAIN,
         bg=BG, fg=MUTED).pack(side="left", padx=(0, 6))
name_entry = tk.Entry(name_frame, font=FONT_MAIN, width=20,
                      bg=BTN_BG, fg=TEXT, insertbackground=TEXT,
                      relief="flat")
name_entry.pack(side="left")
tk.Button(name_frame, text="Begin Adventure →", font=FONT_MAIN,
          bg=ACCENT, fg=BG, activebackground=BTN_HOV,
          relief="flat", padx=10, command=begin_adventure).pack(side="left", padx=8)

# action buttons
btn_frame = tk.Frame(root, bg=BG)
btn_frame.pack(fill="x", padx=12)

def make_btn(text, cmd):
    return tk.Button(btn_frame, text=text, font=FONT_MAIN,
                     bg=BTN_BG, fg=TEXT, activebackground=BTN_HOV,
                     activeforeground=BG, relief="flat",
                     padx=14, pady=6, command=cmd)

btn_explore = make_btn("Explore",  do_explore)
btn_rest    = make_btn("Rest",     do_rest)
btn_fight   = make_btn("⚔ Fight",  do_fight)
btn_run     = make_btn("↩ Run",    do_run)
btn_restart = make_btn("Play Again", do_restart)

all_buttons = [btn_explore, btn_rest, btn_fight, btn_run, btn_restart]

# ── start ─────────────────────────────────────────────────────────────────────
show_name_screen()
root.mainloop()