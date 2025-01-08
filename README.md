### **1. Clona el proyecto.***

### **2. Crear un entorno virtual**

#### En Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### En Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Instalar dependencias**
Con el entorno virtual activado, instala las dependencias:
```bash
pip install -r requirements.txt
```

---

## **Ejecución del proyecto**

### **Comando para iniciar el servidor**
Ejecuta el servidor con el siguiente comando:
```bash
fastapi dev project/app/main.py
```

Por defecto, la aplicación estará disponible en:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

### **Documentación interactiva**
FastAPI incluye una interfaz de documentación interactiva accesible en:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
