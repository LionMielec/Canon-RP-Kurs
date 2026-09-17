# Plan materiałów

## Stan początkowy

Początkowo lokalny katalog materiałów projektu ChatGPT był pusty. Na późniejsze polecenie użytkownika 17.09.2026 pobrano do właściwego repo dwie instrukcje PDF (PL i EN) oraz zapisano katalog 17 materiałów edukacyjnych online. Zdjęcia i klipy nie zostały jeszcze dostarczone. Rejestr oraz ograniczenia wydań znajdują się w [materials/README.md](../materials/README.md).

## Kategorie

| Katalog | Zawartość i rola |
| --- | --- |
| `canon-official/` | Rejestr oficjalnych instrukcji i materiałów kontrolnych |
| `camera-photos/` | Własny aparat: przód, tył, góra, lewy i prawy bok, spód |
| `menu-screens/` | Autentyczne ekrany polskiego menu, Q i fotografowania |
| `example-photos/` | Własne przykłady, porównania przed / po, zdjęcia do ćwiczeń |
| `animations/` | Krótkie klipy wskazujące aparat, przycisk lub pokrętło |

## Zdjęcia egzemplarza do dostarczenia

- Sześć stron korpusu, z czytelnymi przyciskami, pokrętłami i złączami.
- Aparat z obiektywem, którego Ania będzie używać najczęściej.
- Obiektyw: pełna nazwa, przełączniki i pierścienie.
- Ekrany według [planu menu](05_MAPA_MENU_CANON_RP.md), w tym wersja firmware.

Nie znamy jeszcze modelu obiektywu. RF 50 mm z wcześniejszych przykładów nie jest potwierdzonym wyposażeniem Ani. Oryginały zdjęć zachowujemy osobno; ewentualne kadrowanie i oznaczenia powstają na kopiach.

## Animacje

Uzgodniony pomysł: krótki obrót lub zbliżenie → wskazanie elementu → przejście do prawdziwego ekranu → zaznaczenie opcji → efekt na fotografii. Higgsfield jest rozważanym narzędziem do klipów, a nie źródłem tekstów menu. Nie uruchamiamy usługi ani nie kupujemy dostępu na tym etapie.

Każdy klip wymaga porównania z własnymi zdjęciami RP: położenie i kształt przycisków, pokręteł, oznaczeń oraz ciągłość ruchu. Wymyślony element aparatu dyskwalifikuje materiał instruktażowy. Interaktywny model 3D pozostaje możliwością na później.

## Prosty rejestr zamiast systemu zarządzania mediami

Dla materiału zapisujemy: ID, nazwę pliku, autora lub źródło, datę, zgodę lub warunki użycia, cel, docelową lekcję, lokalizację oryginału i status weryfikacji. Ekrany menu dodatkowo otrzymują tryb, firmware i język.

Robocze nazwy mogą wyglądać tak: `rp-body-back-001.jpg`, `rp-menu-photo-m-page-01.jpg`, `portrait-background-before-001.jpg`. To konwencja katalogowania, nie istniejące pliki.

## Przechowywanie

Git przechowuje teraz dokumenty i rejestry. Zdjęcia, filmy, PDF i pliki lokalne pod `materials/` są domyślnie ignorowane; do repo dopuszczone są opisy `.md` i znaczniki katalogów. Gdy wybierzemy materiał do aplikacji, świadomie zdecydujemy o jego miejscu, prawach i rozmiarze. Nie instalujemy teraz Git LFS ani magazynu plików.

Oficjalne źródła zapisujemy jako linki, a pobrane instrukcje przechowujemy lokalnie w `materials/canon-official/`, poza śledzeniem Git. Nie zakładamy, że znalezienie zdjęcia lub PDF oznacza zgodę na jego publikację. Własne fotografie Ani nie trafiają automatycznie na GitHub.
