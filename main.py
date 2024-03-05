import requests


def main():
    usd_iso_code = 'USD'
    table = 'A'

    response = requests.get(f"https://api.nbp.pl/api/exchangerates/rates/{table}/{usd_iso_code}/today/?format=json").json()

    currency_rate = response["rates"][0]["mid"]

    print(f"Kurs dolara: {currency_rate}")


if __name__ == "__main__":
    main()
