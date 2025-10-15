import tkinter as tk
import time
import random

class ReactionGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Reaction Speed Game")
        self.root.geometry("400x300")
        self.root.config(bg="#1e1e1e")

        self.start_time = None
        self.waiting_to_click = False

        self.label = tk.Label(
            root, 
            text="Click 'Start' to play!", 
            font=("Arial", 16), 
            fg="white", 
            bg="#1e1e1e"
        )
        self.label.pack(pady=40)

        self.start_button = tk.Button(
            root, 
            text="Start", 
            font=("Arial", 14), 
            command=self.start_game, 
            bg="#0078d4", 
            fg="white", 
            padx=10, 
            pady=5
        )
        self.start_button.pack(pady=10)

        self.click_area = tk.Button(
            root, 
            text="Wait for Green...", 
            font=("Arial", 14), 
            bg="red", 
            fg="white", 
            width=20, 
            height=5, 
            state="disabled",
            command=self.check_reaction
        )
        self.click_area.pack(pady=20)

    def start_game(self):
        self.label.config(text="Get ready...", fg="white")
        self.start_button.config(state="disabled")
        self.click_area.config(text="Wait for Green...", bg="red", state="disabled")
        self.root.update()

        # Random delay before turning green
        delay = random.uniform(2, 5)
        self.root.after(int(delay * 1000), self.activate_click)

    def activate_click(self):
        self.click_area.config(text="CLICK NOW!", bg="green", state="normal")
        self.start_time = time.time()
        self.waiting_to_click = True

    def check_reaction(self):
        if self.waiting_to_click:
            reaction_time = time.time() - self.start_time
            self.label.config(text=f"Reaction Time: {reaction_time:.3f} seconds", fg="yellow")
            self.click_area.config(state="disabled")
            self.start_button.config(state="normal")
            self.waiting_to_click = False

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = ReactionGame(root)
    root.mainloop()
