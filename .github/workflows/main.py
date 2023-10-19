# Define fixed conversion rates (as of the knowledge cutoff date)
conversion_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.73,
    'JPY': 112.47,
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in conversion_rates or to_currency not in conversion_rates:
        return "Currency not supported."

    conversion_rate = conversion_rates[to_currency] / conversion_rates[from_currency]
    converted_amount = amount * conversion_rate

    return f"{amount} {from_currency} is equal to {converted_amount} {to_currency}"

if __name__ == "__main__":
    while True:
        amount = float(input("Enter the amount: "))
        from_currency = input("From Currency (e.g., USD, EUR): ").upper()
        to_currency = input("To Currency (e.g., USD, EUR): ").upper()

        result = convert_currency(amount, from_currency, to_currency)
        print(result)

        another = input("Do you want to convert another currency? (yes/no): ")
        if another.lower() != 'yes':
            break
