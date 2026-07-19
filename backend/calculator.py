import math

# This is a dummy function! Not the real calculator.
def f(x):
    if 0 <= x < 0.112673936815082:
        return 17.751 * x + 20.000
    elif 0.112673936815082 <= x < 0.204061585370729:
        return 32.827 * x + 18.302
    elif 0.204061585370729 <= x < 0.282:
        return 64.155 * x + 11.904
    elif 0.282 <= x < 0.432:
        return 200.000 * x - 26.400
    elif 0.432 <= x < 0.682:
        return 100.000 * x + 16.800
    elif 0.682 <= x < 0.932:
        return 20.000 * x + 71.360
    elif 0.932 <= x < 1.482:
        return 36.364 * x + 56.109
    elif 1.482 <= x < 2.782:
        return 61.538 * x + 18.769
    elif 2.782 <= x < 5.432:
        return 22.642 * x + 127.019
    elif 5.432 <= x < 8.032:
        return 51.923 * x - 32.061
    elif 8.032 <= x < 13.332:
        return 17.925 * x + 240.983
    elif 13.332 <= x < 26.482:
        return 42.585 * x - 87.869
    elif 26.482 <= x < 52.782:
        return 13.308 * x + 687.589
    elif 52.782 <= x < 79.082:
        return 35.741 * x - 496.164
    elif 79.082 <= x:
        return 18.169 * x + 893.896
    else:
        return 0

def pososto(x):
    if x == 10:
        return 0.35
    elif x == 20:
        return 0.23
    elif x == 30:
        return 0.1
    elif x == 40:
        return 0.04
    else:
        return 0

def run_calculation(horiz, vert, userquant):
    # Fixed Parameters (in mm)
    edge1 = 4  
    edge2 = 70  
    inspace = 2 * edge1  
    roland = 1000  
    wfelimo = roland - 2 * edge1  

    # Math Optimization
    checkmhkos = (wfelimo + inspace) % (horiz + inspace)
    checkplatos = (wfelimo + inspace) % (vert + inspace)

    seira = math.floor(wfelimo / (vert + inspace))
    decidevert = horiz

    if checkmhkos < checkplatos:
        seira = math.floor(wfelimo / (horiz + inspace))
        decidevert = vert

    if seira == 0:
        seira = 1

    # Base price of 50 stickers for discount benchmark
    temp_sthlh = math.floor(50 / seira) or 1
    temp_epifaneia = (temp_sthlh * (decidevert + inspace) - inspace + 2 * edge2) / 1000
    nodiscprice = int(f(temp_epifaneia))

    # 1. Calculate Fixed Table
    qtuple = (10, 20, 30, 40, 50, 100, 200, 300, 500, 1000, 2000, 3000, 5000, 10000, 20000, 30000)
    fixed_results = []
    
    for i in range(4, 14):
        qty = qtuple[i]
        sthlh_f = math.floor(qty / seira) or 1
        epifaneia_f = (sthlh_f * (decidevert + inspace) - inspace + 2 * edge2) / 1000
        timh_f = int(f(epifaneia_f))
        
        ratioprice_f = nodiscprice * qty / 50
        discount_f = int((1 - timh_f / ratioprice_f) * 100) if ratioprice_f > 0 else 0
        price_per_item_f = timh_f / qty
        
        fixed_results.append({
            "quantity": qty,
            "total_price": timh_f,
            "discount": max(0, discount_f),
            "price_per_item": round(price_per_item_f, 2),
            "surface_area": round(epifaneia_f, 3)
        })

    # 2. Calculate User Quantity
    sthlh = math.floor(userquant / seira) or 1
    epifaneia = (sthlh * (decidevert + inspace) - inspace + 2 * edge2) / 1000

    if userquant <= 50:
        timh = int((nodiscprice * userquant / 50) * (1 + pososto(userquant)))
        discount = 0
    else:
        timh = int(f(epifaneia))
        ratioprice = nodiscprice * userquant / 50
        discount = int((1 - timh / ratioprice) * 100) if ratioprice > 0 else 0

    priceperitem = timh / userquant if userquant > 0 else 0

    return {
        "custom": {
            "quantity": userquant,
            "total_price": round(timh, 2),
            "discount": max(0, discount),
            "price_per_item": round(priceperitem, 2),
            "surface_area": round(epifaneia, 3)
        },
        "fixed_table": fixed_results
    }
