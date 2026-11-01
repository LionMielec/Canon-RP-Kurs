# L1-09 — karta wizualno-produkcyjna

Aktualne statusy materiałów: docs/16_ASSET_MANIFEST.md (D-074). Statusy poniżej są historyczne.

Stan: 01.11.2026. Dokument produkcyjny; zgodnie z D-048 jego treść nie jest widoczna w kursie.

Treść lekcji: `docs/L1-09_ROBIE_PROSTY_PORTRET.md` (brama 2, D-094). Zakres: D-093.

Karta na stronie głównej: FOTOGRAFUJĘ OSOBĘ · OKOŁO 20 MINUT.

## Kroki lekcji

| ID | Krok | Materiał |
|---|---|---|
| L1-09-S01 | Najpierw zobacz, o co chodzi | L1-09-V01 |
| L1-09-S02 | Posadź osobę przy oknie | L1-06-V02 (podpunkt 1) |
| L1-09-S03 | Ustaw F2.8 | L1-07-V03 (podpunkt 1); L1-02-V04 (podpunkt 2) |
| L1-09-S04 | Postaw punkt ostrości na bliższym oku | L1-09-V02 |
| L1-09-S05 | Ustaw ostrość i zrób zdjęcie | L1-04-V08 |
| L1-09-S06 | Sprawdź oko | L1-02-V03 |
| Ćwiczenie | Trzy portrety, jedna zmiana naraz | L1-09-V03 (przed ćwiczeniem); L1-02-V03 („Porównaj”) |
| Pomoc | Jeśli coś nie działa | L1-04-V17 („Zamiast małego punktu…”) |

## Zasady dla materiałów L1-09
- Pochodzenie każdego materiału według D-057: WŁASNE, RENDER, WOLNA LICENCJA albo CANON — DO PODMIANY.
- V01 powstaje w Higgsfield na warunkach D-050, z twarzą Ani — postać z konta Higgsfield właściciela.
- Każde płatne generowanie — dopiero po podaniu kosztu i zgodzie właściciela.
- Obraz zatwierdza właściciel przed osadzeniem.
- Kontrola zgodności z zasadami ze źródeł: cień po stronie przeciwnej do okna, ostre bliższe oko, rozmycie tła pasujące do F2.8.
- Wizerunek Ani może być publiczny (zgoda właściciela, D-094); V01 traktujemy jak inne materiały.
- Rysunki z instrukcji Canon (D-056): jak dotąd tylko lokalnie — plik kończy się na `-canon`, nigdy w publicznym repozytorium ani w `review/`.
- Materiał bez źródła nie ma zamiennika; w aplikacji stoi jawne miejsce na brakujący materiał.

## Materiały

| ID | Krok | Co dokładnie pokazuje | Źródło | Pochodzenie | Plik docelowy | Status |
|---|---|---|---|---|---|---|
| L1-09-V01 | S01 | Portret kobiety (twarz Ani) siedzącej przy oknie; światło z okna z boku, druga strona twarzy w delikatnym cieniu; głowa lekko obrócona; bliższe oko ostre, dalsze nieco mniej; tło pokoju daleko, miękko rozmyte jak przy F2.8 i obiektywie 50 mm; bez napisów i marek; naturalnie, nie jak z sesji modowej; poziomo 4:3. Pod spodem wycinek z powiększonym bliższym okiem z tego samego obrazu (bez osobnego generowania) | Higgsfield, model Nano Banana Pro; element „Chic Urban Serenity-1” (wytrenowana postać Ani) i zdjęcie twarzy Ani jako wzorzec (media 95da5ce1-f3ac-4bc0-81a7-f5046fdaf970); generacja a62de71e-2c9e-4ece-b480-e0f8ac68cc67, 01.11.2026, 2400×1792 | GENEROWANE (Higgsfield) — wizerunek Ani, zgoda na publiczne użycie (D-094); licencja do potwierdzenia przed komercjalizacją (jak D-071) | `assets/lessons/l1-09/l1-09-v01-portret.jpg`, `l1-09-v01-oko.jpg` | portret `APPROVED (D-095)`; wycinek oka `TO_PREPARE` |
| L1-09-V02 | S04 | Schemat z góry w dwóch panelach, jeden pod drugim (jak L1-08-V02, czytelniej na telefonie): „F1.8” i „F2.8”. W każdym: prosty prostokąt „aparat”, głowa osoby około 1 m od aparatu, obrócona lekko (około 20°); zaznaczone: nos, bliższe oko, dalsze oko, ucho. Jasne pole „zasięg ostrości” przechodzi przez bliższe oko, prostopadle do osi aparatu. F1.8: pole wąskie — czubek nosa tuż przed jego przednią granicą (poza polem), dalsze oko na tylnej granicy. F2.8: pole szersze — nos i oba oczy w polu, ucho poza nim. Pole sięga prawie tyle samo przed bliższym okiem co za nim. Bez liczb w centymetrach na schemacie; podpisy tylko: „aparat”, „F1.8”, „F2.8”, „zasięg ostrości”, „bliższe oko”, „dalsze oko”, „nos”, „ucho”. Wszystko, co leży poza polem zasięgu ostrości, jest oznaczone tak samo (np. nos przy F1.8, uszy w obu panelach). Styl i kolory jak L1-08-V02. | schemat SVG | WŁASNE | `assets/lessons/l1-09/l1-09-v02-blizsze-oko.svg` | `TO_DESIGN` |
| L1-09-V03 | przed ćwiczeniem | Karta „okno z boku → F2.8 → punkt na bliższym oku → zdjęcie → jedna zmiana → powiększ oko” | komponent aplikacji, jak L1-08-V03 | — | — | `TO_DESIGN` |

