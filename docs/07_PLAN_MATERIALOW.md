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

W rozmowie ze zdjęciami potwierdzono obiektyw RF 50 mm F1.8 STM. Oryginały zdjęć zachowujemy osobno; ewentualne kadrowanie i oznaczenia powstają na kopiach.

## Animacje

Uzgodniony pomysł: krótki obrót lub zbliżenie → wskazanie elementu → przejście do prawdziwego ekranu → zaznaczenie opcji → efekt na fotografii. Higgsfield jest rozważanym narzędziem do klipów, a nie źródłem tekstów menu. Nie uruchamiamy usługi ani nie kupujemy dostępu na tym etapie.

Każdy klip wymaga porównania z własnymi zdjęciami RP: położenie i kształt przycisków, pokręteł, oznaczeń oraz ciągłość ruchu. Wymyślony element aparatu dyskwalifikuje materiał instruktażowy. Interaktywny model 3D pozostaje możliwością na później.

## Prosty rejestr zamiast systemu zarządzania mediami

Dla materiału zapisujemy: ID, nazwę pliku, autora lub źródło, datę, zgodę lub warunki użycia, cel, docelową lekcję, lokalizację oryginału i status weryfikacji. Ekrany menu dodatkowo otrzymują tryb, firmware i język.

Robocze nazwy mogą wyglądać tak: `rp-body-back-001.jpg`, `rp-menu-photo-m-page-01.jpg`, `portrait-background-before-001.jpg`. To konwencja katalogowania, nie istniejące pliki.

## Przechowywanie

Git przechowuje teraz dokumenty i rejestry. Zdjęcia, filmy, PDF i pliki lokalne pod `materials/` są domyślnie ignorowane; do repo dopuszczone są opisy `.md` i znaczniki katalogów. Gdy wybierzemy materiał do aplikacji, świadomie zdecydujemy o jego miejscu, prawach i rozmiarze. Nie instalujemy teraz Git LFS ani magazynu plików.

Oficjalne źródła zapisujemy jako linki, a pobrane instrukcje przechowujemy lokalnie w `materials/canon-official/`, poza śledzeniem Git. Nie zakładamy, że znalezienie zdjęcia lub PDF oznacza zgodę na jego publikację. Własne fotografie Ani nie trafiają automatycznie na GitHub.

## Aktualny kierunek animacji — 18.09.2026

Obowiązuje D-19: automatyczny start po wejściu w krok, obrót aparatu → zbliżenie → rzeczywiste działanie elementu. Bez konieczności naciskania „Odtwórz”. Obrys lub strzałka wskazuje dokładnie jeden element i podąża za nim. Duże kółka obecnej wersji są do zastąpienia.

Najpierw przygotować jedną animację wzorcową „Włącz aparat”, a kolejne dopiero po ocenie. Samo animowanie powiększenia zdjęcia nie wystarcza do pokazania ruchu przełącznika. Źródło klipu i narzędzie trzeba dopiero ustalić; brak nagrania/zweryfikowanego klipu jest otwartą potrzebą, nie zgodą na płatne generowanie.

Zdjęcia korpusu i obiektywu obejrzano w poprzedniej rozmowie. Potwierdzony zestaw: EOS RP + RF 50 mm F1.8 STM. Zdjęcie góry `780DC05E-6E96-4ADA-B67E-219B670E3C0A.jpeg` wykorzystano w prywatnej aplikacji jako `dist/camera-top.jpeg`. Cała seria nie została jeszcze uporządkowana w głównym katalogu materiałów. Nadal brak ekranów menu, firmware i testu na aparacie.

## Organizacja najbliższej sesji zdjęciowej — 18.09.2026

Obowiązuje D-21 i D-22. Kurs jest niespodzianką dla Ani. Paweł jest poza domem; instrukcje przekazuje jej przez telefon lub wiadomości. Ania sama fotografuje aparat telefonem, przesyła materiały Pawłowi, a on przekazuje je do oceny w rozmowie. Codex prowadzi sesję po jednym ujęciu: ustawienie aparatu, strona, kadr, wymagane widoczne elementy, następnie kontrola zdjęcia i ewentualna poprawka. Nie zakładać drugiego fotografa na miejscu.

Plan na 19.09.2026 po zgłoszeniu gotowości: zacząć od zdjęć ogólnych i szczegółów do dwóch istniejących lekcji — góra (ON/OFF, tryby, spust, pokrętło główne), tył (odtwarzanie, lupa, strzałki, Q/SET). Dalsze kadry i ekrany dobierać do potrzeb oraz możliwości Ani. Ujęcia chwytu obiema rękami i nagrania nie są obowiązkowym warunkiem tej sesji. Nie wymagać od Ani przygotowania docelowych animacji.

Zdjęcia są bazą wizualną i kontrolną; ich brak nie blokuje przygotowania tekstów na podstawie instrukcji. Docelowe animacje nadal realizują D-19: obrót, zbliżenie i działanie, automatycznie, z precyzyjnym wskazaniem. „Włącz aparat” sprawdza styl doświadczenia, nie trudność czynności. Sposób wykonania ruchu ustalimy osobno.
