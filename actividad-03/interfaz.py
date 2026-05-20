import tkinter as tk
from calculadora import Calculadora

calc = Calculadora()

def calcular(operacion):
    try:
        x = float(entrada_a.get())
        y = float(entrada_b.get())

        if operacion == "sumar":
            resultado = calc.sumar(x, y)
        elif operacion == "restar":
            resultado = calc.restar(x, y)
        elif operacion == "multiplicar":
            resultado = calc.multiplicar(x, y)
        elif operacion == "dividir":
            resultado = calc.dividir(x, y)

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