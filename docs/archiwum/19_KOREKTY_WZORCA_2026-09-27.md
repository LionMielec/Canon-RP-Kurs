# Canon RP kurs — pakiet korekt wzorca L1-01/L1-02

Data: 2026-09-27  
Status: ZATWIERDZONY DO WDROŻENIA

## Cel
Domknąć drobne niedociągnięcia wykryte podczas rzeczywistego testu pierwszych dwóch lekcji na iPhonie 15 Pro Max, bez zmiany zaakceptowanego stylu i bez rozszerzania zakresu aplikacji.

## K-01 — przejście teoria → ćwiczenie
W L1-01 przejście po kroku „Dociśnij do końca” nie może od razu zaczynać ćwiczenia poleceniem „Powtórz jeszcze dwa razy”.

Docelowy przebieg:
1. krótko podsumować cały cykl:
   **wyceluj → półnaciśnij → poczekaj na potwierdzenie ostrości → dociśnij do końca**,
2. dodać zdanie: **„Teraz przejdźmy do ćwiczenia.”**,
3. przycisk rozpoczynający ćwiczenie nazwać **„Przejdź do ćwiczenia →”**,
4. dopiero w ćwiczeniu pokazać polecenie **„Zrób jeszcze dwa zdjęcia”** i przypomnieć spokojny, świadomy przebieg.

Treść źródłowa została skorygowana w:
`docs/L1-01_ROBIE_SWOJE_PIERWSZE_ZDJECIE.md`.

## K-02 — identyfikatory wewnętrzne niewidoczne dla Ani
Usunąć z całej warstwy użytkowej wszystkie identyfikatory produkcyjne:
- `L1-01`, `L1-02`,
- `Sxx`,
- `Vxx`,
- inne identyfikatory techniczne używane w danych lub dokumentacji.

Dozwolona warstwa użytkowa:
- „Lekcja 1”, „Lekcja 2”,
- tytuł lekcji,
- „Krok x z y”,
- „Ćwiczenie”,
- naturalne komunikaty.

Identyfikatory pozostają w kodzie/danych, jeśli są potrzebne technicznie, ale nie są renderowane użytkowniczce.

## K-03 — tylny wybierak musi być pokazany
W L1-02 słowa „tylny wybierak” nie mogą pojawiać się bez wcześniejszego wizualnego wskazania elementu.

Źródło:
`57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg`  
Library: `libfile_eb4721328c288191bb5aa19d2aa13f7e`

To rzeczywiste zdjęcie tylnej ścianki EOS RP Ani i wyraźnie pokazuje okrągły wybierak z kierunkami po prawej stronie ekranu.

### Krok S03
Materiał V03 ma pokazać:
1. przycisk odtwarzania,
2. tylny wybierak,
3. podpis prostym językiem: „Tylny wybierak — lewo / prawo”.

### Krok S04
Materiał V04 ma być trzyetapowy:
**lupa → główne pokrętło → tylny wybierak**.

Źródła V04:
- tył: `57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg`,
- góra: `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg`.

Nie tworzyć z domysłu elementów aparatu.

## K-04 — kontrola tekstu widocznego dla Ani
Po implementacji przejść wszystkie ekrany L1-01 i L1-02 i sprawdzić, czy:
- nie ma żadnego `L1-`, `Sxx`, `Vxx`,
- nie ma nazw fizycznych elementów aparatu bez pokazania ich wcześniej,
- przejścia do ćwiczeń są jawne i naturalne,
- przyciski opisują działanie, gdy zaczynają nowy etap.

## Co pozostaje bez zmian
- styl,
- kolorystyka,
- ikona,
- układ wizualny jako kierunek,
- ten sam prywatny Canon RP Site,
- istniejąca architektura danych lekcji.

## Test po wdrożeniu
Sprawdzić:
- iPhone 15 Pro Max,
- brak poziomego przewijania,
- brak błędów JavaScript,
- przyciski Wstecz/Dalej i wejście do ćwiczenia,
- poprawne wyróżnienie elementów EOS RP,
- brak identyfikatorów produkcyjnych w UI.

## Punkt zatrzymania
Po wdrożeniu i publikacji do istniejącego Site wykonać test na iPhonie 15 Pro Max.

Jeżeli wynik jest dobry:
- oznaczyć L1-01/L1-02 jako zamknięty wzorzec implementacyjny,
- rozpocząć redagowanie L1-03 według zaktualizowanego standardu.
