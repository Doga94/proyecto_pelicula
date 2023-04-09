import tkinter as tk

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 250, height = 200)

    menu_inicio = tk.Menu(barra_menu, tearoff= 0)
    menu_consulta = tk.Menu(barra_menu, tearoff= 0)
    menu_configuracion = tk.Menu(barra_menu, tearoff= 0)
    menu_ayuda =tk.Menu(barra_menu, tearoff= 0)

    barra_menu.add_cascade(label = 'Inicio', menu= menu_inicio)
    menu_inicio.add_command(label= 'Crear registro en BD')
    menu_inicio.add_command(label= 'Eliminar registro BD')
    menu_inicio.add_command(label= 'Salir', command= root.destroy)

    barra_menu.add_cascade(label = 'Consultas', menu= menu_consulta)
    menu_consulta.add_command(label= 'Ver datos')
    menu_consulta.add_command(label= 'Ver registros')

    barra_menu.add_cascade(label= 'Configuración', menu = menu_configuracion)
    menu_configuracion.add_command(label= 'General')
    menu_configuracion.add_command(label= 'Avanzado')

    barra_menu.add_cascade(label='Ayuda', menu = menu_ayuda)
    menu_ayuda.add_command(label='Soporte')
    menu_ayuda.add_command(label='Donación')


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=400)
        self.root = root
        self.pack()
        #self.config( bg= 'blue')

        self.campos_pelicula()

    def campos_pelicula(self):
        #label de cada campo
        self.label_nombre = tk.Label(self, text = 'Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row = 0, column= 0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text = 'Duración: ')
        self.label_duracion.config(font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row = 1, column= 0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text = 'Genero: ')
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row = 2, column= 0, padx=10, pady=10)