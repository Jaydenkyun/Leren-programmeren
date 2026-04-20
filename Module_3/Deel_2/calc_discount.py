month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10
def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    if brand in month_discount_brands:
        return price * month_discount_brands /100
    
    