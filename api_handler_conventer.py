import requests


from Conventer.logger_config import setup_logger



def handler(fromcurrency, tocurrency, amount):
    try:
        response = requests.get(f"https://api.frankfurter.dev/v1/latest?from={fromcurrency}&to={tocurrency}&amount={amount}")
        response.raise_for_status()
        setup_logger().info("Data received successfully!")

        return response.json()

    except requests.exceptions.HTTPError as e:
        setup_logger().error(f"HTTP error: {e.response.status_code} — {e.response.reason}")
        return None

    except requests.exceptions.ConnectionError:
        setup_logger().error("Connection error. Check your internet connection or URL.")
        return None

    except requests.exceptions.Timeout:
        setup_logger().error("The timeout period for waiting for a response from the server has expired.")
        return None

    except Exception as e:
        setup_logger().error(f"Unexpected error: {type(e).__name__} — {e}")
        return None
