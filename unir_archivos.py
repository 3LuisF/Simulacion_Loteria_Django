import os

# Extensiones de archivo que quieres incluir
ARCHIVOS_VALIDOS = ('.py', '.html', '.css', '.js', '.json')
# Carpetas que quieres ignorar para no subir archivos basura
CARPETAS_IGNORADAS = ('venv', 'env', '__pycache__', '.git', 'staticfiles', 'media')

def generar_archivo_contexto(nombre_salida="proyecto_completo.txt"):
    with open(nombre_salida, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk('.'):
            # Ignorar carpetas del sistema
            dirs[:] = [d for d in dirs if d not in CARPETAS_IGNORADAS]
            
            for file in files:
                if file.endswith(ARCHIVOS_VALIDOS):
                    file_path = os.path.join(root, file)
                    outfile.write(f"\n{'='*40}\n")
                    outfile.write(f"ARCHIVO: {file_path}\n")
                    outfile.write(f"{'='*40}\n")
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            outfile.write(infile.read())
                        outfile.write("\n\n")
                    except Exception as e:
                        outfile.write(f"No se pudo leer el archivo: {e}\n\n")

if __name__ == "__main__":
    generar_archivo_contexto()
    print("¡Archivo 'proyecto_completo.txt' creado con éxito!")
