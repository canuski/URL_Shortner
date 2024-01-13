def create_supplier(delay_factor, price_factor):
    def get_offer(expected_delivery_time, price_estimate):
        estimated_delivery = int(expected_delivery_time * delay_factor)
        estimated_price = int(price_estimate * price_factor)

        offer_str = f"geschatte levertijd: {estimated_delivery} dagen\n"
        offer_str += f"geschatte kostprijs: {estimated_price} euro\n"

        return offer_str

    return get_offer

# Voorbeeldgebruik
get_offer_from_bol = create_supplier(0.8, 1.1)
get_offer_from_amazon = create_supplier(1.2, 0.9)
get_offer_from_aliexpress = create_supplier(1.5, 0.75)

# Roep de functies aan en print de resultaten
print(get_offer_from_bol(100, 100))
print(get_offer_from_amazon(100, 100))
print(get_offer_from_aliexpress(100, 100))
