# Canon RP kurs — standard produkcji lekcji

Stan: 2026-09-27  
Status: ZATWIERDZONY  
Obowiązuje: od L1-01 i dla wszystkich kolejnych lekcji

## 1. Cel dokumentu
Każda lekcja ma powstawać od razu jako kompletny pakiet edukacyjno-produkcyjny. Format ma pozwolić Codexowi później złożyć lekcję bez zgadywania, gdzie i po co ma pojawić się zdjęcie, grafika, ekran lub animacja.

## 2. Dwie warstwy każdej lekcji
### A. Warstwa dla Ani
Finalna treść edukacyjna: cel, proste wyjaśnienie, kolejne czynności, ćwiczenie, sprawdzenie efektu i przejście do następnej lekcji.

### B. Warstwa produkcyjna
Niewidoczna jako zwykła treść kursu. Zawiera identyfikatory kroków, materiały wizualne, cel każdego materiału, źródło, instrukcję przygotowania i status produkcji.

## 3. Identyfikatory
Każdy istotny krok i materiał otrzymuje stały identyfikator, np. `L1-01-S01` oraz `L1-01-V01`. Po zatwierdzeniu identyfikatory pozostają stałe.

## 4. Minimalny opis materiału wizualnego
Każdy materiał opisujemy przez: ID, powiązany krok, miejsce użycia, typ, cel dydaktyczny, źródło prawdy, dokładny opis materiału, sposób prezentacji, status i uwagi dla Codexa.

## 5. Statusy produkcyjne
- `SOURCE_SELECTED` — konkretne źródło zostało wybrane, ale finalny asset nie jest jeszcze przygotowany,
- `TO_CAPTURE` — trzeba wykonać zdjęcie, klip lub rzeczywisty ekran z aparatu Ani,
- `TO_DESIGN` — trzeba przygotować grafikę na podstawie zatwierdzonych źródeł,
- `TO_ANIMATE` — trzeba przygotować animację/3D,
- `TO_PREPARE` — istniejące źródło trzeba przyciąć, oznaczyć, zoptymalizować lub przygotować do użycia,
- `TO_VERIFY` — materiał wymaga kontroli technicznej lub zgodności z aparatem Ani,
- `APPROVAL_PENDING` — materiał jest gotowy produkcyjnie i czeka na akceptację właściciela projektu,
- `APPROVED` — materiał zatwierdzony do implementacji.

Jeden asset może mieć jednocześnie kilka statusów zadaniowych, np. `TO_CAPTURE` + `TO_DESIGN`. Codex nie zastępuje brakującego materiału własnym zamiennikiem.

## 6. Zasada doboru formy
Stosujemy najprostszą formę, która skutecznie uczy: zdjęcie/prawdziwy ekran → grafika → animacja → 3D tylko wtedy, gdy wnosi realną przewagę edukacyjną.

## 7. Zasady dla Codexa
Codex implementuje zatwierdzoną strukturę i identyfikatory, osadza materiały przy wskazanych krokach, nie zmienia samodzielnie kolejności dydaktycznej i nie odtwarza wyglądu EOS RP ani menu z domysłu. Brakujący asset pozostaje jawnym placeholderem produkcyjnym.

## 8. Co powstaje dla każdej lekcji
- finalna treść lekcji,
- lista kroków z ID,
- ćwiczenie i kryterium sprawdzenia efektu,
- karta wizualno-produkcyjna,
- lista potrzebnych assetów i ich statusów,
- instrukcje montażu dla Codexa.

## 9. Kolejność pracy
**research źródeł → treść → ćwiczenie → kontrola techniczna na EOS RP → projekt warstwy wizualnej → karta produkcyjna → akceptacja właściciela → produkcja assetów → zatwierdzenie assetów → implementacja w Codexie.**

Warstwę wizualną projektujemy równolegle z treścią każdej lekcji, począwszy od L1-01.

## 10. Reguły UX i dydaktyczne po teście wzorca — 27.09.2026
- Przed przejściem z teorii do ćwiczenia zawsze stosujemy krótkie domknięcie: co Ania już umie + jasna zapowiedź „teraz przejdźmy do ćwiczenia”.
- Gdy przycisk rozpoczyna nowy etap lekcji, jego etykieta opisuje ten etap, np. „Przejdź do ćwiczenia”, zamiast ogólnego „Dalej”.
- Identyfikatory produkcyjne (`L1-xx`, `Sxx`, `Vxx`) pozostają wyłącznie w warstwie wewnętrznej i nigdy nie są wyświetlane Ani.
- Każdy fizyczny element obsługi aparatu przywołany w treści musi zostać pokazany na zweryfikowanym materiale i objaśniony prostym językiem przed użyciem nazwy technicznej.
- Nie zakładamy, że element aparatu jest „oczywisty”; jeśli Ania ma go użyć, kurs ma wskazać dokładnie gdzie on jest i co z nim zrobić.
- Styl i kolorystyka zaakceptowanego wzorca pozostają bez zmian, o ile właściciel projektu nie zdecyduje inaczej.

## 11. Weryfikacja merytoryczna kolejnych lekcji
Podstawą są zatwierdzone źródła projektu: oficjalne instrukcje Canon EOS RP, materiały dotyczące używanego obiektywu, rzeczywisty aparat Ani, rzeczywiste menu i zatwierdzone materiały edukacyjne.

Jeśli potrzebna informacja nie jest potwierdzona w tych materiałach albo pojawia się wątpliwość:
1. nie zgadywać,
2. wyszukać aktualne informacje w internecie,
3. preferować oficjalne źródła Canon jako źródło pierwotne,
4. w razie potrzeby porównać kilka wiarygodnych źródeł pomocniczych,
5. skonfrontować wynik z rzeczywistym aparatem/menu Ani,
6. dopiero wtedy zapisać lub skorygować finalną treść lekcji.

Istotne ustalenia techniczne i źródła weryfikacji należy utrwalać w dokumentacji konkretnej lekcji.