**Rachunek do V02 (wniosek projektu, nie zdanie ze źródła).** Zasięg ostrości dla obiektywu 50 mm z odległości 1 m, przy krążku rozmycia 0,03 mm (pełna klatka): F1.8 — od około 2,1 cm przed do około 2,2 cm za punktem ostrości (razem około 4,3 cm); F2.8 — od około 3,3 cm przed do około 3,5 cm za (razem około 6,7 cm). Układ głowy przyjęty do schematu, względem bliższego oka: czubek nosa około 2,5 cm przed, dalsze oko około 2,2 cm za (rozstaw oczu około 6,3 cm, głowa obrócona o około 20°), ucho około 9 cm za. Zasada, że zasięg ostrości jest ograniczony i rośnie z liczbą przy F: Canon UK „Depth of field”, Canon U.S.A. „Camera Settings for Stunning Portraits”.

Materiały z wcześniejszych lekcji użyte w L1-09 (bez nowych plików):
- S02, podpunkt 1: schemat z pozycją „z boku” — `assets/lessons/l1-06/l1-06-v02-schemat-2.svg` (L1-06-V02).
- S03, podpunkt 1: dolny pasek ekranu z liczbą przy F — `assets/lessons/l1-07/l1-07-v03-liczba-f-canon.png` (L1-07-V03; tylko lokalnie, D-056).
- S03, podpunkt 2: główne pokrętło — `assets/lessons/l1-02/l1-02-main-dial.jpg` (L1-02-V04).
- S05: zielony punkt ostrości — `assets/lessons/l1-04/l1-04-v08-zielony-punkt-canon.png` (L1-04-V08; tylko lokalnie, D-056).
- S06 oraz ćwiczenie, „Porównaj”: przycisk odtwarzania — `assets/lessons/l1-02/l1-02-v03-playback-button.jpg` (L1-02-V03).
- Pomoc „Zamiast małego punktu…”: ramka ostrości na twarzy — `assets/lessons/l1-04/l1-04-v17-ramka-na-twarzy-canon.png` (L1-04-V17; tylko lokalnie, D-056).

## Tabela źródeł (D-048)

| Twierdzenie w lekcji | Źródło |
|---|---|
| W Av Ania wybiera liczbę przy F, aparat dobiera czas | instrukcja PL/EN, s. 100 |
| Im dalej tło od osoby, tym bardziej rozmyte; ostrość na twarzy | instrukcja PL/EN, s. 77 |
| Światło z boku: jedna strona jaśniejsza, cień po przeciwnej stronie; bliżej okna mocniejsza różnica | źródła L1-06 (`docs/L1-06_ZRODLA_INSTRUKCJA.md`, karta L1-06) |
| F2.8 do portretu; nie za mała liczba; przy F2.8–F4 dalsze oko może być nieostre | Canon U.S.A., „Camera Settings for Stunning Portraits”, https://www.usa.canon.com/learning/training-articles/training-articles-list/camera-settings-for-stunning-portraits |
| Ostrość na bliższym oku jako zasada ogólna | Canon Asia SNAPSHOT, „It's All in the Eyes”, https://snapshot.asia.canon/en/article/a-quick-way-to-create-mesmerizing-portraits-its-all-in-the-eyes |
| Większa liczba przy F — więcej rzeczy ostrych (F4.0 w pomocy) | instrukcja PL/EN, s. 101; L1-08 |
| Dotknięcie ekranu przesuwa punkt ostrości | instrukcja PL/EN, s. 193 (L1-04) |
| Zielony punkt po ustawieniu ostrości | instrukcja PL/EN, s. 194 (L1-04) |
| Duża ramka na twarzy, gdy aparat sam wybiera miejsce ostrości | instrukcja PL/EN, s. 188, 191 (L1-04) |
| Miga 30" — za ciemno; miga 1/4000 — za jasno | instrukcja PL/EN, s. 101 |
| Łokcie przy ciele, oparcie o ścianę, spust spokojnie | Canon (pomoc techniczna), „How do I prevent camera shake?”, https://sg.canon/en/support/8201598100; Canon Europe, „Sharper photos” |
| Za blisko okna — za mocny cień; dalej od okna równiej | Nikon School UK, „Shooting with Window Light”, https://nikonschool.co.uk/hints-and-tips/shooting-with-window-light |
| Twarz nie jest płaska; przy F1.8 nos bywa nieostry, F2.8 daje zapas | wniosek: Canon U.S.A. (jw.), Canon UK „Depth of field”, rachunek do V02 |
| Gdy osoba patrzy prosto w aparat, oba oczy są tak samo daleko | wniosek geometryczny projektu |

Szczegóły: `docs/L1-09_ZRODLA_INSTRUKCJA.md`.

## Kontekst dla nauczyciela AI
Cel ćwiczenia: portret osoby przy oknie z punktem ostrości na bliższym oku, przy F2.8; między portretami zmienia się jedna rzecz. AI w pierwszej kolejności sprawdza: (1) czy bliższe oko jest ostre, (2) czy Ania potrafi nazwać jedną zmianę i jej efekt (ustawienie osoby, tło albo kadr). AI nie proponuje jeszcze: wykrywania oka, Servo AF, zmiany czasu, ISO, lampy, blendy ani oceny pozy.

## Do sprawdzenia na aparacie Ani
Lista w `docs/L1-09_ZRODLA_INSTRUKCJA.md`.
