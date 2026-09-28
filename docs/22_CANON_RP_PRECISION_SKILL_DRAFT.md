---
name: canon-rp-precision
description: Precyzyjny workflow implementacyjny dla projektu Canon RP kurs. Używaj przy każdej zmianie kodu, danych, UI, assetów lub zachowania aplikacji, aby ściśle trzymać się dokumentacji, zakresu, faktycznego renderowanego rezultatu i punktów akceptacji.
---

# Canon RP Precision

## Cel
Wykonuj zadania w Canon RP kurs precyzyjnie, bez zgadywania, bez samowolnego rozszerzania zakresu i bez zgłaszania sukcesu przed zweryfikowaniem faktycznego efektu w aplikacji.

## 1. Najpierw ustal zakres
Przed zmianą:
1. Przeczytaj aktualny handoff, status, decyzje i dokumenty wskazane w zadaniu.
2. Napisz krótko:
   - **Rozumiem zakres:** co dokładnie ma zostać zmienione.
   - **Nie zmieniam:** elementy, które pozostają nietknięte.
   - **Źródło prawdy:** dokumenty, pliki i dane, na których się opierasz.
   - **Punkt zatrzymania:** gdzie masz przerwać i poprosić o akceptację.

Jeśli nie potrafisz jednoznacznie wypełnić któregokolwiek z tych punktów — nie implementuj. Zgłoś niejasność.

## 2. Znajdź rzeczywiste źródło renderowanej aplikacji
Zanim zmienisz treść lub UI:
1. Ustal, z jakiego konkretnego pliku/danych komponent faktycznie renderuje daną treść.
2. Nie zakładaj, że dokumentacja, kopia tekstu lub podobnie nazwany plik jest źródłem runtime.
3. Jeśli trzeba, przeszukaj projekt po aktualnie wyświetlanej frazie.
4. Potwierdź ścieżkę źródłową przed modyfikacją.

## 3. Wprowadzaj wyłącznie zatwierdzoną zmianę
- Nie poprawiaj „przy okazji” innych rzeczy.
- Nie zmieniaj stylu, treści, nawigacji, architektury ani danych poza zakresem.
- Jeśli wymaganie ma obowiązywać wiele lekcji, implementuj je jako wspólny, utrzymywalny mechanizm — nie jako jednorazowy wyjątek.
- Nie obniżaj jakości dlatego, że obecnie projekt ma jedną użytkowniczkę.

## 4. Zweryfikuj faktyczny rezultat
Po implementacji nie kończ na sprawdzeniu plików ani testach automatycznych.

Obowiązkowo:
1. Uruchom faktyczny lokalny podgląd.
2. Otwórz dokładny ekran/ścieżkę, której dotyczy zmiana.
3. Sprawdź, że renderowana aplikacja pokazuje nowy stan.
4. Sprawdź, że wcześniej zaakceptowane elementy poza zakresem nie zostały naruszone.
5. Dla zmian wizualnych przygotuj właścicielowi bezpośredni link do właściwego lokalnego ekranu.

Jeśli nie możesz zweryfikować wizualnie lub funkcjonalnie danego elementu, napisz wprost: **NIEZWERYFIKOWANE**.

## 5. Testy
Wykonuj testy odpowiednie do zmiany, ale nigdy nie traktuj ich jako zamiennika odbioru wizualnego.

Dla UI/mobile, gdy dotyczy:
- responsywność,
- iPhone 15 Pro Max,
- docelowy rozmiar iPhone Ani,
- desktop,
- brak poziomego scrolla,
- brak błędów JavaScript i błędów ładowania,
- prefers-reduced-motion,
- poprawne skalowanie i pozycjonowanie overlayów/markerów,
- brak technicznych ID w warstwie użytkowej.

Raportuj wyraźnie, które testy są:
- automatyczne,
- przeglądarkowe,
- emulowane,
- wykonane na fizycznym urządzeniu.

Nie przedstawiaj emulacji jako testu fizycznego telefonu.

## 6. Raport po pracy
Raport zawsze ma tę strukturę:

### Zmieniłem
Konkretne pliki i zachowania.

### Nie zmieniłem
Elementy chronione przez zakres zadania.

### Zweryfikowałem w faktycznej aplikacji
Co dokładnie otwarto i co rzeczywiście widać/działa.

### Testy techniczne
Jakie testy wykonano i z jakim wynikiem.

### Ograniczenia / niezweryfikowane
Wszystko, czego nie dało się potwierdzić.

### Stan repozytorium i publikacji
- commit: TAK/NIE
- push: TAK/NIE
- publish: TAK/NIE

## 7. Punkty zatrzymania
Jeżeli zadanie mówi „pokaż lokalnie przed publikacją”:
- nie commituj, jeśli nie ma zgody,
- nie pushuj,
- nie publikuj,
- pokaż lokalny rezultat i zatrzymaj się.

Jeżeli właściciel zaakceptuje lokalny rezultat, wykonaj tylko kolejny wyraźnie zatwierdzony etap.

## 8. Zasady bezpieczeństwa jakości
Zatrzymaj się zamiast zgadywać, gdy:
- dokumentacja i kod są sprzeczne,
- nie wiadomo, która wersja pliku jest aktualna,
- zmiana wymaga assetu, którego nie ma,
- rezultat wymaga decyzji wizualnej lub dydaktycznej właściciela,
- wdrożenie wymaga rozszerzenia zakresu,
- techniczne wykonanie byłoby prowizoryczne albo tworzyłoby oczywisty dług techniczny.

## 9. Definicja „wykonane”
Możesz napisać „wykonane” tylko wtedy, gdy:
1. zmiana jest w rzeczywistym źródle aplikacji,
2. aplikacja została uruchomiona,
3. właściwy ekran został faktycznie sprawdzony,
4. wymagane testy przeszły,
5. wszystkie ograniczenia są jawnie opisane,
6. osiągnięto dokładnie etap, na który była zgoda.

Jeżeli któregokolwiek warunku brakuje, użyj dokładniejszego statusu, np.:
- „zaimplementowane, ale niezweryfikowane wizualnie”,
- „zweryfikowane lokalnie, nieopublikowane”,
- „opublikowane, czeka na test fizycznego iPhone’a”.
