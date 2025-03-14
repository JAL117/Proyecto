import tkinter as tk
from tkinter import scrolledtext, ttk, font
import threading
import queue
import analizador  
from analizador import CASOS_CORRECTOS, CASOS_INCORRECTOS

# Tema de colores moderno inspirado en Visual Studio Code
COLORES = {
    "fondo": "#1E1E1E",            
    "editor": "#252526",           
    "texto": "#D4D4D4",             
    "acento": "#0078D7",            
    "acento_hover": "#1184E8",    
    "error": "#F14C4C",             
    "exito": "#6CCB7B",             
    "titulo": "#569CD6",           
    "borde": "#3F3F3F",             
    "seleccion": "#264F78",         
    "menu": "#333333",              
    "estado": "#007ACC"             
}

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Analizador Sintáctico LL(1) - IDE Moderno")
    ventana.geometry("1200x800")
    ventana.configure(bg=COLORES["fondo"])
    

    fuente_ui = ('Segoe UI', 10)
    fuente_codigo = ('Cascadia Code', 11)  
    if 'Cascadia Code' not in font.families():
        fuente_codigo = ('Consolas', 11)  
  

    estilo = ttk.Style()
    estilo.theme_use('clam')
    
    
    estilo.configure("TFrame", background=COLORES["fondo"])
    estilo.configure("TLabel", 
                    background=COLORES["fondo"], 
                    foreground=COLORES["texto"],
                    font=fuente_ui)
    estilo.configure("TSeparator", background=COLORES["borde"])
    
    
    hilos_activos = []
    resultado_cola = queue.Queue()
    
    
    marco_principal = ttk.Frame(ventana)
    marco_principal.pack(fill=tk.BOTH, expand=True)
    
    
    barra_superior = tk.Frame(marco_principal, bg=COLORES["menu"], height=40)
    barra_superior.pack(fill=tk.X, pady=(0, 1))
    
    
    panel_trabajo = ttk.PanedWindow(marco_principal, orient=tk.VERTICAL)
    panel_trabajo.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
    
    
    panel_codigo = ttk.Frame(panel_trabajo)
    titulo_codigo = ttk.Frame(panel_codigo)
    titulo_codigo.pack(fill=tk.X, padx=10, pady=(10, 5))
    
    ttk.Label(titulo_codigo, text="EDITOR DE CÓDIGO", font=('Segoe UI', 10, 'bold')).pack(side=tk.LEFT)
    

    contenedor_editor = tk.Frame(panel_codigo, bg=COLORES["borde"], bd=1)
    contenedor_editor.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
    
    
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
        wrap=tk.NONE  
    )
    entrada_codigo.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
    

    panel_resultados = ttk.Frame(panel_trabajo)
    titulo_resultados = ttk.Frame(panel_resultados)
    titulo_resultados.pack(fill=tk.X, padx=10, pady=(10, 5))
    
    ttk.Label(titulo_resultados, text="CONSOLA DE RESULTADOS", font=('Segoe UI', 10, 'bold')).pack(side=tk.LEFT)
    
    
    contenedor_resultados = tk.Frame(panel_resultados, bg=COLORES["borde"], bd=1)
    contenedor_resultados.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
    
 
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
    
    
    panel_trabajo.add(panel_codigo, weight=60)
    panel_trabajo.add(panel_resultados, weight=40)
    
    
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
    
    
    def insertar_resultado(texto, tipo="normal"):
        resultado_texto.config(state=tk.NORMAL)
        
        
        if not hasattr(insertar_resultado, "tags_defined"):
            resultado_texto.tag_configure("normal", foreground=COLORES["texto"])
            resultado_texto.tag_configure("error", foreground=COLORES["error"], font=(fuente_codigo[0], fuente_codigo[1], 'bold'))
            resultado_texto.tag_configure("exito", foreground=COLORES["exito"], font=(fuente_codigo[0], fuente_codigo[1], 'bold'))
            resultado_texto.tag_configure("titulo", foreground=COLORES["titulo"], font=(fuente_codigo[0], fuente_codigo[1], 'bold'))
            insertar_resultado.tags_defined = True
        
        resultado_texto.insert(tk.END, texto, tipo)
        resultado_texto.see(tk.END)
        resultado_texto.config(state=tk.DISABLED)
    
    
    def limpiar_todo():
        entrada_codigo.delete("1.0", tk.END)
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.config(state=tk.DISABLED)
        estado_var.set("Listo")
    
    
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
                
              
                if "Error" in resultado or "error" in resultado:
                    insertar_resultado(f"❌ Resultado: {resultado}\n\n", "error")
                else:
                    insertar_resultado(f"✓ Resultado: {resultado}\n\n", "exito")
        except queue.Empty:
            pass
        
        ventana.after(100, verificar_resultados)
    

    def on_analizar():
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.config(state=tk.DISABLED)
        
        entrada = entrada_codigo.get("1.0", tk.END).strip()
        if not entrada:
            insertar_resultado("❌ Por favor, ingrese código para analizar.\n", "error")
            return
        
        for btn in botones.values():
            btn.config(state=tk.DISABLED)
        
        casos = [caso.strip() for caso in entrada.split("\n\n") if caso.strip()]
        
        if not casos:
            insertar_resultado("❌ No se encontraron casos válidos para analizar.\n", "error")
            for btn in botones.values():
                btn.config(state=tk.NORMAL)
            return
        
   
        def analizar_en_hilo(casos):
            try:
                for i, caso in enumerate(casos, 1):
                    try:
                        resultado = analizador.analizar_entrada(caso)
                        resultado_cola.put((i, caso, resultado))
                    except Exception as e:
                        resultado_cola.put((i, caso, f"Error: {str(e)}"))
            finally:
              
                ventana.after(0, lambda: [btn.config(state=tk.NORMAL) for btn in botones.values()])
        
        hilo = threading.Thread(target=analizar_en_hilo, args=(casos,))
        hilo.daemon = True
        hilos_activos.append(hilo)
        hilo.start()
    

    def cargar_casos_correctos():
        entrada_codigo.delete("1.0", tk.END)
        entrada_codigo.insert(tk.END, "\n\n".join(CASOS_CORRECTOS))
        estado_var.set("Casos correctos cargados")
    
    def cargar_casos_incorrectos():
        entrada_codigo.delete("1.0", tk.END)
        entrada_codigo.insert(tk.END, "\n\n".join(CASOS_INCORRECTOS))
        estado_var.set("Casos incorrectos cargados")
    
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
            cursor="hand2"  
        )
        btn.pack()
        
  
        def on_enter(e):
            if btn['state'] != tk.DISABLED:
                btn['background'] = COLORES["acento_hover"]
                
        def on_leave(e):
            if btn['state'] != tk.DISABLED:
                btn['background'] = COLORES["acento"]
                
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        return btn
    
    
    botones = {}
    botones["analizar"] = crear_boton(barra_superior, "▶", "Analizar", on_analizar, "Ejecutar análisis (Ctrl+Enter)")
    botones["correctos"] = crear_boton(barra_superior, "✓", "Casos Correctos", cargar_casos_correctos)
    botones["incorrectos"] = crear_boton(barra_superior, "✗", "Casos Incorrectos", cargar_casos_incorrectos)
    botones["limpiar"] = crear_boton(barra_superior, "🗑", "Limpiar", limpiar_todo, "Limpiar editor y resultados")
    
    # Inicia la verificación de resultados
    verificar_resultados()
    

    ventana.bind('<Control-Return>', lambda e: on_analizar())
    ventana.bind('<Control-l>', lambda e: limpiar_todo())
    
  
    def on_closing():
        ventana.destroy()
    
    ventana.protocol("WM_DELETE_WINDOW", on_closing)
    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana()