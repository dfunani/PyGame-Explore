# PyGame

The Pygame framework includes several modules with functions for drawing graphics, playing sounds, handling mouse input, and other things.

## Installation

```python
# Consider using a virtual environment
python3 -m pip install virtualenv
python3 -m virtualenv venv
source ./venv/bin/activate

which pip # Output *venv/bin/pip

pip install pygame
pygame --version
```

## Initialization

1. Modules - `pygame.init() -> tuple[int, int]`
2. Display - `pygame.display`
    a. `set_mode(window_size: tuple[int, int], flags: PyGameFlags, depth: int, display: int, vsync: int)`

**PLEASE NOTE:** PyGameFlags
```python
pygame.SHOWN         # window is opened in visible mode (default)
pygame.HIDDEN        # window is opened in hidden mode

pygame.FULLSCREEN    # create a Full-Screen display
pygame.RESIZABLE     # display window should be sizeable
pygame.SCALED        # resolution depends on desktop size and scale graphics

pygame.NOFRAME       # display window will have no border or controls

pygame.DOUBLEBUF     # only applicable with OPENGL
pygame.OPENGL        # create an OpenGL-Renderable display

example_flags = pygame.SHOWN | pygame.HIDDEN
```