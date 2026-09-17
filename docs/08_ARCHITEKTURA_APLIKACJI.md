# Architektura aplikacji — wymagania i kierunek

Status: opis koncepcyjny. Nie wybrano frameworka, hostingu, bazy danych ani sposobu logowania. Nie ma kodu aplikacji.

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
