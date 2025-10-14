class TileView:
    def __init__(self, value, position, size):
        self.value = value
        self.position = position
        self.size = size
        self.color = self.get_tile_color(value)

    def get_tile_color(self, value):
        colors = {
            2: "#eee4da",
            4: "#ede0c8",
            8: "#f2b179",
            16: "#f59563",
            32: "#f67c5f",
            64: "#f67c5f",
            128: "#f9f6f2",
            256: "#f9f6f2",
            512: "#f9f6f2",
            1024: "#f9f6f2",
            2048: "#f9f6f2",
        }
        return colors.get(value, "#cdc1b4")

    def draw(self, canvas):
        x, y = self.position
        canvas.create_rectangle(x, y, x + self.size, y + self.size, fill=self.color, outline="#776e65")
        if self.value > 0:
            canvas.create_text(x + self.size / 2, y + self.size / 2, text=str(self.value), fill="#f9f6f2", font=("Helvetica", 24, "bold"))