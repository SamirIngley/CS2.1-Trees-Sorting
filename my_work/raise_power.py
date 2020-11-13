
def raise_to_power(base, power):
    
    if power == 1:
        return base

    return base * raise_to_power(base, power-1)


print(raise_to_power(2, 3))