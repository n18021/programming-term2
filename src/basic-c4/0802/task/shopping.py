import calc_tax
def exec():
    """
    Parameters
    ----------
    無し

Returns
    ----------
    list
    表示されるメッセージを要素に含むリスト
    """

    unit_dc = {
        "Banana": 100,
        "Apple": 200,
        "Orange": 150
    }

    nums_dc = {
        "Banana": 2,
        "Apple": 1,
        "Orange": 3,
    }

    money = 2000
    res_list = []
    money_list = []
    for name, price in unit_dc.items():
        kosuu = nums_dc[name]
        okane = price * kosuu
        money_list.append(okane)
        s = "{}を{}個買いました。　商品合計は{}円です".format(name, kosuu, okane)
    res_list.append(s)
    total = sum(money_list)
    tax_v = round(calc_tax.calc_incl_tax(total))
    hh = "税抜き総額{}円、消費税込み{}円です。".format(total,tax_v)
    res_list.append(hh)
    pp = "残金{}円です。".format(money - tax_v)
    res_list.append(pp)

    return res_list

def display(msgs):
    """
    結果を表示する

    Parameters
    ----------
    無し
    """
    print("\n".join(msgs))


if __name__ == '__main__':
        display(exec())
