# Canon RP — pakiet źródłowych zdjęć aparatu i menu

Data materiałów: 24.09.2026
Przygotowano: 25.09.2026

## Co zawiera pakiet
- `raw/` — 27 unikalnych oryginalnych zdjęć z pakietu przekazanego do ChatGPT.
- `selected/` — kopie dwóch zdjęć już jednoznacznie przypisanych w dokumentacji do konkretnych assetów.
- `MANIFEST.csv` — nazwa pliku, Library ID, rozmiar, wymiary, SHA-256 i znane zastosowanie.

W Bibliotece były 47 wpisów JPG z tej sesji; 20 z nich było ponownymi kopiami tych samych nazw/plikiem z dopiskiem `(1)`. Do pakietu weszło 27 unikalnych źródeł.

## Twarde przypisania
- L1-01-V01 / L1-01-V02: `raw/fbe2fd62-e8ab-465b-b340-b6d0b4458622.jpg` — jedyny dozwolony master dla ON/OFF i A+.
- L1-02-V03: `raw/57652b89-ae48-4cd1-b998-e883aee8aa1f.jpg` — wybrane źródło przycisku odtwarzania na tylnej ściance.

## Zasada dla Codexa
Ten pakiet jest lokalną biblioteką źródłową. Codex ma używać zdjęć wyłącznie wtedy, gdy konkretne źródło zostało przypisane w dokumentacji/ASSET_MANIFEST. Nie wybiera sam zamienników i nie publikuje całego katalogu w aplikacji.

## Docelowe miejsce na Macu
Rozpakować do:
`/Users/pawelsiedleczka/Documents/ChatGPT/Canon-RP-Kurs/materials/camera-source-pack-2026-09-24/`

Katalog `materials/` jest wykluczony z Git w tym repozytorium, więc prywatne zdjęcia nie powinny zostać przypadkowo wypchnięte do GitHub.
