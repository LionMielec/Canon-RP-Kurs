# AGENTS.md — Canon RP kurs

Status: HISTORYCZNA — obowiązująca wersja to `AGENTS.md` w katalogu głównym (D-047, 29.09.2026).

## Cel projektu
Canon RP kurs jest profesjonalnym kursem nauki fotografii i obsługi Canon EOS RP.
Pierwszą użytkowniczką jest Ania, ale projekt od początku ma standard produktu, który może później zostać rozwinięty i skomercjalizowany.

## Nadrzędne zasady pracy
1. Dokumentacja projektu jest źródłem prawdy. Przed zmianą przeczytaj dokumenty wskazane w aktualnym handoffie i statusie.
2. Nie zgaduj. Jeżeli czegoś nie wiesz, brakuje źródła, instrukcje są sprzeczne albo zakres jest niejasny — zatrzymaj się i zgłoś problem.
3. Nie rozszerzaj zakresu zadania bez zgody.
4. Nie zmieniaj zaakceptowanych elementów poza zakresem zadania.
5. Nie stosuj rozwiązań „byle działało”, jednorazowych hacków ani prowizorek, jeśli wymaganie ma być częścią wzorca dla kolejnych lekcji.
6. Kod, UX, treść, assety i struktura danych mają być utrzymywalne, powtarzalne i skalowalne.
7. Codex jest wykonawcą technicznym. Nie wymyśla samodzielnie finalnej treści edukacyjnej ani nie zmienia kolejności dydaktycznej bez zatwierdzenia.
8. Rzeczywisty Canon EOS RP Ani, zatwierdzone materiały projektu i oficjalne materiały Canon są źródłami prawdy dla obsługi aparatu.
9. Identyfikatory produkcyjne typu L1-xx, Sxx, Vxx nigdy nie mogą trafić do widocznej warstwy użytkowej.
10. Każdy element aparatu użyty w instrukcji dla Ani musi być pokazany na zweryfikowanym materiale i wyjaśniony prostym językiem.

## Obowiązkowy protokół implementacji
Dla każdego zadania implementacyjnego użyj skilla:
`$canon-rp-precision`

Nie pomijaj żadnego etapu tego workflow.

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

## Commit / push / publikacja
Nie wykonuj commit, push ani publikacji, jeżeli zadanie lub handoff ustanawia punkt zatrzymania przed którymkolwiek z tych działań.
Jeżeli nie ma jednoznacznej zgody, zatrzymaj się i raportuj stan.

## Standard jakości
Mały zakres funkcji jest dopuszczalny. Niski standard wykonania — nie.
Projekt ma być tworzony profesjonalnie od początku.
