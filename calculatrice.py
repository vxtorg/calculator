from tkinter import *
from tkinter import ttk

root = Tk()

# Crear un marco 
frame = ttk.Frame(root, padding=10, width=400, height=300)
frame.grid()

Recibidor = Text(frame, height=3, width=30)
Recibidor.grid(row=0, column=0, columnspan=4, pady=10)

# Función para manejar la operación al presionar un botón de número o operador
def Operacion(caracter):
    Recibidor.insert(END, caracter)
    print("El signo " + caracter + " fue presionado")

# Función para resolver la operación cuando se presiona el botón "="
def resuelve():
    ecuacion = Recibidor.get("1.0", END).strip()  # Obtener la expresión de la caja de texto
    try:
        resultado = eval(ecuacion)  # Evaluar la expresión para obtener el resultado
        Recibidor.delete("1.0", END)  # Limpiar la caja de texto
        Recibidor.insert(END, resultado)  # Mostrar el resultado en la caja de texto
        print("Resultado:", resultado)
    except Exception as e:
        Recibidor.delete("1.0", END)  # Limpiar la caja de texto
        Recibidor.insert(END, "Error")  # Mostrar "Error" en la caja de texto si hay un error
        print("Error:", e)

# Botones de los números
for i in range(1, 10):
    boton = ttk.Button(frame, text=str(i), command=lambda i=i: Operacion(str(i)))
    boton.grid(row=(i-1) // 3 + 1, column=(i-1) % 3, pady=10)

# Botones de los operadores
operadores = ["+", "-", "*", "/"]
for i, op in enumerate(operadores):
    boton = ttk.Button(frame, text=op, command=lambda op=op: Operacion(op))
    boton.grid(row=i+1, column=4, pady=10)

# Botón "=" para resolver la operación
boton_igual = ttk.Button(frame, text="=", command=resuelve)
boton_igual.grid(row=4, column=4, pady=10)

# Para que no se cierre la ventana
root.mainloop()
