from pywinauto.application import Application

app = Application(backend='uia').connect(title='YordamBT s.19.2 - Sakarya Uygulamalı Bilimler Üniversitesi - KTP338', timeout=100)
app.kill()