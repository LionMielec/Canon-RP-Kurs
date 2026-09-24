# Standard produkcji lekcji — Canon RP kurs

Data: 2026-09-24  
Status: ZATWIERDZONY  
Obowiązuje: od L1-01 i dla wszystkich kolejnych lekcji

## 1. Zasada

Każda lekcja powstaje od początku jako kompletny pakiet edukacyjno-produkcyjny. Nie przygotowujemy najpierw samego tekstu, a dopiero później warstwy wizualnej.

Każda lekcja ma równolegle dwie warstwy:

1. **Treść dla Ani** — finalna treść edukacyjna, ćwiczenie i sprawdzenie efektu.
2. **Warstwa produkcyjna** — niewidoczna jako zwykła treść kursu; zawiera identyfikatory kroków, potrzebne zdjęcia, ekrany, grafiki, animacje/3D, ich cel, źródła, status i instrukcje dla Codexa.

Standard obowiązuje już od **L1-01**. Nie zaczyna się od L1-02.

## 2. Identyfikatory

Każdy istotny krok lekcji otrzymuje stały identyfikator, np.:

- `L1-01-S01` — krok 1,
- `L1-01-S02` — krok 2.

Każdy materiał wizualny otrzymuje osobny identyfikator, np.:

- `L1-01-V01` — pierwszy materiał wizualny,
- `L1-01-V02` — drugi materiał wizualny.

Po zatwierdzeniu identyfikatory pozostają stałe, aby treść, assety i implementacja były jednoznacznie powiązane.

## 3. Co zapisujemy dla każdego materiału

Każdy materiał wizualny musi mieć:

- ID,
- powiązany krok lekcji,
- dokładne miejsce użycia,
- typ: zdjęcie aparatu Ani / prawdziwy ekran lub menu / grafika / animacja / 3D / porównanie zdjęć,
- cel dydaktyczny,
- źródło prawdy,
- opis tego, co ma być widoczne,
- sposób prezentacji,
- status produkcyjny,
- uwagi dla Codexa.

## 4. Statusy produkcyjne

- `AVAILABLE` — materiał istnieje i został zweryfikowany,
- `TO_SELECT` — mamy materiał źródłowy, trzeba wybrać finalny,
- `TO_CAPTURE` — trzeba wykonać zdjęcie lub rzeczywisty ekran z aparatu Ani,
- `TO_DESIGN` — trzeba przygotować grafikę,
- `TO_ANIMATE` — trzeba przygotować animację/3D,
- `TO_VERIFY` — materiał wymaga kontroli zgodności,
- `APPROVED` — materiał zatwierdzony do implementacji.

Brakującego materiału Codex nie zastępuje własnym zamiennikiem.

## 5. Dobór formy

Stosujemy najprostszą formę, która skutecznie uczy:

1. zdjęcie lub prawdziwy ekran,
2. prosta grafika,
3. krótka animacja,
4. 3D tylko wtedy, gdy realnie poprawia zrozumienie.

Materiał nie może być wyłącznie dekoracyjny.

## 6. Zasady dla Codexa

Codex:

- implementuje zatwierdzoną kolejność i identyfikatory,
- osadza materiały przy wskazanych krokach,
- nie zmienia samodzielnie ich roli dydaktycznej,
- nie przesuwa materiałów w inne miejsca bez decyzji projektowej,
- nie odtwarza wyglądu EOS RP ani menu z domysłu,
- dla brakującego assetu pozostawia jawny placeholder produkcyjny,
- umożliwia późniejszą wymianę assetu bez przebudowy treści lekcji.

## 7. Co powstaje dla każdej lekcji

Dla każdej lekcji przygotowujemy:

- finalną treść dla Ani,
- listę kroków z ID,
- ćwiczenie,
- sposób sprawdzenia efektu,
- kartę wizualno-produkcyjną,
- listę assetów ze statusami,
- instrukcje montażu dla Codexa.

## 8. Kolejność pracy

**research źródeł → treść → ćwiczenie → kontrola techniczna na EOS RP → projekt warstwy wizualnej → karta produkcyjna → akceptacja → produkcja assetów → zatwierdzenie assetów → implementacja przez Codexa**

Warstwę wizualną projektujemy równolegle z treścią każdej lekcji, począwszy od L1-01.
