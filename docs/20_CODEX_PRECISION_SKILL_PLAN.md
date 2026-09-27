# Canon RP kurs — plan skilla precyzyjnej pracy dla Codexa

Stan: 27.09.2026  
Status: wymagania zatwierdzone do opracowania w następnej sesji

## Cel
Przed dalszą implementacją Canon RP kurs przygotować i dodać skill/regułę pracy, która wymusza na Codexie precyzyjne wykonywanie poleceń, ścisłe trzymanie się dokumentacji i profesjonalny standard realizacji.

Skill nie zastępuje dokumentacji projektu. Ma wymuszać właściwy sposób pracy z dokumentacją.

## Problemy zaobserwowane 27.09.2026
- Codex raportował korekty jako wykonane, mimo że faktycznie uruchomiona aplikacja nadal pokazywała stare treści.
- Testy techniczne zostały przedstawione jako potwierdzenie efektu, którego użytkownik nie widział w realnym lokalnym podglądzie.
- Konieczne było ręczne wykrycie, że zmodyfikowano niewłaściwe źródło / warstwę względem faktycznie renderowanej aplikacji.
- Kolejna implementacja spełniała część wymagań technicznych, ale efekt wizualny animowanego wskazania nie osiągnął oczekiwanego poziomu jakości.

## Wymagane zachowanie Codexa
1. Najpierw odczytać obowiązującą dokumentację i ustalić dokładny zakres zadania.
2. Zidentyfikować rzeczywiste źródło danych/kodu renderowanej aplikacji przed zmianą.
3. Nie rozszerzać zakresu bez zgody.
4. Nie wprowadzać jednorazowych hacków, jeżeli wymaganie ma obowiązywać kolejne lekcje.
5. Po zmianie sprawdzić faktycznie renderowaną aplikację, a nie tylko pliki lub test jednostkowy.
6. Oddzielnie raportować: zmienione pliki, testy techniczne, lokalny efekt, commit, push, publikację.
7. Nie używać słowa „wykonane” dla etapu, którego nie zweryfikowano.
8. Nie wykonywać commit/push/publish bez wyraźnej zgody, jeśli handoff ustanawia punkt zatrzymania.
9. Przy sprzeczności, niepewności lub brakującym źródle zatrzymać się i zgłosić problem zamiast zgadywać.
10. Zachować profesjonalny standard produktu zgodnie z D-034.
11. Odbiór wizualny właściciela projektu jest osobnym etapem i nie może być zastąpiony automatycznym testem.
12. Po każdej zmianie sprawdzić, czy nie naruszono wcześniej zaakceptowanych elementów poza zakresem zadania.

## Oczekiwany protokół odpowiedzi Codexa
Przed pracą:
- „Rozumiem zakres: …”
- „Nie zmieniam: …”
- „Pliki/źródło, które zweryfikuję przed zmianą: …”
- „Punkt zatrzymania: …”

Po pracy:
- „Zmieniłem: …”
- „Nie zmieniłem: …”
- „Zweryfikowałem w faktycznym podglądzie: …”
- „Testy techniczne: …”
- „Pozostałe ograniczenia / czego nie zweryfikowałem: …”
- „Commit/push/publish: TAK/NIE”

## Następny krok
W następnej sesji najpierw sprawdzić aktualny oficjalny sposób definiowania/dodawania skilli lub trwałych instrukcji dla Codexa, a następnie przygotować właściwy skill na podstawie powyższych wymagań.

Dopiero po uruchomieniu skilla wracamy do niedomkniętej mikrokorekty L1-02.
