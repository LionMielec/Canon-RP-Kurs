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


## Weryfikacja oficjalnego mechanizmu — 28.09.2026
Sprawdzono aktualne oficjalne materiały OpenAI dotyczące Codexa i skills.

Potwierdzone:
- skill jest katalogiem zawierającym obowiązkowy plik `SKILL.md` z metadanymi `name` i `description` oraz instrukcjami,
- Codex ma wbudowany kreator skills wywoływany przez `$skill-creator`,
- oficjalny przykład OpenAI pokazuje skill repozytoryjny pod `.agents/skills/<skill-name>/SKILL.md` oraz skill użytkownika pod `~/.agents/skills/<skill-name>/SKILL.md`,
- skills są przeznaczone do konkretnych, powtarzalnych workflow,
- `AGENTS.md` jest mechanizmem repozytoryjnych instrukcji ładowanych przez Codex automatycznie.

Wniosek roboczy do zatwierdzenia:
najbardziej niezawodne rozwiązanie dla Canon RP kurs to dwie warstwy:
1. krótki repozytoryjny `AGENTS.md` z niezmiennymi zasadami projektu i wymogiem stosowania skilla przy zadaniach implementacyjnych,
2. repozytoryjny skill `.agents/skills/canon-rp-precision/SKILL.md` opisujący precyzyjny workflow: zakres → źródło prawdy → implementacja → faktyczny podgląd → testy → raport → osobna zgoda na commit/push/publish.

Nie instalować skilla globalnie, dopóki nie ma potrzeby stosowania tych samych reguł w innych projektach.


## Korekta ścieżki 28.09.2026
Aktualna oficjalna dokumentacja Codexa wskazuje repozytoryjne skills w `.agents/skills/<skill-name>/SKILL.md`. Wcześniejszy roboczy zapis `.codex/skills/...` był nieaktualny i nie obowiązuje.
