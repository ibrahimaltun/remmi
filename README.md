# logging_operations

### https://realpython.com/python-logging/

logging işlemi veya loglama, yani günlüğe kaydetme, bir programın akışını daha iyi anlamak ve alınabilecek hataların kodun neresinde olduğu öğrenmek veya kod akışında bilgilendirici bilgileri bir yerde toplayarak daha sonra program hakkında ya da programı kullananlar hakkında analizler yaparak pazarlama stratejileri geliştirmek için kullanılan bir python kitaplığıdır.

standartlaşmış 5 log seviyesi vardır:
    DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL
    {soldan sağa artan önem seviyesine göre}
    Bu seviyelerin herbirisi logging altından bir fonksiyona denk gelir.

* Temel Yapılandırma Ayarları

basicConfig() fonksiyonu kullanılarak basit seviyede günlüğe kaydetme süreci ayarlanabilir.

logging modulü, PEP8 stil kılavuzunu ihlal eder ve camelCase adlandırma kurallını kullanılır. Methodun adından da anlaşılacağı üzere :)
Bunun nedeni Java'daki logging aracı olan Log4j'den uyarlanmış olmasıdır. PEP8 gereksinimlerini karşılayacak şekilde değiştirilmesi geriye dönük uyumluluk sorunlarına neden olacağından herhangi bir işlem yapılmamıştır.

basicConfig için yaygın olarak kullanılan parametreler;
    
    - level: kayıt etmek istenilen log mesajları için önem seviyesinin beirlenmesinde kullanılır, bu seviye ve üstü kaydedilir, logging kitaplığının altındaki bir sabit ile atanır (örn: logging.DEBUG)

    - filename: log'ların kaydı için belirlenen bir dosya adı
    
    - filemode: Eğer filename parametresini methoda geçtiyseniz, filename'de belirlenen bu dosyanın hangi mod ile açılacağını ifade eder. Varsayılan olarak a modundandır, yani ekleme modudur.
    a öodunda verilen isimde dosya yoksa oluşturur öyle yazar.
    Eğer w modu seçilirse, filename'de verilen dosyanın açık olduğudur. Her basicConfig çağrıldığında ya da her program çağrıldığında dosya yeniden yazılacaktır.
    
    - format: log mesajlarının formatını ifade eder.

Not: basicConfig() fonksiyonu yalnızca 1 kez çağrılabilirdir. level'daki herhangi bir seviyenin fonksiyonu çağrılırsa dahili oalrak basicConfig de çağrılacaktır.

Çıktı Formatı
    - log mesajlarının nasıl basılması gerektiğini detaylandırmak isterseniz format parametresiyle bu mümkündür. Örn: eğer process id'i basmak isterseniz aşağıdaki gibi bir format yazılabilir:
    format='%(process)d-%(levelname)s-%(message)s'
    istersek bu format parametresini istediğimiz gibi şekillendirebiliriz. name, process, levelname, message, asctime gibi öğeler format parametresine eklenerek özelleştirilebilir.
    Bu öğeler LogRecord'un bir parçasıdır.

    Tüm format öğelerine https://docs.python.org/3/library/logging.html#logrecord-attributes linkinden ulaşılabilir.

    örnek format öğresi: asctime
    bu format öğesi log dosyasına tarih ve saati eklemek için kullanılır. LogRecord'un oluşma zamanını verir. Bu öğe datefmt özniteliği kullanılarak değiştirilebilir. Aynı time modülünde time.strftime() kullanılarak yapıldığı gibi.


Değişken Verilerinin Günlüğe Kayıt Edilmesi

    Çoğu durumunda uygulamamız içinden gelen dinamik bilgiye log mesajına dahil etmek isteriz. Bunu yapmak doğrudan mümkündür nasıl bir string ifadeye f"" gibi formatlama ya da %s %d gibi placeholder'lar kulanıyor isek burada da aynı yöntem ile log mesajını formatlayabiliriz. Örn;
            name = 'John'
            logging.error('%s raised an error', name)


Exception'lar İçerisinde Günlüğe Kaydetme İşlemi







to log   :          => kayıt tutmak, seyir defterine yazmak, mesafe katetmek
severity : siverıdi => önem, ciddiyet, şiddet

