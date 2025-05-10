import tkinter as tk
import random

# List of 100 random words for Hangman game
words = [
    "Elephant", "Rocket", "Gorilla", "Banana", "Jungle", "Keyboard", "Mountain", 
    "Computer", "Pizza", "Monkey", "Laptop", "Science", "Planet", "Galaxy", "Ocean", 
    "Sunshine", "Pineapple", "Treehouse", "Adventure", "Wilderness", "Coding", 
    "Technology", "Python", "Linux", "Hacker", "Artificial", "Intelligence", "Software", 
    "Algorithm", "Electricity", "Physics", "Chemistry", "Mathematics", "Universe", 
    "Galaxy", "Orbit", "Space", "Physics", "Cloud", "Network", "Engine", "Rocket", 
    "Program", "Hardware", "Artificial", "Robot", "Quantum", "Bioengineering", "Solar", 
    "Ecology", "Environment", "Design", "Innovation", "Education", "Astronaut", 
    "Astronomy", "Explorer", "Telescope", "Research", "Technician", "Spacecraft", 
    "Courage", "Fearless", "Mountain", "Climbing", "Forest", "Survival", "Journey", 
    "Oxygen", "Sunlight", "Adventure", "Explorer", "Timber", "Wilderness", "Creature", 
    "Camping", "Hiking", "Survivalist", "Backpacking", "Discovery", "Nightfall", 
    "Creativity", "Risk", "Vision", "Determination", "Persistence", "Optimism", 
    "Bravery", "Loyalty", "Sustainability", "Equilibrium", "Survival", "Mushroom", 
    "Butterfly", "Caterpillar", "Fire", "Water", "Wind", "Rock", "Bees", "Birds", 
    "Animals", "Galaxy", "Satellite", "Communication", "Wifi", "Radio", "Wi-Fi", 
    "Signal", "Hyperloop", "Energy", "Motivation"
]

# Hangman game logic
class HangmanGame:
    def __init__(self):
        self.word = random.choice(words).lower()
        self.guesses = []
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6
    
    def guess(self, letter):
        if letter in self.guesses:
            return False
        self.guesses.append(letter)
        if letter not in self.word:
            self.incorrect_guesses += 1
        return True

    def get_display_word(self):
        return ''.join([letter if letter in self.guesses else '_' for letter in self.word])

    def is_game_over(self):
        return self.incorrect_guesses >= self.max_incorrect_guesses or self.is_word_guessed()

    def is_word_guessed(self):
        return all([letter in self.guesses for letter in self.word])

    def get_incorrect_guesses(self):
        return self.incorrect_guesses

# Application window for Ape OS
class ApeOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Ape OS")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        # Sidebar Frame for Apps
        self.sidebar = tk.Frame(self.root, width=150, bg="#5a3d2f")
        self.sidebar.pack(side="left", fill="y")
        
        tk.Label(self.sidebar, text="Ape OS", bg="#5a3d2f", fg="white", font=("Arial", 16)).pack(pady=20)

        # Adding buttons to the sidebar
        self.create_sidebar_button("Hangman Game", self.launch_hangman_game)

        # Main display area for the selected app
        self.main_display = tk.Frame(self.root, bg="black")
        self.main_display.pack(side="right", fill="both", expand=True)

    def create_sidebar_button(self, text, command):
        button = tk.Button(self.sidebar, text=text, bg="#5a3d2f", fg="white", font=("Arial", 12), command=command)
        button.pack(pady=10, fill="x")

    def launch_hangman_game(self):
        self.main_display.destroy()
        self.main_display = tk.Frame(self.root, bg="black")
        self.main_display.pack(side="right", fill="both", expand=True)
        game_window = tk.Frame(self.main_display, bg="black")
        game_window.pack(padx=10, pady=10, expand=True)

        # Initialize hangman game
        self.game = HangmanGame()
        self.display_word = tk.Label(game_window, text=self.game.get_display_word(), font=("Courier", 24), bg="black", fg="white")
        self.display_word.pack(pady=20)

        self.guess_input = tk.Entry(game_window, font=("Courier", 20))
        self.guess_input.pack(pady=20)

        self.guess_button = tk.Button(game_window, text="Guess", command=self.make_guess, font=("Arial", 14))
        self.guess_button.pack(pady=10)

        self.incorrect_guesses_label = tk.Label(game_window, text="Incorrect Guesses: 0", font=("Arial", 14), bg="black", fg="white")
        self.incorrect_guesses_label.pack(pady=10)

    def make_guess(self):
        letter = self.guess_input.get().lower()
        if len(letter) == 1 and letter.isalpha():
            self.game.guess(letter)
            self.update_game_ui()
        self.guess_input.delete(0, tk.END)

    def update_game_ui(self):
        self.display_word.config(text=self.game.get_display_word())
        self.incorrect_guesses_label.config(text=f"Incorrect Guesses: {self.game.get_incorrect_guesses()}")

        if self.game.is_game_over():
            result_text = "You win!" if self.game.is_word_guessed() else "You lose!"
            result_label = tk.Label(self.main_display, text=result_text, font=("Courier", 24), bg="black", fg="white")
            result_label.pack(pady=20)
            self.guess_button.config(state="disabled")


# Main Application Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = ApeOS(root)
    root.mainloop()


