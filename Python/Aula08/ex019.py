# snake_tk.py
# Jogo da Cobrinha simples usando tkinter
# Salve e execute: python snake_tk.py

import tkinter as tk
import random

CELL_SIZE = 20
COLS = 30
ROWS = 20
WIDTH = CELL_SIZE * COLS
HEIGHT = CELL_SIZE * ROWS
INITIAL_SPEED = 120  # ms entre movimentos

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Cobrinha - Python (tkinter)")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.score_var = tk.StringVar()
        self.score_var.set("Score: 0")
        self.score_label = tk.Label(root, textvariable=self.score_var, font=("Arial", 14))
        self.score_label.pack()

        self.restart_button = tk.Button(root, text="Reiniciar", command=self.restart)
        self.restart_button.pack(pady=6)

        self.direction = "Right"
        self.next_direction = "Right"
        self.speed = INITIAL_SPEED
        self.running = True

        self.init_game()
        root.bind("<Key>", self.on_key)
        self.game_loop()

    def init_game(self):
        start_x = COLS // 2
        start_y = ROWS // 2
        self.snake = [(start_x - i, start_y) for i in range(3)]
        self.spawn_food()
        self.score = 0
        self.update_score()
        self.direction = "Right"
        self.next_direction = "Right"
        self.speed = INITIAL_SPEED
        self.running = True

    def restart(self):
        self.canvas.delete("all")
        self.init_game()

    def spawn_food(self):
        available = {(x, y) for x in range(COLS) for y in range(ROWS)} - set(self.snake)
        if not available:
            self.food = None
            return
        self.food = random.choice(list(available))

    def on_key(self, event):
        key = event.keysym
        opposites = {"Left":"Right", "Right":"Left", "Up":"Down", "Down":"Up"}
        mapping = {
            "Left": "Left", "a":"Left", "A":"Left",
            "Right":"Right", "d":"Right", "D":"Right",
            "Up":"Up", "w":"Up", "W":"Up",
            "Down":"Down", "s":"Down", "S":"Down"
        }
        if key in mapping:
            new_dir = mapping[key]
            if opposites.get(new_dir) != self.direction:
                self.next_direction = new_dir

    def step(self):
        if not self.running:
            return

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        if self.direction == "Left":
            head_x -= 1
        elif self.direction == "Right":
            head_x += 1
        elif self.direction == "Up":
            head_y -= 1
        elif self.direction == "Down":
            head_y += 1

        new_head = (head_x, head_y)

        if not (0 <= head_x < COLS and 0 <= head_y < ROWS):
            self.game_over()
            return

        if new_head in self.snake:
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if self.food and new_head == self.food:
            self.score += 10
            self.update_score()
            self.spawn_food()
            self.speed = max(30, int(self.speed * 0.95))
        else:
            self.snake.pop()

        self.draw()

    def update_score(self):
        self.score_var.set(f"Score: {self.score}")

    def game_over(self):
        self.running = False
        self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="red", font=("Arial", 36))
        self.canvas.create_text(WIDTH//2, HEIGHT//2 + 40, text="Pressione Reiniciar", fill="white", font=("Arial", 16))

    def draw(self):
        self.canvas.delete("all")
        if self.food:
            x, y = self.food
            self.draw_cell(x, y, fill="red")
        for i, (x, y) in enumerate(self.snake):
            if i == 0:
                self.draw_cell(x, y, fill="lime", outline="white")
            else:
                self.draw_cell(x, y, fill="green")

    def draw_cell(self, cx, cy, fill="white", outline=""):
        x1 = cx * CELL_SIZE
        y1 = cy * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline)

    def game_loop(self):
        self.step()
        self.root.after(self.speed, self.game_loop)


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
