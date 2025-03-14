import tkinter as tk
from tkinter import scrolledtext, ttk, font
import threading
import queue
import analizador  # Importa el módulo analizador
from analizador import CASOS_CORRECTOS, CASOS_INCORRECTOS

# Tema de colores moderno inspirado en Visual Studio Code
COLORES = {
    "fondo": "#1E1E1E",            # Fondo principal (gris oscuro)
    "editor": "#252526",            # Fondo del editor
    "texto": "#D4D4D4",             # Texto principal
    "acento": "#0078D7",            # Color de acento (azul Microsoft)
    "acento_hover": "#1184E8",      # Color de hover para botones
    "error": "#F14C4C",             # Color para errores (rojo más vivo)
    "exito": "#6CCB7B",             # Color para éxito (verde más llamativo)
    "titulo": "#569CD6",            # Color para títulos (azul claro)
    "borde": "#3F3F3F",             # Color para bordes
    "seleccion": "#264F78",         # Color para selección de texto
    "menu": "#333333",              # Fondo de menú/barra
    "estado": "#007ACC"             # Color para barra de estado (azul VS Code)
}

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Analizador Sintáctico LL(1) - IDE Moderno")
    ventana.geometry("1200x800")
    ventana.configure(bg=COLORES["fondo"])
    
    # Configura la fuente predeterminada
    fuente_ui = ('Segoe UI', 10)
    fuente_codigo = ('Cascadia Code', 11)  # Fuente moderna para código
    if 'Cascadia Code' not in font.families():
        fuente_codigo = ('Consolas', 11)  # Alternativa si no está Cascadia Code
        
    # Crea un estilo personalizado
    estilo = ttk.Style()
    estilo.theme_use('clam')
    
    # Configura el estilo de los widgets
    estilo.configure("TFrame", background=COLORES["fondo"])
    estilo.configure("TLabel", 
                    background=COLORES["fondo"], 
                    foreground=COLORES["texto"],
                    font=fuente_ui)
    estilo.configure("TSeparator", background=COLORES["borde"])
    
    # Variables de estado
    hilos_activos = []
    resultado_cola = queue.Queue()
    
    # Crea el marco principal
    marco_principal = ttk.Frame(ventana)
    marco_principal.pack(fill=tk.BOTH, expand=True)
    
    # Barra superior (estilo menú de VS Code)
    barra_superior = tk.Frame(marco_principal, bg=COLORES["menu"], height=40)
    barra_superior.pack(fill=tk.X, pady=(0, 1))
    
    # Panel de trabajo principal (contiene código y resultados)
    panel_trabajo = ttk.PanedWindow(marco_principal, orient=tk.VERTICAL)
    panel_trabajo.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
    
    # Panel de código
    panel_codigo = ttk.Frame(panel_trabajo)
    titulo_codigo = ttk.Frame(panel_codigo)
    titulo_codigo.pack(fill=tk.X, padx=10, pady=(10, 5))
    
    ttk.Label(titulo_codigo, text="EDITOR DE CÓDIGO", font=('Segoe UI', 10, 'bold')).pack(side=tk.LEFT)
    
    # Contenedor para el editor
    contenedor_editor = tk.Frame(panel_codigo, bg=COLORES["borde"], bd=1)
    contenedor_editor.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
    
    # Editor con aspecto moderno
    entrada_codigo = scrolledtext.ScrolledText(
        contenedor_editor,
        bg=COLORES["editor"],
        fg=COLORES["texto"],
        insertbackground=COLORES["texto"],
        selectbackground=COLORES["seleccion"],
        selectforeground=COLORES["texto"],
        font=fuente_codigo,
        borderwidth=0,
        padx=15,
        pady=15,
        wrap=tk.NONE  # Desactiva el ajuste de línea para código
    )
    entrada_codigo.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
    
    # Panel de resultados
    panel_resultados = ttk.Frame(panel_trabajo)
    titulo_resultados = ttk.Frame(panel_resultados)
    titulo_resultados.pack(fill=tk.X, padx=10, pady=(10, 5))
    
    ttk.Label(titulo_resultados, text="CONSOLA DE RESULTADOS", font=('Segoe UI', 10, 'bold')).pack(side=tk.LEFT)
    
    # Contenedor para resultados
    contenedor_resultados = tk.Frame(panel_resultados, bg=COLORES["borde"], bd=1)
    contenedor_resultados.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
    
    # Visor de resultados con estilo moderno
    resultado_texto = scrolledtext.ScrolledText(
        contenedor_resultados,
        bg=COLORES["editor"],
        fg=COLORES["texto"],
        font=fuente_codigo,
        borderwidth=0,
        padx=15,
        pady=15,
        state=tk.DISABLED
    )
    resultado_texto.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
    
    # Agrega los paneles al contenedor principal
    panel_trabajo.add(panel_codigo, weight=60)
    panel_trabajo.add(panel_resultados, weight=40)
    
    # Barra de estado moderna
    barra_estado = tk.Frame(marco_principal, bg=COLORES["estado"], height=25)
    barra_estado.pack(fill=tk.X, side=tk.BOTTOM)
    
    estado_var = tk.StringVar()
    estado_var.set("Listo")
    estado_label = tk.Label(
        barra_estado,
        textvariable=estado_var,
        bg=COLORES["estado"],
        fg=COLORES["texto"],
        font=('Segoe UI', 9),
        padx=10,
        pady=3
    )
    estado_label.pack(side=tk.LEFT)
    
    # Función para insertar texto en resultados con formato
    def insertar_resultado(texto, tipo="normal"):
        resultado_texto.config(state=tk.NORMAL)
        
        # Define etiquetas para formato
        if not hasattr(insertar_resultado, "tags_defined"):
            resultado_texto.tag_configure("normal", foreground=COLORES["texto"])
            resultado_texto.tag_configure("error", foreground=COLORES["error"], font=(fuente_codigo[0], fuente_codigo[1], 'bold'))
            resultado_texto.tag_configure("exito", foreground=COLORES["exito"], font=(fuente_codigo[0], fuente_codigo[1], 'bold'))
            resultado_texto.tag_configure("titulo", foreground=COLORES["titulo"], font=(fuente_codigo[0], fuente_codigo[1], 'bold'))
            insertar_resultado.tags_defined = True
        
        resultado_texto.insert(tk.END, texto, tipo)
        resultado_texto.see(tk.END)
        resultado_texto.config(state=tk.DISABLED)
    
    # Función para limpiar editor y resultados
    def limpiar_todo():
        entrada_codigo.delete("1.0", tk.END)
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.config(state=tk.DISABLED)
        estado_var.set("Listo")
    
    # Verificar resultados periódicamente
    def verificar_resultados():
        nonlocal hilos_activos
        hilos_activos = [h for h in hilos_activos if h.is_alive()]
        
        if hilos_activos:
            estado_var.set(f"Analizando... ({len(hilos_activos)} procesos activos)")
        else:
            estado_var.set("Listo")
        
        try:
            while True:
                caso_num, caso, resultado = resultado_cola.get_nowait()
                insertar_resultado(f"▶ Caso {caso_num}:\n", "titulo")
                insertar_resultado(f"{caso}\n", "normal")
                
                # Destaca los resultados
                if "Error" in resultado or "error" in resultado:
                    insertar_resultado(f"❌ Resultado: {resultado}\n\n", "error")
                else:
                    insertar_resultado(f"✓ Resultado: {resultado}\n\n", "exito")
        except queue.Empty:
            pass
        
        ventana.after(100, verificar_resultados)
    
    # Función para analizar el código
    def on_analizar():
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.config(state=tk.DISABLED)
        
        entrada = entrada_codigo.get("1.0", tk.END).strip()
        if not entrada:
            insertar_resultado("❌ Por favor, ingrese código para analizar.\n", "error")
            return
        
        # Deshabilita los botones durante el análisis
        for btn in botones.values():
            btn.config(state=tk.DISABLED)
        
        casos = [caso.strip() for caso in entrada.split("\n\n") if caso.strip()]
        
        if not casos:
            insertar_resultado("❌ No se encontraron casos válidos para analizar.\n", "error")
            for btn in botones.values():
                btn.config(state=tk.NORMAL)
            return
        
        # Analiza los casos en un hilo separado
        def analizar_en_hilo(casos):
            try:
                for i, caso in enumerate(casos, 1):
                    try:
                        resultado = analizador.analizar_entrada(caso)
                        resultado_cola.put((i, caso, resultado))
                    except Exception as e:
                        resultado_cola.put((i, caso, f"Error: {str(e)}"))
            finally:
                # Habilita los botones al finalizar
                ventana.after(0, lambda: [btn.config(state=tk.NORMAL) for btn in botones.values()])
        
        hilo = threading.Thread(target=analizar_en_hilo, args=(casos,))
        hilo.daemon = True
        hilos_activos.append(hilo)
        hilo.start()
    
    # Carga casos de prueba
    def cargar_casos_correctos():
        entrada_codigo.delete("1.0", tk.END)
        entrada_codigo.insert(tk.END, "\n\n".join(CASOS_CORRECTOS))
        estado_var.set("Casos correctos cargados")
    
    def cargar_casos_incorrectos():
        entrada_codigo.delete("1.0", tk.END)
        entrada_codigo.insert(tk.END, "\n\n".join(CASOS_INCORRECTOS))
        estado_var.set("Casos incorrectos cargados")
    
    # Crea botones modernos
    def crear_boton(parent, icono, texto, comando, tooltip=""):
        frame = tk.Frame(parent, bg=COLORES["menu"])
        frame.pack(side=tk.LEFT, padx=5)
        
        btn = tk.Button(
            frame,
            text=f"{icono} {texto}",
            command=comando,
            bg=COLORES["acento"],
            fg="white",
            activebackground=COLORES["acento_hover"],
            activeforeground="white",
            relief=tk.FLAT,
            bd=0,
            padx=12,
            pady=6,
            font=('Segoe UI', 9, 'bold'),
            cursor="hand2"  # Cambia el cursor a mano
        )
        btn.pack()
        
        # Efectos hover
        def on_enter(e):
            if btn['state'] != tk.DISABLED:
                btn['background'] = COLORES["acento_hover"]
                
        def on_leave(e):
            if btn['state'] != tk.DISABLED:
                btn['background'] = COLORES["acento"]
                
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        return btn
    
    # Crea los botones en la barra superior
    botones = {}
    botones["analizar"] = crear_boton(barra_superior, "▶", "Analizar", on_analizar, "Ejecutar análisis (Ctrl+Enter)")
    botones["correctos"] = crear_boton(barra_superior, "✓", "Casos Correctos", cargar_casos_correctos)
    botones["incorrectos"] = crear_boton(barra_superior, "✗", "Casos Incorrectos", cargar_casos_incorrectos)
    botones["limpiar"] = crear_boton(barra_superior, "🗑", "Limpiar", limpiar_todo, "Limpiar editor y resultados")
    
    # Inicia la verificación de resultados
    verificar_resultados()
    
    # Atajos de teclado
    ventana.bind('<Control-Return>', lambda e: on_analizar())
    ventana.bind('<Control-l>', lambda e: limpiar_todo())
    
    # Función para cerrar la ventana
    def on_closing():
        ventana.destroy()
    
    ventana.protocol("WM_DELETE_WINDOW", on_closing)
    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana()