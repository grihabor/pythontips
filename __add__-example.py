class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __add__(self, other):
        return Color(
            (self.r + other.r) // 2,
            (self.g + other.g) // 2,
            (self.b + other.b) // 2,
        )

white = Color(255, 255, 255)
black = Color(0, 0, 0)
gray = white + black
print(gray.r, gray.g, gray.b)
#|127 127 127