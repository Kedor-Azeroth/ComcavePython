def process_order(items, max_price, customer_type, verbose):
    # Randbedingung: Leere Liste
    if not items:
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

        if is_approved:
            print("Bestätigt!")
        else:
            print("Abgelehnt!")

    # 4. Rückgabe als Tuple
    return (total, is_approved)

# Ohne Nebeneffekte
result = process_order([10, 20, 30], 50, "regular", False)
print(result)  # (60, False)

# Mit Nebeneffekten
result = process_order([10, 20, 30], 100, "vip", True)
print(result)  # (60, True)
