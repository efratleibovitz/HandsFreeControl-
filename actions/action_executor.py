import pyautogui

class ActionExecutor:
    def __init__(self):
        pass

    def set_volume(self, percent):
        if percent > 50:
            pyautogui.press('volumeup')
        elif percent < 20:
            pyautogui.press('volumedown')

    def volume_up(self, steps=5):
        for _ in range(steps):
            pyautogui.press('volumeup')

    def volume_down(self, steps=5):
        for _ in range(steps):
            pyautogui.press('volumedown')

    def play_pause(self):
        pyautogui.press('playpause')

    def scroll(self, direction):
        # direction: 1 = up, -1 = down
        pyautogui.scroll(direction * 15)
