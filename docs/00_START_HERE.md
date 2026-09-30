# Zacznij tutaj

**Stan 29.09.2026:** projekt pracuje w nowym układzie (D-047). Paweł podejmuje decyzje końcowe, Claude w czacie (projekt claude.ai) jest architektem i audytorem, Claude Code implementuje. Dokumentacja i kod aplikacji są w jednym repozytorium; kod w `app/dist/`.

## Najpierw przeczytaj
1. [14 — najnowszy handoff](14_PRZEKAZANIE_SESJI.md) — aktualny stan jest na końcu pliku
2. [09 — decyzje](09_DECISIONS.md) — najnowsze wpisy na końcu
3. [10 — zadania](10_TODO.md)
4. [15 — standard produkcji lekcji](15_STANDARD_PRODUKCJI_LEKCJI.md)
5. [16 — manifest assetów](16_ASSET_MANIFEST.md)
6. [12 — program Poziomu 1](12_PROGRAM_POZIOMU_1.md)

Zasady pracy agenta kodującego: `AGENTS.md`, `CLAUDE.md` i skill `.claude/skills/canon-rp-precision/SKILL.md`.

Zasady pracy Claude w czacie: [23 — zasady Claude w czacie](23_ZASADY_CLAUDE_W_CZACIE.md).

## Stan lekcji
- L1-01 i L1-02 — zatwierdzone, opublikowane, wzorzec redakcyjny i UX. Nieopublikowana mikrokorekta L1-02 (zmienia też wygląd L1-01) czeka na gałęzi `wip/l1-02-l1-03` na rozdzielenie i odbiór właściciela.
- L1-03 — treść i przebieg zaakceptowane lokalnie (gałąź `wip/l1-02-l1-03`); brakuje sześciu materiałów demonstracyjnych: V01, V02, V03, V04A, V04B, V05.
- L1-04–L1-14 — program roboczy, analizowany kolejno.

## Zasady, których nie otwieramy ponownie
- obecna ikona, kolorystyka i kierunek wizualny zostają,
- agent kodujący implementuje zatwierdzoną treść; nie wymyśla własnej,
- brakujących materiałów nie zastępujemy domysłem; generowane sceny tylko na warunkach D-050, nigdy sprzęt Ani ani ekrany menu,
- Ania nie produkuje materiałów, na których dopiero ma się uczyć,
- źródłowe zdjęcia aparatu i menu są lokalnie w `materials/camera-source-pack-2026-09-24/`,
- każda informacja w kursie ma sprawdzone, autentyczne źródło, niewidoczne dla Ani (D-048),
- publikacja jest wstrzymana do decyzji o hostingu (D-047).
