# Sürecine göre toplanmış metotlar

Buradaki modüller yordamı aç, ödünç ver, iade al süreçlerinde kullanılan metotların ayrı ayrı toplanmasıyla oluşturuldu.

Bunlar daha sonra Runnable modüllerde sıraya dizilip aralarına sleep metoduyla bekleme süreleri konulmuştur.

## Mevcut Modüller
* Açılış metotları
* Ödünç ver metotları
* İade al metotları

### Metotlar ve Açıklamaları
* Açılış Metotları
    * StartFileMaker

        FileMaker programını pywinauto-application sınıfını kullanarak açar.

        FileMaker programının dizindeki adresini kullanır, bu dosya yolu Data içindeki strings modülünde depolanmıştır.
    
    * ConnectFileMakerandReturnApp

        Gene pywinauto-application sınıfını kullanarak açılmış olan filemaker pro uygulamasına bağlanır ve uygulamayı döndürür.

        FileMaker Pro penceresinin başlığı kullanılarak bağlanılır. Bu veri Data klasörü içinde strings modülünde depolanmıştır.

        Döndürülen app uygulaması daha sonra Yordamı açmak ve login olmak için kullanılacaktır.

        Burada filemaker pro düğmelerinin ve input boxlarının id leriyle işlem yapılır.

        Yordama login olduktan sonra resim tıklama yoluyla navigasyon sağlanır.
    
    * ClickYordamBTAfterFileMakerStarted

        FileMaker Pro açıldıktan sonraki pencerede Yordam ı seçer.

        Bir önceki metotu kullanır ve dönen app uygulamasıyla işlem yapar.

    * LoginYordamBT

        YordamBT seçildikten sonra gelen sifre inputubu doldurur ve oturum açar.

    * ClickUyeOduncIslemleriImage ve ClickOduncIslemleriImage

        Oturum açıldıktan sonra soldaki liste menüden üye ödünç işlemleri ve ödünç işlemlerini seçerek, Yordamı ödünç modunda açarlar. Bunlar YordamIslemPencereAc metotunda beraber kullanılır.

    * MaximizeActiveWindow - MinimizeActiveWindow

        İsimlerinde anlaşılacağı gibi, o an aktif olan pencereyi maximize ve minimize ederler.

        Yordamı açtıktan sonra tam ekran yapıp daha sonra minimize ederek arka plana atarlar.

        pygetwindow paketi kullanılır.

* Ödünç Modülleri

    Burada metotlara türkçe isim verilmiş.

    Akış olarak, önce kullanıcıdan tkInter paketiyle çizdirilen inputbox ile kullanıcı no alır, sonra demirbaş no alır.

    Daha sonra yordamı tam ekran yaptıktan sonra ödünç ver düğmesini tıklar sırayla kullanıcı numarasını ve demirbaş numarasını girerek işlemi bitimeye çalışır.

    Sonunda da başarılı olursa onun dönüşünü yapar.

    Ve en son ekranda kendiliğinden açılan input boxta vazgeç düğmesini tıklar ve yordamı minimize ederek arka plana atar.

    Bu akışta kullanıcı numarasını veya demirbaş numarasını girdikten sonra, yordam bir uyarı verirse bu uyarıyı handleUyariOdunc metoduyla tespit eder, bilgilendirmeyi yaparak yordamı minimize eder.

* İade Al Modülleri

    Burada da metotlara türkçe isimler verilmiş, kullanıcıdan önce demirbaş numarasını alır, sonra yordam tam ekran olduktan sonra iade al düğmesini tıklar, gelen inputbox a demirbaş noyu yazar ve işlemi bitirmeye çalışır.




