# Mój nauczyciel / Analiza mojego zdjęcia

Status: zaakceptowany moduł docelowego kursu. Implementacja jest późniejszym etapem.

## Cel

Ania dodaje zdjęcie po ćwiczeniu albo własne zdjęcie niezależnie od lekcji. Nauczyciel pomaga zrozumieć wynik i wykonać lepszą kolejną próbę. Analizuje fotografię w kontekście zasad i treści kursu.

**Doprecyzowanie 18.09.2026 (D-24):** Ania może dodawać zarówno nowe zdjęcia z Canon EOS RP, jak i swoje wcześniejsze fotografie, również wykonane innym aparatem lub telefonem. Zdjęcie nie musi pochodzić z ćwiczenia ani zawierać danych EXIF. Nie zakładamy, że zostało wykonane zestawem EOS RP + RF 50 mm F1.8 STM.

To współpraca z nauczycielem AI: Ania pokazuje zdjęcie, może opowiedzieć o swoim zamiarze i dopytać o wskazówki. AI pomaga dostrzec, co działa, co przeszkadza w zamierzonym efekcie i czego warto spróbować. Może omówić kolejną próbę, jeśli Ania ją doda. Bez egzaminowania i narzucania jednego „poprawnego” gustu. Sposób prowadzenia rozmowy i przechowywania jej historii pozostaje do ustalenia przy implementacji.

## Wejście

- Zdjęcie przygotowane do analizy.
- Cel lekcji lub odpowiedź Ani na „Co chciałaś osiągnąć?”, gdy brak kontekstu.
- Poziom i istotny, ograniczony kontekst postępów.
- Programowo odczytane dane zdjęcia: aparat, obiektyw, ogniskowa, czas, przysłona, ISO — wyłącznie dostępne pola.
- Zasady języka nauczyciela oraz lista rzeczywiście istniejących, odpowiednich lekcji.

Metadane odczytujemy przed usunięciem zbędnych danych z kopii wysyłanej do AI. Brak pola nie jest wartością zero. Metadane mogą być niepełne lub zmodyfikowane; nauczyciel mówi „według danych pliku”, gdy to istotne.

Przy braku danych sprzętu i ustawień nadal omawiamy widoczną treść zdjęcia, np. kompozycję, światło i tło, w granicach jakości materiału. Nie odgadujemy modelu aparatu, parametrów ani pewnej przyczyny problemu. Wskazówki do kolejnej próby na Canonie Ani odróżniamy od ustaleń o tym, jak powstało wcześniejsze zdjęcie.

## Odpowiedź

1. Co wyszło dobrze.
2. Co warto poprawić — najwyżej jedna lub dwie rzeczy.
3. Co prawdopodobnie było przyczyną, z wyraźnym zaznaczeniem niepewności.
4. Co zrobić przy następnym zdjęciu.

Opcjonalnie: odnośnik do istniejącej lekcji lub ćwiczenia. Bez punktacji „6/10”, wymyślonych parametrów i stwierdzania pewnej przyczyny na podstawie niejednoznacznego obrazu. Nieczytelne zdjęcie oznacza prośbę o lepszy materiał, a nie pozornie dokładną diagnozę.

## Model — kierunek roboczy

W końcowej części rozmowy GPT-6 Astra został wskazany jako preferowany model referencyjny. Wcześniejsza propozycja automatycznego przełączania Terra → Sol → Astra nie jest przyjętą architekturą startową. Przed integracją sprawdzimy dostęp na koncie, jakość na rzeczywistych zdjęciach i koszt. [Zweryfikowane informacje o API](11_AI_API_BEZPIECZENSTWO.md).

## Później

Rozpoznawanie powtarzających się trudności, dobór kolejnego ćwiczenia i samodzielny nauczyciel poza kursem. W rozmowie pojawiły się trzy możliwe tryby: „Pomóż mi poprawić to zdjęcie”, „Czego mogę się nauczyć?” oraz „Daj następne ćwiczenie”. To propozycje rozwoju, nie wymaganie budowy trzech trybów od razu.

## Próby akceptacyjne przed uruchomieniem

Sprawdzimy zdjęcie z kompletnymi danymi, bez EXIF, z częściowymi danymi, nieostre lub bardzo małe, przypadek niejednoznaczny, brak powiązanej lekcji, brak internetu oraz wyczerpany budżet API. Nauczyciel ma zachować prosty język, granice wnioskowania i maksymalnie dwa zalecenia. Błąd usługi nie może oznaczać utraty postępu w kursie.

Próby obejmą też wcześniejsze zdjęcie z innego aparatu lub telefonu, zdjęcie o nieznanym pochodzeniu sprzętowym oraz pytanie uzupełniające Ani. Sprawdzimy, czy AI uwzględnia jej zamiar, nie przypisuje zdjęciu sprzętu EOS RP bez danych i potrafi pomóc bez wymuszania związku z lekcją.
