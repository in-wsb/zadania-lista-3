import requests

# Funkcja do sprawdzania kluczowych elementów w odpowiedzi JSON
def check_elements(data, elements):
    for element in elements:
        if element not in data:
            return False
    return True

# Lista endpointów do testowania
endpoints = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/posts/3'
]

# Elementy, które powinny być obecne w odpowiedzi JSON
required_elements = ['userId', 'id', 'title', 'body']

# Testowanie endpointów
for i, endpoint in enumerate(endpoints):
    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        if check_elements(data, required_elements):
            print(f"Test {i + 1}: PASSED")
        else:
            print(f"Test {i + 1}: FAILED - Missing elements")
    else:
        print(f"Test {i + 1}: FAILED - HTTP Status {response.status_code}")
