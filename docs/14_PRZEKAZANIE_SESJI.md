# HANDOFF — Canon RP kurs — korekty wzorca — 27.09.2026

## Punkt startowy
L1-01 i L1-02 są zatwierdzone, wdrożone i opublikowane. Nie wracać do ich projektowania od zera.

Paweł zakończył zbieranie drobnych uwag po teście na iPhonie 15 Pro Max. Pakiet został utrwalony w `docs/19_KOREKTY_WZORCA_2026-09-27.md`. Następnym działaniem jest **jedna skonsolidowana runda korekt w istniejącej aplikacji**.

## Pakiet korekt do wdrożenia

### K-01 — Przejście z teorii do ćwiczenia
Obecne przejście w L1-01 od „Dociśnij do końca” do „Powtórz jeszcze dwa razy” jest zbyt nagłe.

Należy dodać krótkie domknięcie części dydaktycznej, np. sens:
- Ania zna już cały podstawowy cykl wykonania zdjęcia,
- krótko przypominamy: wyceluj → półnaciśnij → poczekaj na potwierdzenie ostrości → dociśnij,
- następnie jawne zdanie: „Teraz przejdźmy do ćwiczenia.”

Przycisk rozpoczynający ćwiczenie powinien być opisowy, np. **„Przejdź do ćwiczenia →”**, zamiast neutralnego „Dalej”.

Samo ćwiczenie może potem używać krótkiego polecenia, np. „Zrób jeszcze dwa zdjęcia”.

### K-02 — Usunąć identyfikatory produkcyjne z UI
Identyfikatory typu `L1-01`, `L1-02`, `S03`, `V04` są wewnętrzne.

Nie mogą być widoczne dla Ani w żadnej części aplikacji. Warstwa użytkowa pokazuje naturalne nazwy: „Lekcja 1”, „Lekcja 2”, tytuł lekcji, „Krok x z y”, „Ćwiczenie” itd.

### K-03 — Pokazać „tylny wybierak” i wszystkie elementy obsługi używane w tekście
W L1-02 tekst odwołuje się do „tylnego wybieraka” przy przechodzeniu między zdjęciami i przesuwaniu powiększonego widoku.

Jeśli Ania ma użyć fizycznego elementu aparatu:
1. najpierw pokazać go na zweryfikowanym zdjęciu aparatu Ani,
2. zaznaczyć dokładnie element,
3. wyjaśnić prostym językiem, gdzie jest i co nim zrobić,
4. dopiero potem utrwalać nazwę techniczną.

Ta zasada obowiązuje wszystkie kolejne lekcje.

## Co pozostaje bez zmian
- styl i kolorystyka aplikacji są zaakceptowane,
- ikona pozostaje,
- ten sam prywatny Canon RP Site,
- nie tworzyć nowej aplikacji ani nowej identyfikacji,
- nie rozszerzać zakresu tej rundy o nowe funkcje.

## Po wdrożeniu
1. Opublikować poprawki do tego samego Site.
2. Sprawdzić na iPhonie 15 Pro Max.
3. Jeżeli wynik jest dobry, zamknąć L1-01/L1-02 jako wzorzec implementacyjny.
4. Przejść do redagowania kolejnych lekcji.

## Standard kolejnych lekcji
Każda kolejna lekcja ma uwzględniać powyższe drobne zasady UX i dydaktyczne od samego początku.

Treść techniczna ma być oparta na zatwierdzonych materiałach źródłowych. Jeśli czegoś nie wiemy albo źródła nie wystarczają, nie zgadujemy: wykonujemy research internetowy, w pierwszej kolejności w oficjalnych materiałach Canon, weryfikujemy z aparatem/menu Ani i dopiero potem zatwierdzamy treść.

## Punkt zatrzymania dla Codexa
Po implementacji i lokalnej weryfikacji raportować wynik. Publikacja ma trafić wyłącznie do istniejącego Site; nie tworzyć nowego Site.


## Instrukcja startowa dla Codexa — wdrożenie korekt

Pracować w istniejącym checkoutcie aplikacji:
`/Users/pawelsiedleczka/.codex/.chatgpt-projects/g-p-6aabf9b9dd848191b1f8a77f4f9213d0/canon-rp-app`

Przed zmianami zsynchronizować lokalną dokumentację `Canon-RP-Kurs` z gałęzią `main`, następnie przeczytać:
1. `docs/19_KOREKTY_WZORCA_2026-09-27.md`,
2. zaktualizowane `docs/L1-01_ROBIE_SWOJE_PIERWSZE_ZDJECIE.md`,
3. zaktualizowane `docs/L1-02_SPRAWDZAM_CZY_ZDJECIE_JEST_OSTRE.md`,
4. `docs/L1-02_KARTA_WIZUALNO_PRODUKCYJNA.md`,
5. `docs/16_ASSET_MANIFEST.md`,
6. `docs/15_STANDARD_PRODUKCJI_LEKCJI.md`.

