import tkinter as tk
from tkinter import ttk

# 変換ロジック
def convert():
    try:
        val = float(entry_input.get())
        mode = combo_mode.get()
        
        if mode == "メートル ➔ フィート":
            result = val * 3.28084
            label_result.config(text=f"{result:.2f} ft")
        elif mode == "フィート ➔ メートル":
            result = val / 3.28084
            label_result.config(text=f"{result:.2f} m")
        elif mode == "キログラム ➔ ポンド":
            result = val * 2.20462
            label_result.config(text=f"{result:.2f} lb")
        elif mode == "ポンド ➔ キログラム":
            result = val / 2.20462
            label_result.config(text=f"{result:.2f} kg")
    except ValueError:
        label_result.config(text="数値を入力してください")

# メインウィンドウの設定
root = tk.Tk()
root.title("簡易 単位変換 アプリ")
root.geometry("350x250")
root.resizable(False, False)

# レイアウト用の枠
frame = ttk.Frame(root, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

# 変換モード選択
label_mode = ttk.Label(frame, text="変換モード:")
label_mode.grid(row=0, column=0, sticky=tk.W, pady=5)

combo_mode = ttk.Combobox(frame, values=[
    "メートル ➔ フィート", 
    "フィート ➔ メートル", 
    "キログラム ➔ ポンド", 
    "ポンド ➔ キログラム"
], state="readonly")
combo_mode.current(0)
combo_mode.grid(row=0, column=1, label_mode, pady=5, sticky=tk.EW)

# 数値入力
label_input = ttk.Label(frame, text="数値を入力:")
label_input.grid(row=1, column=0, sticky=tk.W, pady=5)

entry_input = ttk.Entry(frame)
entry_input.grid(row=1, column=1, pady=5, sticky=tk.EW)

# 変換ボタン
btn_convert = ttk.Button(frame, text="変換する", command=convert)
btn_convert.grid(row=2, column=0, columnspan=2, pady=15)

# 結果表示
label_res_title = ttk.Label(frame, text="【結果】", font=("Helvetica", 10, "bold"))
label_res_title.grid(row=3, column=0, sticky=tk.W, pady=5)

label_result = ttk.Label(frame, text="--", font=("Helvetica", 12, "bold"), foreground="blue")
label_result.grid(row=3, column=1, sticky=tk.W, pady=5)

# 横幅の自動調整設定
frame.columnconfigure(1, weight=1)

root.mainloop()
