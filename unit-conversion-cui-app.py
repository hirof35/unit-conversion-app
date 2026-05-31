def meter_to_feet(meter):
    return meter * 3.28084

def feet_to_meter(feet):
    return feet / 3.28084

def kg_to_lb(kg):
    return kg * 2.20462

def lb_to_kg(lb):
    return lb / 2.20462

def main():
    print("=== 単位変換アプリ ===")
    print("1: メートル -> フィート")
    print("2: フィート -> メートル")
    print("3: キログラム -> ポンド")
    print("4: ポンド -> キログラム")
    
    choice = input("変換する番号を選んでください (1-4): ")
    
    if choice not in ['1', '2', '3', '4']:
        print("無効な選択です。")
        return

    try:
        val = float(input("変換したい数値を入力してください: "))
    except ValueError:
        print("数値を正しく入力してください。")
        return

    if choice == '1':
        print(f"結果: {val} m = {meter_to_feet(val):.2f} ft")
    elif choice == '2':
        print(f"結果: {val} ft = {feet_to_meter(val):.2f} m")
    elif choice == '3':
        print(f"結果: {val} kg = {kg_to_lb(val):.2f} lb")
    elif choice == '4':
        print(f"結果: {val} lb = {lb_to_kg(val):.2f} kg")

if __name__ == "__main__":
    main()
