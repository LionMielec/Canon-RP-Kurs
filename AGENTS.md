# Zasady pracy — Canon-RP-Kurs

Przed pracą przeczytaj `docs/00_START_HERE.md`, `docs/09_DECISIONS.md` i `docs/10_TODO.md`.

Użytkownik podejmuje decyzje końcowe. ChatGPT jest architektem, audytorem i drugą parą oczu. Codex implementuje zaakceptowane rozwiązania. Projekt jest niezależny od LuxeTerminal; nie modyfikuj innych projektów.

Rozwiązuj zaakceptowany problem najmniejszą trwałą zmianą. Pracuj samodzielnie w zatwierdzonym zakresie, grupując odczyty, diagnostykę i weryfikację. Nie wdrażaj opcjonalnych usprawnień ani systemów na przyszłość.

Przed rozszerzeniem zakresu, zmianą architektury lub znaczącym wzrostem złożoności zatrzymaj się i zgłoś **BLOCKER / SCOPE EXPANSION**: przyczynę, wpływ, najmniejszy wariant oraz alternatywy. Jeśli mała poprawka wymaga przebudowy, powiedz: „To przestało być małą poprawką”.

Zatrzymaj się przed niezatwierdzonym: usuwaniem/resetowaniem danych, commit/push/reset/checkout/rebase, zmianą branchy, produkcyjnej infrastruktury lub harmonogramu, restartem infrastruktury, zmianą zewnętrznego systemu, operacją z rzeczywistym skutkiem zewnętrznym albo ujawnieniem/zmianą sekretów. Nie pytaj ponownie o działanie już wyraźnie zatwierdzone w bieżącej sesji.

Przed implementacją wykonaj potrzebną analizę całości. Zwracaj jeden skonsolidowany przegląd istotnych problemów; pomijaj kosmetykę. Po etapie przeprowadź adekwatną weryfikację i self-review, sprawdź zakres oraz zwróć końcowy raport. Nie przechodź automatycznie do kolejnego etapu wymagającego zgody.

## Reguły treści

- Kurs jest prywatny, dla Ani i jej Canon EOS RP. Używaj prostego polskiego języka na wszystkich poziomach.
- Oddzielaj ustalenia użytkownika, propozycje i niezweryfikowane dane.
- Nie wymyślaj polskich nazw menu, obiektywu, firmware ani parametrów zdjęcia.
- Tekst i ikony menu pochodzą z rzeczywistych ekranów, nie z generatorów.
- Nie publikuj zdjęć, ciężkich materiałów ani cudzych treści bez sprawdzenia zakresu i warunków użycia.
- Klucze API pozostają poza kodem klienta i repo. Nie uruchamiaj płatnych usług w etapie dokumentacji.
- Zmiany decyzji zapisuj z datą w `docs/09_DECISIONS.md`.
