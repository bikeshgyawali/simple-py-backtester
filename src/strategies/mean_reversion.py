from src.utils.friction import buy_friction, sell_friction

def mean_reversion(eod_close_price, portfolio, shares, history=None):
    if history is None:
        history = []
    
    history.append(eod_close_price)
    
    if len(history) < 20:
        return portfolio, shares, history
        
    recent_history = history[-20:]
    
    ma_20 = sum(recent_history) / 20
    
    variance = sum((x - ma_20) ** 2 for x in recent_history) / 20
    std_dev = variance ** 0.5
    
    upper_band = ma_20 + (2 * std_dev)
    lower_band = ma_20 - (2 * std_dev)

    if eod_close_price < lower_band:
        total_cost = buy_friction(eod_close_price)
        if portfolio >= total_cost:
            shares += 1
            portfolio -= total_cost

    elif eod_close_price > upper_band and shares > 0:
        shares -= 1
        portfolio += sell_friction(eod_close_price)

    return portfolio, shares, history