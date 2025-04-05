import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        a = float(a_entry.get().replace(',', '').replace('，', ''))
        b = float(b_entry.get().replace(',', '').replace('，', ''))
        c = float(c_entry.get().replace(',', '').replace('，', ''))
        
        result1 = round(a / b / c, 2)
        comparison = "<" if result1 < 22000 else ">="
        
        result2 = 200 * b * c if result1 < 22000 else 500 * b * c
        
        result3 = a - result2
        
        result4 = round((a - result2) / b / c, 2)
        
        result1_entry.delete(0, tk.END)
        result1_entry.insert(0, f"{result1} ({comparison} 22000)")
        
        result2_entry.delete(0, tk.END)
        result2_entry.insert(0, str(result2))
        
        result3_entry.delete(0, tk.END)
        result3_entry.insert(0, str(result3))
        
        result4_entry.delete(0, tk.END)
        result4_entry.insert(0, str(result4))
        
        process_label.config(text=(
            f"（计算过程: {a} ÷ {b} ÷ {c} = {result1}）\n"
            f"（计算过程: {'200 × ' if result1 < 22000 else '500 × '}{b} × {c} = {result2}）\n"
            f"（计算过程: {a} - {result2} = {result3}）\n"
            f"（计算过程: ({a} - {result2}) ÷ {b} ÷ {c} = {result4}）"
        ))
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字！")

root = tk.Tk()
root.title("金額計算")
root.geometry("600x450")

tk.Label(root, text="A: 口座入金").pack()
a_entry = tk.Entry(root)
a_entry.pack()

tk.Label(root, text="B: 泊数").pack()
b_entry = tk.Entry(root)
b_entry.pack()

tk.Label(root, text="C: 人数").pack()
c_entry = tk.Entry(root)
c_entry.pack()

tk.Button(root, text="计算", command=calculate).pack()

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="两万二:", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky='w')
result1_entry = tk.Entry(frame, font=("Arial", 12, "bold"), width=20)
result1_entry.grid(row=0, column=1)

tk.Label(frame, text="宿泊税:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky='w')
result2_entry = tk.Entry(frame, font=("Arial", 12, "bold"), width=20)
result2_entry.grid(row=1, column=1)

tk.Label(frame, text="売り上げ:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky='w')
result3_entry = tk.Entry(frame, font=("Arial", 12, "bold"), width=20)
result3_entry.grid(row=2, column=1)

tk.Label(frame, text="単価:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky='w')
result4_entry = tk.Entry(frame, font=("Arial", 12, "bold"), width=20)
result4_entry.grid(row=3, column=1)

process_label = tk.Label(root, text="（计算过程: ）", fg="darkblue", justify="left")
process_label.pack()

root.mainloop()
