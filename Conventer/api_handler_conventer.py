import requests



def handler(fromcurrency, tocurrency, amount):
    try:
        response = requests.get(f"https://api.frankfurter.dev/v1/latest?from={fromcurrency}&to={tocurrency}&amount={amount}")
        response.raise_for_status()
        print("Data received successfully!")

        return response.json()

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e.response.status_code} — {e.response.reason}")
        return None

    except requests.exceptions.ConnectionError:
        print("Connection error. Check your internet connection or URL.")
        return None

    except requests.exceptions.Timeout:
        print("The timeout period for waiting for a response from the server has expired.")
        return None

    except Exception as e:
        print(f"Unexpected error: {type(e).__name__} — {e}")
        return None
