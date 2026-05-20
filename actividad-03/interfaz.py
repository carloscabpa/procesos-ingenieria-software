import tkinter as tk
from calculadora import Calculadora

calc = Calculadora()

def calcular(operacion):
    try:
        a = float(entrada_a.get())
        b = float(entrada_b.get())

        if operacion == "sumar":
            resultado = calc.sumar(a, b)
        elif operacion == "restar":
            resultado = calc.restar(a, b)
        elif operacion == "multiplicar":
            resultado = calc.multiplicar(a, b)
        elif operacion == "dividir":
            resultado = calc.dividir(a, b)

        etiqueta_resultado.config(text=f"Resultado: {resultado}")

    except ValueError as error:
        etiqueta_resultado.config(text=f"Error: {error}")


ventana = tk.Tk()
ventana.title("Calculadora")

entrada_a = tk.Entry(ventana)
entrada_a.pack()

entrada_b = tk.Entry(ventana)
entrada_b.pack()

tk.Button(ventana, text="Sumar", command=lambda: calcular("sumar")).pack()
tk.Button(ventana, text="Restar", command=lambda: calcular("restar")).pack()
tk.Button(ventana, text="Multiplicar", command=lambda: calcular("multiplicar")).pack()
tk.Button(ventana, text="Dividir", command=lambda: calcular("dividir")).pack()

etiqueta_resultado = tk.Label(ventana, text="Resultado:")
etiqueta_resultado.pack()

ventana.mainloop()