Wdrożyć wyłącznie pakiet K-01–K-04, bez zmiany stylu, kolorystyki, ikony, Site ani architektury poza tym, co konieczne.

Po zmianach:
- sprawdzić lokalnie,
- przeszukać renderowaną warstwę użytkową pod kątem `L1-`, `S0`, `V0`,
- sprawdzić L1-01 i L1-02 w szerokości iPhone 15 Pro Max,
- raportować wynik przed publikacją, jeśli lokalny workflow nadal wymaga osobnej zgody na publish.


## Stan po lokalnym odbiorze — 27.09.2026
Paweł sprawdził poprawioną lokalną wersję aplikacji po skorygowaniu faktycznego źródła renderowanych treści i potwierdził: **jest OK**.

K-01–K-04 są zaakceptowane lokalnie.

Następne działania dla Codexa:
1. wykonać commit zmian aplikacji,
2. wykonać push,
3. opublikować do istniejącego Canon RP Site — bez tworzenia nowego Site,
4. podać commit aplikacji i potwierdzenie publikacji,
5. nie zmieniać przy tym stylu, kolorów, ikony ani zakresu.

Po publikacji Paweł wykonuje test na rzeczywistym iPhonie 15 Pro Max. Dopiero po jego pozytywnym wyniku oznaczamy L1-01/L1-02 jako zamknięty wzorzec i rozpoczynamy L1-03.


## KONIEC SESJI 27.09.2026 — obowiązujący punkt startowy następnej sesji

### Stan aplikacji
- K-01–K-04 zostały wdrożone, opublikowane i sprawdzone na iPhonie.
- Po tym teście wykryto dodatkową potrzebę: materiał o odtwarzaniu i materiał o tylnym wybieraku mają być rozdzielone i umieszczone bezpośrednio przy odpowiadających im instrukcjach.
- Codex przygotował lokalnie wspólny mechanizm nakładek na zdjęcia aparatu: procentowe pozycjonowanie, wspólny komponent, obsługa reduced motion.
- Kierunek wspólnego mechanizmu jest właściwy, ale aktualny efekt pulsowania został oceniony jako wizualnie nieakceptowalny / nieprofesjonalny.
- Ta ostatnia mikrokorekta NIE została zaakceptowana do publikacji.
- Nie kontynuować od razu pracy nad animacją ani nie rozpoczynać L1-03.

### Problem procesu
W bieżącej sesji Codex kilkukrotnie wymagał dodatkowej kontroli:
- raportował wykonanie korekt, których nie było w faktycznie uruchomionej aplikacji,
- testy techniczne nie odpowiadały rzeczywistemu efektowi widocznemu w UI,
- użytkownik musiał ręcznie wykrywać rozbieżności.

### Pierwszy krok następnej sesji
**Nie zaczynać od aplikacji. Najpierw przygotować i dodać skill precyzyjnej pracy dla Codexa.**

Wymagania skilla są zapisane w:
- `docs/20_CODEX_PRECISION_SKILL_PLAN.md`
- D-035 w `docs/09_DECISIONS.md`

Skill ma wymuszać:
- pracę ściśle według dokumentacji i zatwierdzonego zakresu,
- weryfikację faktycznie renderowanej aplikacji,
- zakaz zgadywania i samowolnego rozszerzania zadania,
- rozdzielenie raportowania: pliki → testy → podgląd → commit → push → publish,
- profesjonalny standard wykonania,
- zatrzymanie i zgłoszenie problemu przy niepewności.

### Kolejność po dodaniu skilla
1. Uruchomić/zweryfikować skill na prostym zadaniu kontrolnym.
2. Wrócić do lokalnej mikrokorekty L1-02.
3. Dopracować styl wskazania elementu aparatu do poziomu profesjonalnego.
4. Obejrzeć lokalny rezultat.
5. Dopiero po akceptacji wykonać commit/push/publish.
6. Sprawdzić na fizycznym iPhonie.
7. Zamknąć L1-01/L1-02 jako wzorzec.
8. Dopiero wtedy rozpocząć L1-03.

### Nadrzędna zasada jakości
Canon RP kurs jest profesjonalnym produktem, którego pierwszą użytkowniczką jest Ania. Prywatny obecny zakres nie uzasadnia rozwiązań „byle działało”.
