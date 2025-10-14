# styles.py

class Styles:
    BOARD_BACKGROUND_COLOR = "#BBADA0"
    TILE_BACKGROUND_COLOR = {
        2: "#EEE4DA",
        4: "#EDE0C8",
        8: "#F2B179",
        16: "#F59563",
        32: "#F67C5F",
        64: "#F67C5F",
        128: "#EDCF72",
        256: "#EDCC61",
        512: "#EDC850",
        1024: "#EDC53F",
        2048: "#EDC22E",
    }
    TILE_TEXT_COLOR = {
        2: "#776E65",
        4: "#776E65",
        8: "#F9F6F2",
        16: "#F9F6F2",
        32: "#F9F6F2",
        64: "#F9F6F2",
        128: "#F9F6F2",
        256: "#F9F6F2",
        512: "#F9F6F2",
        1024: "#F9F6F2",
        2048: "#F9F6F2",
    }
    TILE_FONT_SIZE = 40
    TILE_PADDING = 10
    BOARD_SIZE = 400
    TILE_SIZE = (BOARD_SIZE - (TILE_PADDING * 5)) // 4  # Assuming a 4x4 board
    ANIMATION_DURATION = 0.1

    @staticmethod
    def get_tile_style(value):
        return {
            "background_color": Styles.TILE_BACKGROUND_COLOR.get(value, "#CDC1B4"),
            "text_color": Styles.TILE_TEXT_COLOR.get(value, "#776E65"),
            "font_size": Styles.TILE_FONT_SIZE,
            "padding": Styles.TILE_PADDING,
        }