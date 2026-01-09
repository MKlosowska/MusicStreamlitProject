# Analiza utworów artysty (iTunes)

Aplikacja webowa umożliwiająca analizę utworów muzycznych wybranego artysty na podstawie danych pobieranych z iTunes Search API. Pozwala na przeglądanie listy utworów, analizę najnowszych wydań oraz wizualizację statystyk dotyczących długości utworów, lat wydania i gatunków muzycznych.

Projekt pozwala w prosty i czytelny sposób:
- przeglądać wszystkie utwory danego artysty,
- sprawdzić jego najnowsze wydania,
- analizować długość utworów, lata wydania oraz gatunki muzyczne.

---

## Opis plików projektu

### app.py
Główny plik aplikacji Streamlit.

- uruchamia aplikację webową,
- odpowiada za interfejs użytkownika,
- pobiera nazwę artysty z panelu bocznego,
- wywołuje pobieranie i analizę danych,
- dzieli aplikację na zakładki:
  - Wszystkie utwory
  - Najnowsze utwory
  - Analiza utworów
  - Analiza gatunków,
- wyświetla tabele oraz wykresy,
- formatuje dane (numeracja, nazwy kolumn, ukrycie indeksu).

---

### sources.py
Plik odpowiedzialny za pobieranie danych z zewnętrznego API.

- definiuje klasę `Track`, reprezentującą pojedynczy utwór,
- zawiera klasę `ITunesSource`,
- wysyła zapytania HTTP do iTunes Search API,
- przetwarza odpowiedź API na listę obiektów `Track`.

---

### analysis.py
Moduł analizy i przetwarzania danych.

- konwertuje dane do obiektu DataFrame (`to_df`),
- filtruje utwory po artyście,
- oblicza podstawowe statystyki (KPI),
- wybiera najnowsze utwory,
- analizuje:
  - długość utworów,
  - lata wydania,
  - gatunki muzyczne,
- przygotowuje dane do dalszej wizualizacji.

---

### plots.py
Plik pomocniczy do wizualizacji danych.

- zawiera funkcje przygotowujące dane do wykresów,
- oddziela logikę analizy od prezentacji,
- obsługuje wykresy:
  - histogram długości utworów,
  - liczbę utworów wg lat,
  - top gatunki,
  - trendy gatunkowe,
  - średnią długość utworów wg gatunku.

---

### decorators.py
Plik z dekoratorami pomocniczymi.

- zawiera dekorator `timer`,
- umożliwia pomiar czasu wykonania funkcji,
- używany do debugowania i optymalizacji.

---

### test_analysis.py
Plik z testami jednostkowymi.

- testuje kluczowe funkcje analizy danych,
- sprawdza poprawność:
  - filtrowania danych,
  - obliczeń statystyk,
  - wyboru najnowszych utworów,
  - analizy gatunków,
- umożliwia szybką weryfikację poprawności kodu.

---

### requirements.txt
Lista wymaganych bibliotek.

- streamlit
- pandas
- requests
- pytest

Plik wykorzystywany do instalacji zależności projektu.

---

## Technologie

- **Python**
- **Streamlit**
- **Pandas**
- **Requests**
- **iTunes Search API**
