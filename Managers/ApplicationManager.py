from pywinauto.application import Application

class ApplicationManager:
    def __init__(self, title="", file_path="") -> None:
        self.title = title
        self.file_path = file_path

    def connect_app_with_title_and_return_app(self):
        app = Application(backend='uia').connect(title=self.title, timeout=100)
        return app

    def start_with_file_path(self):
        Application(backend="uia").start(
        self.file_path
    )

    def close(self):
        self.connect_app_with_title().kill()