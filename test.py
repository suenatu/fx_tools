# クロス円 - pips
YEN = 0.01      # 1銭

# 米ドルストレート- pips
DOLLAR = 0.0001     # 0.01セント


pips_trans_dic = {"YEN":0.01, "DOLLAR":0.0001, "PONDO":0.00001}


# 単位
def unit_selection(pair) :
    # 通貨ペアの場合
    if len(pair) == 6 :
        # 通貨
        unit = pair[3:]
        # 1pips
        pip_unit = pips_trans_dic[unit]

    return pip_unit

# pips計算 - 範囲が何pipsか
def pips_calc(pip_unit, up_rate, bottom_rate):
    # 範囲
    if up_rate >bottom_rate :
        rate_range = up_rate - bottom_rate
    else :
        rate_range = bottom_rate - up_rate
    # pips計算
    calc = rate_range / pip_unit

    return calc

# リスクリワード - 1:2がどこか
def risk_rewards(pip_unit, rate, profit_rate) :
    # ショートの場合
    if rate > profit_rate :
        rate_range = rate - profit_rate
    # ロングの場合
    else :
        rate_range = profit_rate - rate
    risk = rate_range / 2
    # ショートの場合
    if rate > profit_rate :
        rate += risk
    # ロングの場合
    else :
        rate -= risk

    return rate