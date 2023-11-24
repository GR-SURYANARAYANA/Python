import os
class Style:
    def bold_start(self):
        return "\033[1m"

    def bold_end(self):
        return "\033[0m"

    def italic_start(self):
        return "\x1B[3m"

    def italic_end(self):
        return "\x1B[0m"

    def underline(self):
        return "\u0332"

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

