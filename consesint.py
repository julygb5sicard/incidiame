class Element:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.horizontal_alignment = HorizontalAlignment.CENTER
        self.vertical_alignment = VerticalAlignment.MIDDLE

    def set_horizontal_alignment(self, alignment):
        self.horizontal_alignment = alignment

    def set_vertical_alignment(self, alignment):
        self.vertical_alignment = alignment

    def render(self):
        # Calculate the position based on the alignment
        x = 0
        y = 0
        if self.horizontal_alignment == HorizontalAlignment.CENTER:
            x = container_width // 2 - self.width // 2
        elif self.horizontal_alignment == HorizontalAlignment.RIGHT:
            x = container_width - self.width

        if self.vertical_alignment == VerticalAlignment.MIDDLE:
            y = container_height // 2 - self.height // 2
        elif self.vertical_alignment == VerticalAlignment.BOTTOM:
            y = container_height - self.height

        # Render the element at the calculated position
        render_element(x, y, self.width, self.height)
