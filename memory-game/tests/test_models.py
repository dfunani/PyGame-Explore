from models.colors import Colors
from models.shapes import Shapes
from models.players import Mouse

def test_colors():
    assert Colors.BLACK.value == (0, 0, 0)
    assert Colors.WHITE.value == (255, 255, 255)

def test_shapes():
    assert Shapes.BLUE_CIRCLE.value == "🔵"
    assert Shapes.RED_SQUARE.value == "🟥"

def test_mouse():
    mouse = Mouse(10, 20)
    assert mouse.x == 10
    assert mouse.y == 20