# Automatyzacja procesów z wykorzystaniem Makefile

## Opis

Ten projekt zawiera prostą aplikację w Pythonie oraz Makefile, który automatyzuje procesy testowania i uruchamiania aplikacji.

## Struktura projektu

- `app.py` - główny plik aplikacji
- `test_app.py` - plik testów jednostkowych
- `Makefile` - plik zawierający reguły do automatyzacji procesów

## Jak uruchomić

1. Skopiuj pliki `app.py`, `test_app.py` i `Makefile` do lokalnego katalogu.
2. Utwórz plik `requirements.txt` z wymaganymi bibliotekami (jeśli są).
3. Uruchom instalację zależności:
    ```bash
    make install
    ```
4. Uruchom testy jednostkowe:
    ```bash
    make test
    ```
5. Uruchom aplikację:
    ```bash
    make run 
    ```
6. Możliwe jest kaskadowe wykonanie komend za pomocą komendy:
    ```bash
    make run 
    ```