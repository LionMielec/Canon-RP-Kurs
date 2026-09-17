# Rejestr decyzji

Data bazowa: 17.09.2026. Źródło: rozmowa „Planowanie kursu Canon RP” i polecenie rozpoczęcia dokumentacji oraz repo. Status odróżnia zaakceptowaną koncepcję od propozycji asystenta.

## Ustalone

| ID | Ustalenie | Uzasadnienie |
| --- | --- | --- |
| D-01 | Prywatny, niekomercyjny kurs dla Ani na Canon EOS RP | Konkretny odbiorca i egzemplarz |
| D-02 | Nauka fotografii i aparatu w jednym kursie | Działanie ma prowadzić do efektu na zdjęciu |
| D-03 | Rozwój od podstaw przez średni do zaawansowanego poziomu | Kurs ma rosnąć z umiejętnościami Ani |
| D-04 | Zwykły język na każdym poziomie | Żargon nie ma odstraszać ani utrudniać nauki |
| D-05 | Cel → aparat → ustawienie → efekt → ćwiczenie | Nauka przez praktykę |
| D-06 | Prawdziwe polskie menu i zdjęcia egzemplarza | Zgodność instrukcji z tym, co widzi Ania |
| D-07 | Animacja prowadzi po aparacie; menu pozostaje autentyczne | Czytelność i poprawność instruktażu |
| D-08 | Osobny moduł „Mój nauczyciel / Analiza mojego zdjęcia” | Informacja zwrotna na własnych pracach |
| D-09 | Dane zdjęcia odczytywane programowo; brak danych nie jest zgadywany | Uczciwa analiza i rozróżnienie faktów od hipotez |
| D-10 | Krótka informacja zwrotna bez punktacji, najwyżej dwa zalecenia | Pomoc bez przytłaczania początkującej |
| D-11 | Osobne prywatne repo Canon-RP-Kurs, najpierw dokumentacja | Zachowanie decyzji przed implementacją |
| D-12 | Klucz API poza klientem i GitHubem; osobny projekt i budżet API | Bezpieczeństwo i kontrola kosztów |
| D-13 | Na początek główne strony menu, Q, ekran fotografowania i firmware | Materiały potrzebne do planowania bez zbierania setek ekranów |

## Kierunki robocze i decyzje otwarte

| ID | Temat | Status |
| --- | --- | --- |
| P-01 | WWW/PWA zamiast aplikacji App Store | Preferowany kierunek; technologia i zakres offline nieustalone |
| P-02 | Higgsfield do krótkich klipów | Rozważane narzędzie; brak prób i zakupu w tym etapie |
| P-03 | GPT-6 Astra jako model referencyjny nauczyciela | Ostatnia propozycja z rozmowy; przed integracją ocena jakości, dostępności i kosztu |
| P-04 | Saldo 5–10 USD i wyłączone automatyczne doładowanie | Przykład budżetu; nie jest zgodą na płatność ani zmianę konta |
| P-05 | Lista i kolejność lekcji Poziomu 1 | Do opracowania i akceptacji |
| P-06 | Obiektyw, firmware i dokładne polskie etykiety menu | Oczekuje na materiały egzemplarza |
| P-07 | Hosting, logowanie, baza, synchronizacja postępów, retencja zdjęć | Do ustalenia przed implementacją |

## Później

Specjalizacje jako kolejny poziom, model aparatu obracany palcem, osiągnięcia, adaptacyjne ćwiczenia, niezależny nauczyciel fotografii i ewentualna optymalizacja modeli. Zachowanie pomysłu nie oznacza zatwierdzenia jego implementacji.

## Doprecyzowania po przeglądzie rozmowy

- Linki do materiałów nie oznaczają pobranych plików. Początkowo nie mamy lokalnych zdjęć ani instrukcji.
- Liczby stron menu są roboczym planem zbierania zdjęć, nie zweryfikowaną mapą egzemplarza.
- Nazwy i numery lekcji użyte w przykładach nie ustanawiają programu kursu.
- Budżet/alert API i egzekwowany twardy limit to różne ustawienia. Nawet twardy limit nie daje gwarancji rozliczenia co do centa; szczegóły w dokumencie 11.
- Kwota za 42 zdjęcia była szacunkiem, nie wynikiem pomiaru. Nie stanowi gwarancji kosztu.
- Wcześniejsza propozycja kilku modeli ustępuje prostszemu kierunkowi jednego modelu referencyjnego; wdrożenie nadal wymaga decyzji.

## Jak dopisywać decyzje

Nowy wpis zawiera datę, ID, decyzję, status, uzasadnienie i wpływ na zakres. Zmiana wcześniejszej decyzji wskazuje, który wpis zastępuje. Decyzje produktowe podejmuje użytkownik; Codex implementuje zaakceptowany etap.

## D-14 — Lokalna baza instrukcji (17.09.2026)

Na wyraźne polecenie użytkownika pobrano oryginalne PDF PL i EN do `materials/canon-official/` we właściwym repo. Pliki pozostają lokalne i ignorowane przez Git. Pochodzenie, daty i ograniczenia zapisano w rejestrze. Materiały wideo mają na razie tylko lokalny katalog i odnośnik do źródła; nie są dostępne offline. Decyzja nie obejmuje commit/push ani redystrybucji instrukcji.
