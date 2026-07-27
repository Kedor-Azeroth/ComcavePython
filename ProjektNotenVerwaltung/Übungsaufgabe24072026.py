def calculate_average(num1, num2):
    return (num1 + num2) / 2


result = calculate_average(10, 20)
print(result)  # 15.0


def greet_user(name, age):
    return ('Hallo ' + name + '! Du bist ' + str(age) + ' Jahre alt.')
    #greet_user = f"Hallo {name}! Du bist {age} Jahre alt."

result = greet_user("Anna", 25)
print(result)

def format_phone_number(phone_str):
  #return f"({phone_str[:3]}) {phone_str[3:6]}-{phone_str[6:]}"
   return '(' + phone_str[0:3] + ') ' + phone_str[3:6] + '-' + phone_str[6:10]

formatted = format_phone_number('1234567890')
print(formatted)

def is_discount_valid(price, discount_percent, coupon_code):
    if  price < 50:
        print('Preis zuniedrig')
        return False
        

    if discount_percent < 5 or discount_percent > 30:#geht auch elif
       price('Rabatt außerhalb des Bereichs')
       return False

    if not coupon_code.startswith("SAVE"): # geht auch elif
        print('Ungültiger Coupon-Code')
        return False

    return True
print()

print(is_discount_valid(100, 20, 'SAVE123')) # True, Ausgabe:  keine 
print(is_discount_valid(30, 20, 'SAVE123')) # False, Ausgabe: 'Preis zu niedrig' 


def process_order(items, max_price, customer_type, verbose):
    if not items:
        if verbose:
            print("Warnung: Liste ist leer")
        return (0, False)

    total = 0
    for price in items:
        if verbose:
            print("Artikel:", price)
        total += price

    if verbose:
        print("Gesamtsumme:", total)

    if customer_type == "vip":
        is_approved = total <= max_price * 1.5
    else:
        is_approved = total <= max_price

    if verbose:
        if is_approved:
            print("Bestätigt!")
        else:
            print("Abgelehnt!")

    return (total, is_approved)


# Ohne Nebeneffekte
result = process_order([10, 20, 30], 50, "regular", False)
print(result)  # (60, False)

# Mit Nebeneffekten
result = process_order([10, 20, 30], 100, "vip", True)
print(result)  # (60, True)


def process_order(items, max_price, customer_type, verbose): #verbose = ausführlich
                                                             #Gibt an, ob ein Programm detaillierte Informationen ausgeben soll.
                                                             #verbose = true → viele Logmeldungen und Details.
                                                             #verbose = false → nur wichtige Meldungen.

    # Randbedingung: Leere Liste
    if not items:  #Wächter Clausel
        if verbose:
            print("Warnung: Die Bestellliste ist leer.")
        return (0, False)

    # 1. Gesamtsumme berechnen
    total = sum(items)

    # 2. VIP-Toleranz berücksichtigen (VIPs bekommen 50% mehr Budget)
    effective_max = max_price * 1.5 if customer_type == "vip" else max_price
    is_approved = total <= effective_max

    # 3. Optionaler Nebeneffekt bei verbose == True
    if verbose:
        for item in items:
            print(f"Artikel: {item}")
        print(f"Gesamtsumme: {total}")

        if is_approved:#is_approved = ist genehmigt / wurde freigegeben bool wert
            print("Bestätigt!")
        else:
            print("Abgelehnt!")

    # 4. Rückgabe als Tuple
    return (total, is_approved)
result = process_order([10, 20, 30], 50, "regular", False)
print(result)  # (60, False)

# Mit Nebeneffekten
result = process_order([10, 20, 30], 100, "vip", True)
print(result)  # (60, True)
'''Bei Fragen:
Die Funktion prüft, ob eine Bestellung im Budget liegt, und liefert Summe und Ergebnis zurück.

Ablauf

Guard Clause: Ist items leer, bricht die Funktion sofort mit (0, False) ab. Alles Weitere wird gar nicht erst erreicht.
Summe: sum(items) addiert alle Beträge.
Budget: Ein VIP bekommt per Bedingungsausdruck das 1,5-fache Limit, alle anderen das normale. Der Vergleich total <= effective_max liefert direkt einen Wahrheitswert.
Verbose: Nur wenn gewünscht, werden Artikel, Summe und Entscheidung ausgegeben. Das ändert das Ergebnis nicht — reiner Nebeneffekt.
Rückgabe: Ein Tupel aus Summe und Genehmigung.

Die beiden Aufrufe

Aufruf	Limit effektiv	Summe	Ergebnis	Ausgabe
[10,20,30], 50, regular, False	50	60	(60, False)	nur das Tupel
[10,20,30], 100, vip, True	150	60	(60, True)	Artikel, Summe, „Bestätigt!", dann Tupel




'''
