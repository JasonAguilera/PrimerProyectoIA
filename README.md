# PrimerProyectoIA
# 🚀 Proyecto IA en la Nube

## Descripción

Este proyecto consiste en el desarrollo de una API en Python que implementa un modelo básico de inteligencia artificial para realizar predicciones en base a datos de entrada.

La aplicación permite enviar un valor (horas) y devuelve un resultado calculado mediante un modelo de regresión lineal. Además, cada predicción se almacena en una base de datos en la nube.

---

##  Tecnologías utilizadas

* **Visual Studio Code** → Desarrollo del proyecto
* **GitHub** → Control de versiones
* **Python** → Lenguaje principal
* **Flask** → Framework para la API
* **Scikit-learn** → Modelo de inteligencia artificial
* **Supabase** → Base de datos en la nube
* **Render** → Despliegue en la nube
* **Docker** → Contenerización

---

## 📁 Estructura del proyecto

```
PrimerProyectoIA/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .env.example
├── README.md
└── screenshots/
```

---

##  Instalación local

```bash
git clone https://github.com/TU-USUARIO/PrimerProyectoIA.git
cd PrimerProyectoIA
pip install -r requirements.txt
python app.py
```

La API se ejecutará en:

```
http://localhost:5000
```

---

##  Uso de la API

### 🔹 Endpoint principal

```
GET /
```

Respuesta:

```json
{
  "mensaje": "API IA funcionando 🚀"
}
```

---

###  Predicción

```
POST /predict
```

Body:

```json
{
  "horas": 5
}
```

Respuesta:

```json
{
  "resultado": 80.0
}
```

---

##  Despliegue en la nube

La aplicación fue desplegada utilizando **Render**, conectado directamente con GitHub para integración continua.

🔗 URL de la aplicación:

```
https://primerproyectoia.onrender.com
```

---

##  Base de datos (Supabase)

Se utilizó **Supabase** como base de datos en la nube para almacenar las predicciones generadas por el modelo.

### Tabla utilizada:

**predicciones**

| Campo     | Tipo  |
| --------- | ----- |
| id        | int   |
| horas     | float |
| resultado | float |

---

##  Configuración de entorno

Se utilizaron variables de entorno para proteger credenciales:

```
SUPABASE_URL=tu_url
SUPABASE_KEY=tu_key
```

Estas variables se configuran en Render (Environment).

---

##  Seguridad

Para fines académicos, se desactivó temporalmente la política de seguridad **Row Level Security (RLS)** en Supabase para permitir inserciones desde la API.

---

##  Decisiones tecnológicas

* Se eligió **Python** por su fuerte integración con inteligencia artificial.
* **Flask** por su simplicidad para crear APIs rápidas.
* **Supabase** por ofrecer una base de datos en la nube fácil de usar.
* **Render** por su facilidad de despliegue automático.
* **Docker** para asegurar portabilidad del entorno.
* **GitHub** para control de versiones e integración continua.

---

## Evidencia

Las capturas del funcionamiento del sistema se encuentran en la carpeta:

```
/screenshots
```

Incluyen:

* API funcionando localmente
* Despliegue en Render
* Pruebas del endpoint
* Datos almacenados en Supabase

---

##  Conclusión

Este proyecto demuestra la integración completa de herramientas modernas para el desarrollo de soluciones de datos e inteligencia artificial en la nube, incluyendo desarrollo, despliegue, persistencia de datos y consumo mediante API.

---

##  Autor

Jason Aguilera
