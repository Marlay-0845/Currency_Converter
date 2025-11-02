import requests


def handler(fromcurrency, tocurrency, amount):
    try:
        response = requests.get(f"https://api.frankfurter.dev/v1/latest?from={fromcurrency}&to={tocurrency}&amount={amount}")
        response.raise_for_status()
        print("Данные получены успешно!")

    except requests.exceptions.HTTPError as e:
        print(f"❌ Ошибка HTTP: {e.response.status_code} — {e.response.reason}")

    except requests.exceptions.ConnectionError:
        print("❌ Ошибка соединения. Проверьте интернет или URL.")

    except requests.exceptions.Timeout:
        print("❌ Истекло время ожидания ответа от сервера.")

    except Exception as e:
        print(f"⚠️ Непредвиденная ошибка: {type(e).__name__} — {e}")

    return response.json()
