'''Calculadora GUI usando Tkinter'''

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Calculadora")
    root.geometry("300x400")

    expressao = ""

    def atualizar_display(valor):
        nonlocal expressao
        expressao += str(valor)
        display_var.set(expressao)

    def calcular():
        nonlocal expressao
        try:
            resultado = str(eval(expressao))
            display_var.set(resultado)
            expressao = resultado
        except Exception:
            display_var.set("Erro")
            expressao = ""

    def limpar():
        nonlocal expressao
        expressao = ""
        display_var.set("")

    display_var = tk.StringVar()
    display = tk.Entry(root, textvariable=display_var, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify='right')
    display.pack(fill='both', padx=10, pady=10, ipady=10)

    botoes = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['0', '.', 'C', '+'],
    ]

    for linha in botoes:
        frame = tk.Frame(root)
        frame.pack(expand=True, fill='both')
        for b in linha:
            if b == 'C':
                btn = tk.Button(frame, text=b, font=("Arial", 18), command=limpar)
            else:
                btn = tk.Button(frame, text=b, font=("Arial", 18), command=lambda x=b: atualizar_display(x))
            btn.pack(side='left', expand=True, fill='both', padx=2, pady=2)

    igual_btn = tk.Button(root, text='=', font=("Arial", 18), bg='#4CAF50', fg='white', command=calcular)
    igual_btn.pack(expand=True, fill='both', padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()