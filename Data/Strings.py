from datetime import datetime

current_time = datetime.now().time()
formatted_time = current_time.strftime("%H%M%S")
current_date = datetime.now().date()
formatted_date = current_date.strftime("%d%m%y")
ssName = f"{formatted_date}-{formatted_time}"

#  - Configure
yordam_title = "YordamBT s.19.2 - Sakarya Uygulamalı Bilimler Üniversitesi - KTP338"

demirbasNoGir = "Lütfen Demirbaş Seri No Girdikten sonra işleme devam etmek için entera, , çıkış için ESC'ye basınız."

demirbasNoGir2 = "Lütfen Demirbaş Seri No Giriniz."

# Odunc Ver Modul

odunc_tc_no_giriniz = "Lütfen TC Kimlik No Girdikten sonra devam etmek için entera, çıkış için ESC'ye basınız."

odunc_tc_no_giriniz2 = "Lütfen TC Kimlik No Giriniz."

odunc_demirbasNoGiriniz = "Lütfen Demirbaş Seri No Girdikten sonra ödünç işlemi için entera, çıkış için ESC'ye basınız."

odunc_success = "Ödünç verme işlemi başarılı"

# Opening Modules  - Configure

file_maker_exe_path = r"C:\Program Files\FileMaker\FileMaker Pro 19\FileMaker Pro.exe"

file_maker_title = "FileMaker Pro"

# FilePaths

uyariBaslikImage = (
    r"C:\Users\SUBU\Documents\Codebas\YordamYardimBT\uyariImages\uyariBaslik.png"
)

uyariSaveFilePath = (
    rf"C:\Users\SUBU\Documents\Codebas\YordamYardimBT\uyari-{ssName}.png"
)


# İade Al Modules

iadeAL_demirbasNoGiriniz = "Lütfen Demirbaş Seri No Girdikten sonra iade alma işlemi için entera, çıkış için ESC'ye basınız."
iadeAl_demirbasNoGir2 = "Lütfen Demirbaş Seri No Giriniz."

# General
dugme_bulunamadi = "Düğme bulunamadı."

# Yordam Kullanıcı Bilgileri - Configure
yordam_kullanici_adi = "akyazimyo"
yordam_sifre = "akyazimyo"
