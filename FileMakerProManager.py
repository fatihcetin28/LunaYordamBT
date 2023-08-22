from ApplicationManager import ApplicationManager as AM
from time import sleep

file_path = r"C:\Program Files\FileMaker\FileMaker Pro 19\FileMaker Pro.exe"
title = "FileMaker Pro"

app = AM(title,file_path)

class FileMakerProManager:

    def start(self):
        app.start_with_file_path()

    def connect_with_title_if_open_and_return(self):
        return app.connect_app_with_title_and_return_app()
    
    def close(self):
        app.close()

    def ClickYordamBTAfterFileMakerStarted(self):
        app = self.connect_with_title_if_open_and_return()
        yordamBT_button = app.FileMakerPro.child_window(
            title="YordamBT", control_type="ListItem"
        ).wrapper_object()
        yordamBT_button.double_click_input()

    def LoginYordamBT(self):
        app = self.connect_with_title_if_open_and_return()
        passInput = app.FileMakerPro.child_window(
            auto_id="passwordBox", control_type="Edit"
        ).wrapper_object()
        passInput.type_keys("akyazimyo")
        sleep(0.5)
        signInButton = app.FileMakerPro.child_window(
            title="Sign in", auto_id="IDSIGNIN", control_type="Button"
        ).wrapper_object()
        signInButton.click()