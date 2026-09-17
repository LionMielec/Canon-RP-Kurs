# AI / API / bezpieczeństwo

Status: wymagania dla przyszłej integracji, bez aktywowania usługi i bez płatności. Weryfikacja źródeł: 17.09.2026.

## Uzgodniona granica

Klucz API nie trafia do telefonu, kodu przeglądarki, repo ani dokumentacji. Model wywołuje warstwa serwerowa. Projekt API Canon-RP-Kurs ma mieć osobne rozliczenie zużycia i zatwierdzony budżet. Subskrypcji ChatGPT nie traktujemy jako budżetu API aplikacji.

OpenAI zaleca przechowywanie kluczy przez zmienne środowiskowe lub magazyn sekretów. W projekcie oznacza to sekrety serwera, a nie zmienne dołączane do publicznego kodu klienta. Nie prosimy o wklejanie kluczy do rozmowy. [Production best practices](https://developers.openai.com/api/docs/guides/production-best-practices).

## Minimalne wymagania przed uruchomieniem

- Kontrola dostępu do analizy, aby prywatny klucz nie finansował otwartego endpointu.
- Sprawdzenie typu i rozmiaru pliku przed analizą; konkretne limity do ustalenia.
- Odczyt potrzebnych danych fotograficznych, następnie usunięcie zbędnych metadanych, w szczególności lokalizacji GPS, z kopii wysyłanej modelowi.
- Świadome wysłanie zdjęcia do zewnętrznej usługi. Zdjęcia nie trafiają automatycznie do Git ani do logów.
- Określony czas przechowywania i sposób usunięcia zdjęć oraz analiz; jeszcze bez wyboru magazynu danych.
- Ograniczenie liczby analiz, wielkości wejścia, odpowiedzi i ponowień po stronie serwera.
- Zapis modelu, zużycia, szacowanego kosztu i statusu żądania, bez sekretów i pełnych prywatnych treści.
- Treść zdjęć i metadanych traktowana jako dane, a nie polecenia zmieniające zasady nauczyciela.
- Obsługa błędów usługi bez utraty postępów kursu.

To wymagania bezpieczeństwa do dopracowania przy integracji, nie implementowany teraz subsystem.

## Kontrola wydatków

Według aktualnej dokumentacji OpenAI alert wydatków informuje, ale nie blokuje ruchu. Twardy limit organizacji lub projektu wymaga włączenia egzekwowania. Po osiągnięciu śledzonego wydatku usługa zwraca odpowiedni błąd 429. Egzekwowanie nie jest natychmiastowe i koszt może nieznacznie przekroczyć limit. [Spend limits](https://developers.openai.com/api/docs/guides/spend-limits).

Przed uruchomieniem sprawdzamy ustawienia konkretnego konta. Propozycje salda 5–10 USD, limitu 10 USD/miesiąc i wyłączenia automatycznego doładowania pozostają propozycjami do zatwierdzenia. Nie przyjmujemy wcześniejszego zapewnienia o zerowym ryzyku dodatkowego kosztu.

## Model i szacunek

Karta GPT-6 Astra potwierdza wejście obrazowe oraz bazowe stawki tekstowe Standard: 10 USD / mln tokenów wejścia i 50 USD / mln tokenów wyjścia. Warunki dla długiego kontekstu i innych trybów cenowych są inne; dostępność na koncie trzeba sprawdzić osobno. [Karta GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra).

Wyłącznie przykład arytmetyczny: przy 2000 płatnych tokenów wejścia i 800 płatnych tokenów wyjścia analiza kosztowałaby 0,06 USD, a 42 takie analizy — 2,52 USD. Nie jest to pomiar zdjęć Ani. Założenie musi obejmować całe rozliczane wejście i wyjście, a rzeczywisty koszt zależy również od przetwarzania obrazu, rozumowania i ponowień. Przed przyjęciem budżetu wykonamy zatwierdzoną małą próbę i odczytamy faktyczne zużycie.

W tym etapie nie tworzymy klucza, nie zmieniamy ustawień konta i nie uruchamiamy płatnych analiz.
