from pathlib import Path
import json
import csv


from Conventer.logger_config import setup_logger


def storage(date, to_currency):
    BASE_DIR = Path(__file__).resolve().parent


    data_dir = BASE_DIR / "data"
    data_dir.mkdir(exist_ok=True)


    file_path1 = data_dir / "converter_info.json"
    file_path2 = data_dir / "converter_info.csv"


    data = date


    with open(file_path1, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)

        setup_logger().info(f"The file is saved at: {file_path1}")


    with open(file_path2, 'w', encoding="cp1251", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(["From", "To", "Amount", "Date", "Rates"])


    with open(file_path2, 'a', encoding="cp1251", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow([data["base"], to_currency, data["amount"], data["date"], data["rates"][f"{to_currency}"]])

        setup_logger().info(f"The file is saved at: {file_path2}")
