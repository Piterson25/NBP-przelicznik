import requests


def get_usd_rating():
    usd_iso_code = 'USD'
    table = 'A'

    response = requests.get(f"https://api.nbp.pl/api/exchangerates/rates/{table}/{usd_iso_code}/today/?format=json").json()
    currency_rate = response["rates"][0]["mid"]
    return float(currency_rate)


def get_gold_rating():
    response = requests.get(f"https://api.nbp.pl/api/cenyzlota?format=json").json()
    gold_rate = response[0]["cena"]
    return float(gold_rate)


def pln_to_usd(usd_rating, gold_rating):
    pln = round(float(input("Podaj ilość złotówek do przeliczenia na dolary i złoto: ")), 2)
    print(f"{pln}zł to {round(pln / usd_rating, 2)}$ lub {round(pln / (gold_rating * 1000), 10)}kg złota")


def usd_to_pln(usd_rating, gold_rating):
    usd = round(float(input("Podaj ilość dolarów do przeliczenia na złotówki i złoto: ")), 2)
    print(f"{usd}$ to {round(usd * usd_rating, 2)}zł lub {round(usd * usd_rating / (gold_rating * 1000), 10)}kg złota")


def main():
    usd_rating = get_usd_rating()
    print(f"Kurs dolara: {usd_rating}")

    gold_rating = get_gold_rating()
    print(f"Cena złota: {gold_rating}\n")

    print("1. przeliczanie złotówek na dolary\n2. przeliczanie dolarów na złotówki\n")
    choice = int(input("Wybierz rodzaj przeliczenia: "))

    while choice != 1 and choice != 2:
        choice = int(input("Niepoprawny wybór, spróbuj jeszcze raz: "))

    if choice == 1:
        pln_to_usd(usd_rating, gold_rating)
    else:
        usd_to_pln(usd_rating, gold_rating)


if __name__ == "__main__":
    main()
