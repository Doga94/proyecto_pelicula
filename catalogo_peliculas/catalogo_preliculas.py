# Importar el módulo tkinter con el alias tk
import tkinter as tk
from client.gui__app import Frame, barra_menu

# Definir la función principal del programa
def main():
    # Crear una instancia de la clase Tk del módulo tkinter y asignarla a la variable root
    root = tk.Tk()
    root.title('Catalogo peliculas') #Cambiar titulo del programa
    root.iconbitmap('img/palomitas-de-maiz.png') #cambiar icono del programa
    root.resizable(1,0) #permite modificaciones de la ventana
    # Ejecutar el ciclo principal del gestor de eventos de la ventana
    barra_menu(root)

    app = Frame(root=root)

    root.mainloop()

# Comprobar si el script se está ejecutando como el archivo principal
if __name__ == '__main__':
    # Llamar a la función principal
    main()
