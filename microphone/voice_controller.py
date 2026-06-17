from actions.action_executor import ActionExecutor

class VoiceController:
    def __init__(self):
        self.executor = ActionExecutor()

    def handle(self, command):
        if command == "volume_up":
            self.executor.volume_up()
        elif command == "volume_down":
            self.executor.volume_down()
        elif command == "stop":
            self.executor.play_pause()
        elif command == "continue":
            self.executor.play_pause()
        elif command == "scroll_up":
            self.executor.scroll(1)
        elif command == "scroll_down":
            self.executor.scroll(-1)
