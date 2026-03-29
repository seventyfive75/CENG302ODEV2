# CENG302ODEV2

Bu proje, Python programlama ve modüler tasarım pratiklerini göstermek amacıyla hazırlanmış küçük bir çalışma dizinidir. Her bir modül, belirli bir işlevi yerine getirir ve aynı zamanda yanlış uygulama örnekleri ile güvenlik zafiyetleri açısından incelenebilecek arayüzler sağlar.

## Dosyalar

- `spaghetti_logic.py`
  - Karmaşık veya kötü yapılandırılmış mantık içeren bir örnek dosyasıdır.
  - Proje kapsamında daha açıklayıcı ve okunabilir kod yazmanın önemini göstermek için kullanılır.

- `failing_calculator.py`
  - Basit bir hesaplama modülüdür.
  - Girilen değerlerden vergi sonrası toplamları hesaplar, çıktıyı biçimler ve sonuçları bir log dosyasına yazar.
  - Veri işleme, yan etkiler ve hata ayıklamada dikkat edilmesi gereken noktaları vurgular.

- `secret_leak.py`
  - Kod içinde doğrudan gizli anahtar saklayan bir örnek içerir.
  - Bu dosya, hardcoded secret kullanımının neden tehlikeli olduğunu gösterir ve güvenli konfigürasyon yönetiminin önemini ortaya koyar.

- `mystery_module.py`
  - İkinci derece bir denklemin köklerini hesaplayan yardımcı bir modüldür.
  - `fn_x(a, b, c)` fonksiyonu, ax² + bx + c = 0 formundaki denklemler için diskiriminantı kontrol eder ve gerçek kökler varsa çözümü döner.
  - Negatif diskriminant durumunda `None` döndürerek kök olmadığını ifade eder.

## Kullanım

Her bir dosya, kendi amaçları doğrultusunda ayrı ayrı çalıştırılabilir. `failing_calculator.py` gibi bir modül, veri işleme ve loglama örneklerini içerirken, `mystery_module.py` matematiksel çözümlemeye odaklanır.

## Güvenlik ve kalite notları

- `secret_leak.py` dosyasında gizli anahtarın doğrudan kodda tutulması güvenlik tehdididir.
- `spaghetti_logic.py` yapısı, okunabilirlik ve bakım maliyeti açısından kötü bir örnektir.
- Proje, kod kalitesinin ve güvenliğinin nasıl geliştirilebileceğine yönelik bir çalışma ortamı sağlar.
