from pydantic import BaseModel

class Estudiante(BaseModel):
    EstadoCivil: int
    ModoAplic: int
    OrdenAplic: int
    Curso: int
    AsistDiaNoche: int
    TitulPrevia: int
    Desplazado: int
    NecesidadesEducativasEspeciales: int
    Deudor: int
    MatriculasAlDia: int
    Genero: int
    Becario: int
    EdadInscripcion: int
    UC1erSemestreMatriculadas: int
    UC1erSemestreEvaluaciones: int
    UC1erSemestreAprobadas: int
    UC1erSemestreCalificacion: int
    UC1erSemestreSinEvaluaciones: int
    UC2doSemestreMatriculadas: int
    UC2doSemestreEvaluaciones: int
    UC2doSemestreAprobadas: int
    UC2doSemestreCalificacion: int
    UC2doSemestreSinEvaluaciones: int

class Prediccion(BaseModel):
    prediction: str