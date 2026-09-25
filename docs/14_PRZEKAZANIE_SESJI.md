# HANDOFF — Canon RP kurs — koniec sesji 25.09.2026

## Punkt startowy następnej sesji

Nie wracać do zatwierdzania L1-01 ani L1-02. Obie lekcje są zatwierdzone, wdrożone i opublikowane w istniejącej aplikacji Canon RP.

Pierwsze zadanie następnej sesji:
**Paweł podaje wszystkie drobne niedociągnięcia i uzupełnienia zauważone podczas rzeczywistego testu na iPhonie 15 Pro Max. Zbieramy je w jeden pakiet korekt i dopiero wtedy przekazujemy Codexowi.**

Nie poprawiać rzeczy pojedynczo po jednej. Nie rozpoczynać jeszcze L1-03.

## Stan aplikacji

- istniejący prywatny Canon RP Site pozostaje jedyną aplikacją,
- adres pozostaje bez zmian,
- obecna ikona i kolorystyka są zaakceptowane i pozostają,
- L1-01 i L1-02 zostały wdrożone według wspólnego wzorca danych/ekranów,
- wersja została opublikowana 25.09.2026,
- commit źródła aplikacji: `651b4f6e746f4a6cffac612812169afc74874545`,
- rzeczywisty test na iPhonie 15 Pro Max: **ogólnie pozytywny; kilka drobnych niedociągnięć do poprawy**.

## Cel następnej sesji

1. Zebrać pełną listę uwag Pawła z telefonu.
2. Rozdzielić uwagi na: błąd / korekta UX / brak materiału / uzupełnienie treści.
3. Sprawdzić tylko te kwestie, które naprawdę wymagają weryfikacji; nie uruchamiać karuzeli dodatkowych audytów.
4. Przygotować jeden skonsolidowany pakiet zmian dla Codexa.
5. Wdrożyć go w istniejącej aplikacji.
6. Opublikować poprawioną wersję do tego samego Site.
7. Ponownie sprawdzić na iPhonie 15 Pro Max.
8. Jeżeli wynik jest dobry — formalnie zamknąć wzorzec dwóch pierwszych lekcji.
9. Dopiero potem przejść do L1-03.

## Stan treści

### L1-01 — „Robię swoje pierwsze zdjęcie”
- treść zatwierdzona,
- wdrożona,
- V01 i V02 mają przygotowane kadry i czekają na finalną ocenę wizualną,
- V03–V06 pozostają jawnymi brakami produkcyjnymi; nie są zastępowane domysłem.

### L1-02 — „Sprawdzam, czy zdjęcie jest ostre”
- treść zatwierdzona,
- wdrożona,
- V03 ma przygotowany kadr i czeka na finalną ocenę wizualną,
- V01, V02, V04 i V05 pozostają jawnymi brakami/elementami do przygotowania,
- kolejność dydaktyczna pozostaje: gotowy przykład → wyjaśnienie → obsługa EOS RP → ćwiczenie na własnych zdjęciach.

## Materiały źródłowe

Codex ma lokalny pakiet:
`/Users/pawelsiedleczka/Documents/ChatGPT/Canon-RP-Kurs/materials/camera-source-pack-2026-09-24/`

Pakiet został skopiowany i porównany ze źródłem bez różnic. Jest lokalnym źródłem zdjęć aparatu i menu.

Twarde przypisania:
- L1-01-V01/V02: wyłącznie `fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg`,
- L1-02-V03: `57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg`.

Codex nie wybiera alternatywnych zdjęć samodzielnie.

## Reguły pozostające w mocy

- ChatGPT + Paweł tworzą i zatwierdzają treść oraz sposób nauczania; Codex implementuje.
- Ania dostaje gotowy kurs; nie produkuje materiałów, na których ma się dopiero uczyć.
- Nie zgadujemy menu, ustawień ani wyglądu EOS RP.
- Brak finalnego assetu może być placeholderem produkcyjnym, ale nie może być ukryty losowym zamiennikiem.
- Obecna identyfikacja wizualna aplikacji jest zaakceptowana.
- Nie tworzyć nowego Site.
- Nie wracać do zakończonych decyzji bez wyraźnej potrzeby.

## Po zamknięciu następnej sesji

Jeżeli poprawiona wersja przejdzie test na iPhonie:
- oznaczyć L1-01/L1-02 jako **wzorzec implementacyjny kolejnych lekcji**,
- utrwalić ewentualne nowe zasady UX w standardzie produkcji lekcji,
- przejść do wspólnego opracowania i zatwierdzenia L1-03.

## Komenda startowa do nowego wątku

**„Wracamy do Canon RP kurs. Przeczytaj najnowszy handoff i aktualną dokumentację. Dwie pierwsze lekcje są już wdrożone i przetestowane na iPhonie 15 Pro Max. W tej sesji skupiamy się wyłącznie na zebraniu i poprawieniu drobnych niedociągnięć wersji wzorcowej. Nie przechodź jeszcze do L1-03 i nie wracaj do wcześniejszych zatwierdzonych decyzji.”**
