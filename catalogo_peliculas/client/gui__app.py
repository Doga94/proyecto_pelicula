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
        self.desabilitar_campos()

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

        #Entrys
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width=50, font=('Arial', 11))
        self.entry_nombre.grid(row = 0, column= 1, padx=10, pady=10, columnspan= 2)

        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.config(width=50, font=('Arial', 11))
        self.entry_duracion.grid(row = 1, column= 1, padx=10, pady=10, columnspan= 2)

        self.entry_genero = tk.Entry(self)
        self.entry_genero.config(width=50, font=('Arial', 11))
        self.entry_genero.grid(row = 2, column= 1, padx=10, pady=10, columnspan= 2)

        #Botones
        self.boton_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 11, 'bold'),
                                                fg= '#FFFFFF', bg= '#1387F8', cursor= "hand2", activebackground='#0053FC')
        self.boton_nuevo.grid(row= 4, column= 0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar")
        self.boton_guardar.config(width=20, font=('Arial', 11, 'bold'),
                                                fg= '#FFFFFF', bg= '#01C1BC', cursor= "hand2", activebackground='#67DEA1')
        self.boton_guardar.grid(row= 4, column= 1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text="Cancelar", command=self.desabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 11, 'bold'),
                                                fg= '#FFFFFF', bg= '#AB2967', cursor= "hand2", activebackground='#EE7055')
        self.boton_cancelar.grid(row= 4, column= 2, padx=10, pady=10)

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def desabilitar_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')