# AGENTS.md — Canon RP kurs

## Cel projektu
Canon RP kurs jest profesjonalnym kursem nauki fotografii i obsługi Canon EOS RP.
Pierwszą użytkowniczką jest Ania, ale projekt od początku ma standard produktu, który może później zostać rozwinięty i skomercjalizowany.

## Role (D-047)
- Paweł (właściciel projektu) podejmuje decyzje końcowe.
- Claude w czacie (projekt claude.ai) jest architektem i audytorem: redaguje treść, przygotowuje decyzje i polecenia.
- Agent kodujący implementuje wyłącznie zatwierdzone rozwiązania.
- Projekt jest niezależny od innych projektów właściciela. Nie modyfikuj innych projektów.

## Struktura repozytorium
- `docs/` — dokumentacja, źródło prawdy. Aktualny stan: koniec `docs/14_PRZEKAZANIE_SESJI.md` i najnowsze wpisy w `docs/09_DECISIONS.md`.
- `app/dist/` — kanoniczne źródło aplikacji (statyczny HTML/CSS/JS, bez procesu build).
- `materials/` — lokalne materiały źródłowe; pliki zdjęć są poza Git.
- `materials/canon-official/` — oficjalne instrukcje Canon EOS RP w PDF (polska i angielska); tylko lokalnie, poza Git.
- `review/` — lekkie kopie materiałów do przeglądu przez Claude w czacie (D-053); bez GPS i numerów seryjnych; nie jest częścią aplikacji.
- Dawny folder aplikacji w katalogu Codexa jest zamrożonym archiwum. Nie edytuj go.

## Nadrzędne zasady pracy
1. Dokumentacja projektu jest źródłem prawdy. Przed zmianą przeczytaj dokumenty wskazane w aktualnym handoffie i statusie.
2. Nie zgaduj. Jeżeli czegoś nie wiesz, brakuje źródła, instrukcje są sprzeczne albo zakres jest niejasny — zatrzymaj się i zgłoś problem.
3. Nie rozszerzaj zakresu zadania bez zgody.
4. Nie zmieniaj zaakceptowanych elementów poza zakresem zadania.
5. Nie stosuj rozwiązań „byle działało”, jednorazowych hacków ani prowizorek.
6. Kod, UX, treść, assety i struktura danych mają być utrzymywalne, powtarzalne i skalowalne.
7. Agent kodujący jest wykonawcą technicznym. Nie wymyśla samodzielnie finalnej treści edukacyjnej ani nie zmienia kolejności dydaktycznej bez zatwierdzenia.
8. Rzeczywisty Canon EOS RP Ani, zatwierdzone materiały projektu i oficjalne materiały Canon są źródłami prawdy dla obsługi aparatu.
9. Identyfikatory produkcyjne typu L1-xx, Sxx, Vxx nigdy nie mogą trafić do widocznej warstwy użytkowej.
10. Każdy element aparatu użyty w instrukcji dla Ani musi być pokazany na zweryfikowanym materiale i wyjaśniony prostym językiem.
11. Rozwiązuj zaakceptowany problem najmniejszą trwałą zmianą. Przed rozszerzeniem zakresu, zmianą architektury lub znaczącym wzrostem złożoności zatrzymaj się i zgłoś BLOCKER / SCOPE EXPANSION: przyczynę, wpływ, najmniejszy wariant oraz alternatywy.

## Reguły treści
- Używaj prostego polskiego języka na wszystkich poziomach.
- Oddzielaj ustalenia właściciela, propozycje i niezweryfikowane dane.
- Źródła, numery stron i adresy nigdy nie trafiają do warstwy widocznej dla Ani (D-048).
- Nie wymyślaj polskich nazw menu, obiektywu, firmware ani parametrów zdjęcia.
- Tekst i ikony menu pochodzą z rzeczywistych ekranów, nie z generatorów.
- Nie publikuj zdjęć, ciężkich materiałów ani cudzych treści bez sprawdzenia zakresu i warunków użycia.
- Klucze API pozostają poza kodem klienta i repo.
- Zmiany decyzji zapisuj z datą w `docs/09_DECISIONS.md`.

## Obowiązkowy protokół implementacji
Dla każdego zadania implementacyjnego użyj skilla `canon-rp-precision`. Nie pomijaj żadnego etapu tego workflow.

## Rozdzielenie stanów
Zawsze odróżniaj:
- zmianę dokumentacji,
- zmianę kodu / danych aplikacji,
- uruchomienie lokalnego podglądu,
- test techniczny,
- weryfikację faktycznie renderowanego UI,
- akceptację właściciela,
- commit,
- push,
- publikację.

Nie nazywaj zadania „wykonanym”, jeśli właściwy etap nie został rzeczywiście zweryfikowany.

## Punkty zatrzymania
Zatrzymaj się przed niezatwierdzonym: usuwaniem lub resetowaniem danych, commit, push, reset, checkout, zmianą gałęzi, rebase, publikacją, zmianą zewnętrznego systemu albo ujawnieniem lub zmianą sekretów.
Jeżeli nie ma jednoznacznej zgody, zatrzymaj się i raportuj stan. Nie pytaj ponownie o działanie już wyraźnie zatwierdzone w bieżącym zadaniu.

## Standard jakości
Mały zakres funkcji jest dopuszczalny. Niski standard wykonania — nie.
Projekt ma być tworzony profesjonalnie od początku.
