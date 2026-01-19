# L-System Fractal Architect

A simple Python app to play with L-Systems (Lindenmayer Systems).
It uses `tkinter` for the window and `turtle` for drawing.
The code is written in a very direct way, with plain functions and a few global variables.

Main file: `L_system/main.py`

## Tech Stack
- Python 3.x
- Standard library only:
  - `tkinter`
  - `turtle`

## What you can do
- Change the starting string (axiom).
- Add or edit rules.
- Change angle, number of iterations and step length.
- Draw different fractals with one click.
- Use three ready-made presets:
  - Koch Snowflake
  - Dragon Curve
  - Fractal Plant

## Variables used in the code

These are the most important variables and what they mean:

- `axiom_entry`  
  Text box where you type the starting string. Example: `F` or `FX`.

- `rules_text`  
  Multi-line text box where each line is one rule, written as  
  `Symbol:Replacement`  
  Example:  
  `F:F+F-F-F+F`

- `angle_entry`  
  Text box for the angle in degrees. This is how much the turtle turns for `+` and `-`.

- `iter_entry`  
  Text box for the number of iterations (how many times we expand the word).

- `length_entry`  
  Text box for how far the turtle moves when it sees `F`.

- `canvas`  
  Tkinter canvas that holds the turtle drawing.

- `screen` and `pen`  
  Objects from `turtle`.  
  `screen` is the drawing area, `pen` is the turtle that moves.

- `state_stack`  
  A Python list used as a stack for branching.  
  When we see `[` we save the turtle position and heading.  
  When we see `]` we restore the last saved state.

## Commands in the L-system string

The final word (after all iterations) is read one character at a time:

- `F` – move forward by `length_entry` while drawing a line.  
- `+` – turn right by `angle_entry` degrees.  
- `-` – turn left by `angle_entry` degrees.  
- `[` – push current turtle state `(position, heading)` onto `state_stack`.  
- `]` – pop the last state from `state_stack` and move the turtle there.

The color of the line changes with the depth of the stack.
Deeper branches use different colors, which makes a simple gradient effect.

## How to run

1. Make sure Python 3 is installed.
2. Open a terminal in the project folder.
3. Run:

```bash
cd L_system
python main.py
```

This will open a window with controls on the left and the drawing area on the right.

## How to use the app

1. Set the **Axiom**.  
   For example:
   - `F` for Koch-like shapes.
   - `FX` for the dragon curve.
   - `X` for the plant.

2. Write **Rules**.  
   Each line is one rule:
   - Koch:  
     `F:F+F-F-F+F`
   - Dragon:  
     `X:X+YF+`  
     `Y:-FX-Y`
   - Plant:  
     `F:FF`  
     `X:F+[[X]-X]-F[-FX]+X`

3. Set **Angle**, **Iterations**, and **Step length**.  
   Start with low iterations (3–5). Large iterations create very long strings.

4. Click **Generate Fractal**.  
   The turtle will draw the image on the right.

5. Click **Clear Canvas** to reset the drawing area.

6. Use **Koch Snowflake**, **Dragon Curve**, or **Fractal Plant** buttons  
   to quickly load example settings.

## How the code works (simple view)

- `read_rules()`  
  Reads the text from `rules_text` and builds a Python dictionary  
  like `{"F": "F+F-F-F+F"}`.

- `lindenmayer_translation(rules, word)`  
  Creates a new string by going through each symbol in `word` and replacing it  
  with `rules[symbol]` if there is a rule, or leaving it as-is otherwise.

- `generate_word()`  
  Starts from the axiom and calls `lindenmayer_translation` `n` times,  
  where `n` is the number of iterations.

- `draw_l_system()`  
  Reads the final word and moves the turtle according to the commands  
  `F`, `+`, `-`, `[`, and `]`.
