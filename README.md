# api-xgboost - Sistema de Alerta Temparana (SAT) para Prevenir el Abandono Escolar

Modelo XGBoost con una precision del 91.46%

### 1. El modelo usado en el proyecto esta disponible en Colab

[Abrir Colab](https://colab.research.google.com/drive/1GaiVXQF31XE854sKaDxZR6kCCjcOl0DC?usp=sharing)

### 2. Entorno virtual (opcional)

Abra una terminal y ejecute para la creacion del entorno virtual en caso de requerirse

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Dependencias necesarias

Abra una terminal y ejecute. Si cuenta con un entorno virtual ejecutar en este:

```bash
pip install uvicorn fastapi joblib xgboost starlette streamlit
```

### 3. Iniciar el servidor backend
Abra una terminal y ejecute. Si cuenta con un entorno virtual ejecutar en este:

```bash
uvicorn main:app --reload
```

### 4. Iniciar el servidor frontend
Abra una terminal y ejecute. Si cuenta con un entorno virtual ejecutar en este:

```bash
streamlit run app.py
```
