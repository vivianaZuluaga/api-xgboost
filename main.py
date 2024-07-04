from fastapi import FastAPI, HTTPException
from modelo.modelo import __version__ as version, modelo, categorias
from modelo.estudiante import Estudiante, Prediccion
import numpy as np
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
origins = ['*'] 
app = FastAPI(middleware=[
    Middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])
])

@app.get('/')
def index():
    try:
        return {
            'message': 'Sistema de Alerta Temprana Para Prevenir El Abandono Escolar ML API', 
            'version': version
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/predict', response_model=Prediccion)
def predict(data: Estudiante):
    try:
        data = data.dict()
        EstadoCivil = data["EstadoCivil"]
        ModoAplic = data["ModoAplic"]
        OrdenAplic = data["OrdenAplic"]
        Curso = data["Curso"]
        AsistDiaNoche = data["AsistDiaNoche"]
        TitulPrevia = data["TitulPrevia"]
        Desplazado = data["Desplazado"]
        NecesidadesEducativasEspeciales = data["NecesidadesEducativasEspeciales"]
        Deudor = data["Deudor"]
        MatriculasAlDia = data["MatriculasAlDia"]
        Genero = data["Genero"]
        Becario = data["Becario"]
        EdadInscripcion = data["EdadInscripcion"]
        UC1erSemestreMatriculadas = data["UC1erSemestreMatriculadas"]
        UC1erSemestreEvaluaciones = data["UC1erSemestreEvaluaciones"]
        UC1erSemestreAprobadas = data["UC1erSemestreAprobadas"]
        UC1erSemestreCalificacion = data["UC1erSemestreCalificacion"]
        UC1erSemestreSinEvaluaciones = data["UC1erSemestreSinEvaluaciones"]
        UC2doSemestreMatriculadas = data["UC2doSemestreMatriculadas"]
        UC2doSemestreEvaluaciones = data["UC2doSemestreEvaluaciones"]
        UC2doSemestreAprobadas = data["UC2doSemestreAprobadas"]
        UC2doSemestreCalificacion = data["UC2doSemestreCalificacion"]
        UC2doSemestreSinEvaluaciones = data["UC2doSemestreSinEvaluaciones"]
        estudiante = np.asarray([[EstadoCivil,ModoAplic,OrdenAplic,Curso,AsistDiaNoche,TitulPrevia,Desplazado,NecesidadesEducativasEspeciales,Deudor,MatriculasAlDia,Genero,Becario,EdadInscripcion,UC1erSemestreMatriculadas,UC1erSemestreEvaluaciones,UC1erSemestreAprobadas,UC1erSemestreCalificacion,UC1erSemestreSinEvaluaciones,UC2doSemestreMatriculadas,UC2doSemestreEvaluaciones,UC2doSemestreAprobadas,UC2doSemestreCalificacion,UC2doSemestreSinEvaluaciones]])
        prediction = modelo.predict(estudiante)
        categoria = categorias[prediction[0]]
        return {
            'prediction': categoria
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))