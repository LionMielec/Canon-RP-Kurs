# Architektura aplikacji — wymagania i kierunek

Status: od 18.09.2026 istnieje zatwierdzony minimalny szkielet aplikacji internetowej (D-18). Statyczne HTML/CSS/JavaScript i prywatny hosting Sites, bez frameworka, bazy i własnego logowania. Pozostałe wymagania poniżej opisują przyszły rozwój, nie obecne możliwości. Szczegóły: [13 — Pierwsza aplikacja](13_PIERWSZA_APLIKACJA.md).

## Kierunek z rozmowy

Aplikacja internetowa/PWA używana na iPhonie i komputerze. Częściowe działanie materiałów offline było propozycją, nie obietnicą pełnego działania bez internetu. Analiza przez zewnętrzne API wymaga połączenia.

## Minimalne granice odpowiedzialności

- Kurs prezentuje treści, zdjęcia, menu, klipy i ćwiczenia.
- Treści mają stabilne identyfikatory i powiązania, aby można było dokładać poziomy.
- Postępy zapisują ukończenie i miejsce powrotu; sposób przechowywania i synchronizacji pozostaje otwarty.
- Warstwa serwerowa obsługuje analizę zdjęcia i przechowuje sekret API.
- Zewnętrzny model dostaje zdjęcie, potrzebne dane i kontekst kursu; zwraca informację zwrotną.

Przepływ docelowy: Ania → aplikacja → serwer z kontrolą dostępu i kosztów → model → odpowiedź w kursie. To wymaganie dla późniejszej integracji, bez wdrażania serwera w etapie dokumentacyjnym.

## Co ustalić przed kodowaniem

1. Pierwszy fragment kursu i jego kryteria odbioru.
2. Obsługiwane urządzenia, wygoda czytania i odtwarzania instrukcji przy aparacie.
3. Miejsce materiałów i sposób zachowania oryginałów.
4. Zapis postępów: jeden sprzęt czy synchronizacja telefonu i komputera.
5. Dostęp do prywatnego kursu i usługi AI.
6. Zakres offline, rozmiar pobieranych materiałów i czytelne błędy.
7. Przechowywanie i usuwanie przesłanych zdjęć.
8. Technologia i hosting dopasowane do zatwierdzonego zakresu.

Nie budujemy na tym etapie wielu usług, systemu agentów, wyszukiwarki wektorowej, rozbudowanego panelu administracyjnego ani automatycznego routingu modeli. Ich potrzeba nie wynika z uzgodnionego celu.

## Pierwszy projekt wizualny — ustalenie 18.09.2026

Zaczynamy od widoku lekcji na telefonie. Urządzenie Ani: iPhone 17 Pro Max. Urządzenie użytkownika do prób: iPhone 15 Pro Max. Projekt należy dopasować do obu telefonów; test na jednym nie zastępuje sprawdzenia na drugim. To ustalenie urządzeń docelowych dla pierwszego projektu, bez wyboru technologii, hostingu lub zatwierdzenia implementacji. Wygląd i sposób nawigacji pozostają do wspólnego przeglądu.


## Standard inżynierski od początku

Projekt jest dziś prywatny, ale rdzeń ma być wykonany jak fundament produktu, który może być później rozwijany i komercjalizowany.

To oznacza:
- brak rozwiązań typu „byle działało” i brak świadomego długu technicznego bez uzasadnienia,
- czytelny podział danych lekcji, komponentów UI i assetów,
- spójne wzorce implementacyjne dla kolejnych lekcji zamiast kopiowania wyjątków,
- możliwość wymiany materiałów i rozbudowy programu bez przepisywania aplikacji,
- responsywność, dostępność, poprawne stany błędów i kontrolę jakości,
- testowanie rzeczywistych ścieżek użytkownika, nie tylko testów technicznych,
- dokumentowanie decyzji wpływających na przyszłą skalowalność.

Nie oznacza to budowania dziś systemów sprzedaży, multi-tenant, CMS, logowania klientów ani rozbudowanego backendu. **Profesjonalizm oznacza solidny rdzeń i właściwe granice odpowiedzialności, a nie maksymalną liczbę funkcji.**
