import tkinter as tk
from tkinter import messagebox
import turtle


root = tk.Tk()
root.title("L-System Fractal Architect")
root.geometry("1000x800")

left_frame = tk.Frame(root, padx=10, pady=10)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

right_frame = tk.Frame(root, padx=10, pady=10)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

title_label = tk.Label(left_frame, text="Configuration", font=("Helvetica", 16, "bold"))
title_label.pack(pady=(0, 20))

axiom_label = tk.Label(left_frame, text="Axiom (start string)")
axiom_label.pack(anchor="w")
axiom_entry = tk.Entry(left_frame, width=30)
axiom_entry.insert(0, "F")
axiom_entry.pack(fill="x", pady=(0, 10))

rules_label = tk.Label(left_frame, text="Rules (Symbol:Replacement)")
rules_label.pack(anchor="w")
rules_hint = tk.Label(left_frame, text="One per line (F:F+F-F-F+F)", font=("Arial", 8))
rules_hint.pack(anchor="w")
rules_text = tk.Text(left_frame, height=8, width=30)
rules_text.insert("1.0", "F:F+F-F-F+F")
rules_text.pack(fill="x", pady=(0, 10))

angle_label = tk.Label(left_frame, text="Angle (degrees)")
angle_label.pack(anchor="w")
angle_entry = tk.Entry(left_frame, width=30)
angle_entry.insert(0, "90")
angle_entry.pack(fill="x", pady=(0, 10))

iter_label = tk.Label(left_frame, text="Iterations")
iter_label.pack(anchor="w")
iter_entry = tk.Entry(left_frame, width=30)
iter_entry.insert(0, "4")
iter_entry.pack(fill="x", pady=(0, 10))

length_label = tk.Label(left_frame, text="Step length")
length_label.pack(anchor="w")
length_entry = tk.Entry(left_frame, width=30)
length_entry.insert(0, "5")
length_entry.pack(fill="x", pady=(0, 20))

canvas = tk.Canvas(right_frame, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
screen.bgcolor("white")
pen = turtle.RawTurtle(screen)
pen.speed(0)
pen.hideturtle()


def read_rules():
    text = rules_text.get("1.0", tk.END).strip()
    lines = text.split("\n")
    rules = {}
    for line in lines:
        if ":" in line:
            left, right = line.split(":", 1)
            rules[left.strip()] = right.strip()
    return rules


def lindenmayer_translation(rules, word):
    new_word = ""
    for symbol in word:
        if symbol in rules:
            new_word += rules[symbol]
        else:
            new_word += symbol
    return new_word


def generate_word():
    axiom = axiom_entry.get().strip()
    rules = read_rules()
    try:
        n = int(iter_entry.get().strip())
    except ValueError:
        messagebox.showerror("Error", "Iterations must be an integer.")
        return axiom

    word = axiom
    for _ in range(n):
        word = lindenmayer_translation(rules, word)
    return word


def draw_l_system():
    try:
        angle = float(angle_entry.get().strip())
        length = float(length_entry.get().strip())
    except ValueError:
        messagebox.showerror("Error", "Angle and length must be numbers.")
        return

    instructions = generate_word()

    pen.reset()
    pen.hideturtle()
    pen.speed(0)
    screen.bgcolor("white")

    if "[" in instructions:
        pen.penup()
        pen.setpos(0, -250)
        pen.setheading(90)
        pen.pendown()
    else:
        pen.penup()
        pen.setpos(-200, 0)
        pen.setheading(0)
        pen.pendown()

    state_stack = []
    colors = ["#2E8B57", "#228B22", "#006400", "#8B4513", "#A0522D"]

    for symbol in instructions:
        if symbol == "F":
            depth = len(state_stack)
            color_index = depth % len(colors)
            pen.pencolor(colors[color_index])
            pen.forward(length)
        elif symbol == "+":
            pen.right(angle)
        elif symbol == "-":
            pen.left(angle)
        elif symbol == "[":
            pos = pen.pos()
            heading = pen.heading()
            state_stack.append((pos, heading))
        elif symbol == "]":
            if state_stack:
                pos, heading = state_stack.pop()
                pen.penup()
                pen.setpos(pos)
                pen.setheading(heading)
                pen.pendown()


def clear_canvas():
    pen.clear()
    pen.reset()
    pen.hideturtle()


def load_koch():
    axiom_entry.delete(0, tk.END)
    axiom_entry.insert(0, "F")
    rules_text.delete("1.0", tk.END)
    rules_text.insert("1.0", "F:F+F-F-F+F")
    angle_entry.delete(0, tk.END)
    angle_entry.insert(0, "90")
    iter_entry.delete(0, tk.END)
    iter_entry.insert(0, "3")
    length_entry.delete(0, tk.END)
    length_entry.insert(0, "5")


def load_dragon():
    axiom_entry.delete(0, tk.END)
    axiom_entry.insert(0, "FX")
    rules_text.delete("1.0", tk.END)
    rules_text.insert("1.0", "X:X+YF+\nY:-FX-Y")
    angle_entry.delete(0, tk.END)
    angle_entry.insert(0, "90")
    iter_entry.delete(0, tk.END)
    iter_entry.insert(0, "10")
    length_entry.delete(0, tk.END)
    length_entry.insert(0, "5")


def load_plant():
    axiom_entry.delete(0, tk.END)
    axiom_entry.insert(0, "X")
    rules_text.delete("1.0", tk.END)
    rules_text.insert("1.0", "F:FF\nX:F+[[X]-X]-F[-FX]+X")
    angle_entry.delete(0, tk.END)
    angle_entry.insert(0, "25")
    iter_entry.delete(0, tk.END)
    iter_entry.insert(0, "4")
    length_entry.delete(0, tk.END)
    length_entry.insert(0, "5")


generate_button = tk.Button(left_frame, text="Generate Fractal", command=draw_l_system)
generate_button.pack(fill="x", pady=(0, 10))

clear_button = tk.Button(left_frame, text="Clear Canvas", command=clear_canvas)
clear_button.pack(fill="x", pady=(0, 20))

presets_label = tk.Label(left_frame, text="Presets", font=("Helvetica", 12, "bold"))
presets_label.pack(anchor="w")

koch_button = tk.Button(left_frame, text="Koch Snowflake", command=load_koch)
koch_button.pack(fill="x", pady=2)

dragon_button = tk.Button(left_frame, text="Dragon Curve", command=load_dragon)
dragon_button.pack(fill="x", pady=2)

plant_button = tk.Button(left_frame, text="Fractal Plant", command=load_plant)
plant_button.pack(fill="x", pady=2)


if __name__ == "__main__":
    root.mainloop()
