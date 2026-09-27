# HANDOFF — Canon RP kurs — korekty wzorca — 27.09.2026

## Punkt startowy
L1-01 i L1-02 są zatwierdzone, wdrożone i opublikowane. Nie wracać do ich projektowania od zera.

Paweł zakończył zbieranie drobnych uwag po teście na iPhonie 15 Pro Max. Następnym działaniem jest **jedna skonsolidowana runda korekt w istniejącej aplikacji**.

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
