# Codex — wzorzec implementacji dwóch pierwszych lekcji

Status: WYKONANE I OPUBLIKOWANE — 25.09.2026  
Data: 2026-09-25

## Cel
Zaktualizować istniejącą prywatną aplikację Canon RP tak, aby dwie zatwierdzone lekcje Poziomu 1 były pierwszym wzorcem implementacyjnym dla kolejnych lekcji.

Nie tworzyć nowej aplikacji od zera.

## Gdzie pracować
Właściwy kod istniejącej aplikacji znajduje się w checkoutcie Sites opisanym w `docs/13_PIERWSZA_APLIKACJA.md`:

`/Users/pawelsiedleczka/.codex/.chatgpt-projects/g-p-6aabf9b9dd848191b1f8a77f4f9213d0/canon-rp-app`

Repozytorium `Canon-RP-Kurs` przechowuje dokumentację i zatwierdzoną treść. Katalog `app/` w tym repo nie jest aktualnym kodem opublikowanej aplikacji.

## Obowiązkowe źródła przed implementacją
Przeczytać:
1. `AGENTS.md`
2. `docs/00_START_HERE.md`
3. `docs/09_DECISIONS.md`
4. `docs/15_STANDARD_PRODUKCJI_LEKCJI.md`
5. `docs/16_ASSET_MANIFEST.md`
6. `docs/L1-01_ROBIE_SWOJE_PIERWSZE_ZDJECIE.md`
7. `docs/L1-01_KARTA_WIZUALNO_PRODUKCYJNA.md`
8. `docs/L1-02_SPRAWDZAM_CZY_ZDJECIE_JEST_OSTRE.md`
9. `docs/L1-02_KARTA_WIZUALNO_PRODUKCYJNA.md`
10. `docs/13_PIERWSZA_APLIKACJA.md`

## Zakres
### 1. Lekcja 1 — „Robię swoje pierwsze zdjęcie”
Wdrożyć dokładnie zatwierdzoną treść i kolejność kroków.

Użyć istniejących zatwierdzonych/wybranych materiałów tam, gdzie są dostępne.

Brakujące materiały V03–V06 pozostawić jako jawne placeholdery produkcyjne zgodne z kartą lekcji. Nie generować zamienników i nie zmieniać treści, aby ukryć brak.

### 2. Lekcja 2 — „Sprawdzam, czy zdjęcie jest ostre”
Wdrożyć dokładnie zatwierdzoną treść i kolejność:
gotowy przykład → wyjaśnienie → obsługa EOS RP → ćwiczenie na własnych zdjęciach.

V01–V05 osadzić zgodnie z kartą produkcyjną. Jeśli finalny asset nie jest jeszcze przygotowany, zostawić jawny placeholder.

### 3. Wzorzec kolejnych lekcji
Kod ma wyraźnie rozdzielać:
- dane lekcji,
- kroki,
- ćwiczenie,
- podsumowanie,
- pomoc,
- powiązane materiały wizualne.

Celem jest możliwość dodania kolejnej zatwierdzonej lekcji bez ręcznego budowania nowej strony od zera.

Nie tworzyć rozbudowanego frameworka ani systemu na przyszłość. Zastosować najmniejszą trwałą strukturę, która wystarczy do dalszych lekcji Poziomu 1.

### 3a. Zachować zatwierdzony wygląd aplikacji
- Zachować obecną ikonę aplikacji bez zmian.
- Zachować obecną kolorystykę i ogólny kierunek wizualny aplikacji; użytkownik ocenia je jako właściwe.
- Aktualizacja dwóch lekcji nie może tworzyć nowej identyfikacji wizualnej ani nowej ikony.
- Kontynuować pracę na tym samym istniejącym Site i tym samym adresie.

### 4. Nawigacja
Zachować istniejący kierunek wizualny aplikacji jako punkt wyjścia.

Dodać czytelny spis lekcji z wejściem do:
- Lekcji 1,
- ćwiczenia Lekcji 1,
- Lekcji 2,
- ćwiczenia Lekcji 2.

Nie dodawać Lekcji 3 ani kolejnych.

### 5. Urządzenia
Priorytet mobilny:
- iPhone 17 Pro Max Ani,
- iPhone 15 Pro Max Pawła.

Sprawdzić również zwykły widok desktopowy.

### 6. Zakazy
Codex nie może:
- zmieniać zatwierdzonej treści lekcji,
- dopisywać nowych treści dydaktycznych,
- projektować nowych lekcji,
- wymyślać wyglądu menu lub elementów EOS RP,
- generować brakujących materiałów wizualnych jako zamienników,
- dodawać AI, backendu, bazy danych ani synchronizacji,
- tworzyć drugiego Site,
- publikować ani wdrażać wersji bez osobnej zgody właściciela projektu.

## Kryteria odbioru
Przed zakończeniem:
1. Obie lekcje działają w istniejącej aplikacji lokalnie.
2. Każdy krok odpowiada aktualnej zatwierdzonej dokumentacji.
3. Brakujące assety są jawnie oznaczone, a nie ukryte.
4. Nawigacja pozwala wejść bezpośrednio do lekcji i ćwiczeń.
5. Układ jest czytelny na szerokościach mobilnych i desktopowych.
6. Nie ma poziomego przepełnienia ani błędów JavaScript.
7. Powiększony tekst i ograniczenie ruchu nie psują podstawowej obsługi.
8. Struktura kodu pozwala dodać kolejną lekcję na tym samym wzorcu.

## Oczekiwany raport Codexa
Po wykonaniu pracy Codex ma zwrócić:
- listę zmienionych plików,
- krótkie wyjaśnienie wzorca implementacyjnego,
- listę placeholderów/brakujących assetów,
- wyniki testów,
- zrzuty lub podgląd obu lekcji,
- listę istotnych problemów wymagających decyzji Pawła.

## Punkt zatrzymania
Po lokalnej implementacji i weryfikacji zatrzymać się.

Nie commitować, nie pushować i nie publikować nowej wersji bez osobnej zgody właściciela projektu.

## Decyzja o nieblokowaniu testu przez źródło V01/V02
- Rozbieżność nazwy/identyfikatora zdjęcia góry aparatu nie blokuje wersji testowej.
- Obecne `dist/camera-top.jpeg` może pozostać roboczym podglądem V01/V02 w wersji testowej.
- Nie oznaczać tego pliku jako finalnie zatwierdzonego assetu.
- Finalne źródło i kadry V01/V02 zostaną domknięte później w produkcji assetów.
- Priorytet teraz: uruchomić wzorcowe dwie lekcje w istniejącej aplikacji i przeprowadzić test na iPhonie 15 Pro Max.

## Wynik etapu
- L1-01 i L1-02 zostały wdrożone w istniejącej aplikacji.
- Zachowano ikonę, kolorystykę, istniejący Site i dostęp tylko dla właściciela.
- Commit źródła aplikacji: `651b4f6e746f4a6cffac612812169afc74874545`.
- Wersja została opublikowana i uruchomiona na iPhonie 15 Pro Max.
- Ogólny kierunek został oceniony pozytywnie.
- Następny etap: jedna runda drobnych korekt zebranych po teście na telefonie; dopiero po niej wzorzec zostanie formalnie zamknięty.
