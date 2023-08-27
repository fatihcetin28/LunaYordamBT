from pywinauto.application import Application
from Managers.ApplicationManager import ApplicationManager
from Data.Strings import yordam_title

app = ApplicationManager(yordam_title)
app.close()

# app = Application(backend='uia').connect(title='YordamBT s.19.2 - Sakarya Uygulamalı Bilimler Üniversitesi - KTP338', timeout=100)
# app.kill()