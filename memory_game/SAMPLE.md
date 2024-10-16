# Sample Data Structures

Below are samples of the various data blocks used in the game render.

```python
# What the Icon Layout looks like - behind the scenes 4 x 4 Board
Sample_board_data = [
    ["💧", "🧱", "🚀", "🔵"],
    ["💧", "🟨", "🟨", "🔵"],
    ["💛", "🙂", "🙂", "📌"],
    ["📌", "🧱", "🚀", "💛"],
]
```

```python
# What the Click Reveal State Layout looks like - behind the scenes
sample_board_states = [
    [False, False, False, True],
    [False, True, True, True],
    [False, True, True, False],
    [False, False, False, False],
]
```

```python
# What the Block Layout and Location looks like - behind the scenes - a Block is (x, y, w, h)
sample_board_boxes = [
    [(220, 140, 40, 40), (270, 140, 40, 40), (320, 140, 40, 40), (370, 140, 40, 40)],
    [(220, 190, 40, 40), (270, 190, 40, 40), (320, 190, 40, 40), (370, 190, 40, 40)],
    [(220, 240, 40, 40), (270, 240, 40, 40), (320, 240, 40, 40), (370, 240, 40, 40)],
    [(220, 290, 40, 40), (270, 290, 40, 40), (320, 290, 40, 40), (370, 290, 40, 40)],
]
```
