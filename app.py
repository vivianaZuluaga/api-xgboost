import streamlit as st 
import requests 
import json
 
#Color de fondo

#Color del formulario
css = """
<style>
[data-testid="stForm"] {
    background: LightBlue;
}
</style>
"""
st.write(css, unsafe_allow_html=True)

# Título de la aplicación 
st.title('Formulario de Test estudiantil') 
 
# Campos del formulario 

#Opciones en el formulario
valores_selec1 = {1: "Soltero", 2: "Casado", 3: "Viudo", 4: "Divorciado", 5: "Union de hecho", 6: "Legalmente separado"}
opcion_selec1 = st.selectbox("Estado civil:", valores_selec1.keys(), 
format_func=lambda x:valores_selec1[ x ], 
index=None, 
placeholder="Seleccione una opcion")

valores_selec2 = {1:"Primera fase—Contingente general",
2:"Ordenanza n° 612/93",3:"1ª fase—contingente especial (Isla Azores)",4:"Titulares de otros cursos superiores",5:"Ordenanza N° 854-B/99",
6:"Estudiante internacional (licenciatura)",7:"1.ª fase—contingente especial (Isla Madeira)",8:"2.ª fase—contingente general",9:"3ra fase—contingente general",
10:"Ordenanza N° 533-A/99, inciso b2) (Plan Diferente)",11:"Ordenanza N° 533-A/99, inciso b3 (Otra Institución)",12:"Mayores de 23 años",
13:"Transferencia",14:"Cambio de rumbo",15:"Titulados de diplomas de especialización tecnológica",16:"Cambio de institución/curso",
17:"Titulados de diploma de ciclo corto",18:"Cambio de institución/curso (Internacional)"}
opcion_selec2 = st.selectbox("Modo de aplicación", valores_selec2.keys(), 
format_func=lambda x:valores_selec2[ x ], 
index=None, 
placeholder="Seleccione una opcion")

valores_selec3 = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
opcion_selec3 = st.selectbox("Orden de solicitud: ", valores_selec3.keys(), 
format_func=lambda x:valores_selec3[ x ], 
index=None, 
placeholder="Seleccione una opcion")

valores_selec4 = {1:"Tecnologías de producción de biocombustibles",
2:"Animación y diseño multimedia",3:"Servicio social (asistencia nocturna)",4:"Agronomía",
5:"Diseño de comunicación",6:"Enfermería veterinaria",7:"Ingeniería informática",
8:"Equinicultura",9:"Gestión",10:"Servicio Social",11:"Turismo",12:"Enfermería",13:"Higiene bucal",14:"Gestión de publicidad y marketing",15:"Periodismo y comunicación",
16:"Educación básica",17:"Gestión (asistencia nocturna)"}
opcion_selec4=st.selectbox("Curso: ", valores_selec4.keys(), 
format_func=lambda x:valores_selec4[ x ], 
index=None, 
placeholder="Seleccione una opcion")

valores_selecDiurno = {1:'Nocturna',0:'Diurna'}
opcion_selecDiurno= st.selectbox("Asistencia Diurna o Nocturna: ", valores_selecDiurno.keys(), 
format_func=lambda x:valores_selecDiurno[ x ], 
index=None, 
placeholder="Seleccione una opcion")

valores_selec5 = {1:"Educación secundaria",2:"Educación superior—licenciatura",3:"Educación superior—título",
4:"Educación superior—maestría",5:"Educación superior—doctorado",6:"Frecuencia de educación superior",
7:"12° año de escolaridad—no completado",8:"11° año de escolaridad—no completado",
9:"Otros—11° año de escolaridad",10:"10° año de escolarización",11:"décimo año de escolaridad—no completado",
12:"Educación básica 3er ciclo (9°/10°/11° año) o equivalente",
13:"Educación básica 2° ciclo (6°/7°/8° año) o equivalente",
14:"Curso de especialización tecnológica",
15:"Educación superior—licenciatura (1er ciclo)",
16:"Curso técnico superior profesional",
17:"Educación superior—maestría (2do ciclo)"}
opcion_selec5= st.selectbox("Titulación previa-Nivel educativo: ", valores_selec5.keys(), 
format_func=lambda x:valores_selec5[ x ], 
index=None, 
placeholder="Seleccione una opcion")

valores_selec8 = {1:'Si',0:'No'}
opcion_selec8= st.selectbox("Desplazado: ", valores_selec8.keys(), 
format_func=lambda x:valores_selec8[ x ], 
index=None, 
placeholder="Seleccione una opcion")

valores_selec9 = {1:'Si',0:'No'}
opcion_selec9= st.selectbox("Necesidades educativas especiales: ", valores_selec9.keys(), 
format_func=lambda x:valores_selec9[ x ], 
index=None, 
placeholder="Seleccione una opcion")

valores_selec10 = {1:'Si',0:'No'}
opcion_selec10= st.selectbox("Deudor: ", valores_selec10.keys(), 
format_func=lambda x:valores_selec10[ x ], 
index=None, 
placeholder="Seleccione una opcion")

valores_selec11 = {1:'Si',0:'No'}
opcion_selec11= st.selectbox("Matrículas al día: ", valores_selec11.keys(), 
format_func=lambda x:valores_selec11[ x ], 
index=None, 
placeholder="Seleccione una opcion")

valores_selec12 = {1:'Masculino',0:'Femenino'}
opcion_selec12= st.selectbox("Género: ", valores_selec12.keys(), 
format_func=lambda x:valores_selec12[ x ], 
index=None, 
placeholder="Seleccione una opcion")

valores_selec13 = {1:'Si',0:'No'}
opcion_selec13= st.selectbox("Becario: ", valores_selec13.keys(), 
format_func=lambda x:valores_selec13[ x ], 
index=None, 
placeholder="Seleccione una opcion")

user_input12 = st.text_input('Edad de inscripción:', placeholder='Edad del estudiante al momento de la inscripción')
user_input13 = st.text_input('Numero de unidades curriculares matriculadas en el 1er semestre', placeholder='Cantidad de unidades')
user_input14 = st.text_input('Numero de evaluaciones a unidades curriculares en el 1er semestre', placeholder='Ingrese la cantidad de unidades')
user_input15 = st.text_input('Numero de unidades curriculares aprobadas en el 1er semestre', placeholder='Ingrese la cantidad de unidades')
user_input16 = st.text_input('Promedio de calificaciones 1er semestre (entre 0 y 20)', placeholder='Ingrese el promedio')
user_input17 = st.text_input('Numero de unidades curriculares 1er semestre sin evaluaciones', placeholder='Ingrese la cantidad de unidades')
user_input18 = st.text_input('Numero de unidades curriculares matriculadas en el 2do semestre', placeholder='Cantidad de unidades')
user_input19 = st.text_input('Numero de evaluaciones a unidades curriculares en el 2do semestre', placeholder='Ingrese la cantidad de unidades')
user_input20 = st.text_input('Numero de unidades curriculares aprobadas en el 2do semestre', placeholder='Ingrese la cantidad de unidades')
user_input21 = st.text_input('Promedio de calificaciones en el 2do semestre (entre 0 y 20)', placeholder='Ingrese el promedio')
user_input22 = st.text_input('Numero de unidades curriculares sin evaluaciones en el 2do semestre', placeholder='Ingrese la cantidad de unidades')

submit_button = st.button('Enviar') 

# Conectar a la API y mostrar la respuesta 
if submit_button: 
    api_url = 'http://localhost:8000/predict'  # Reemplaza con la URL de tu API 
    payload = { 'EstadoCivil': opcion_selec1,
                'ModoAplic': opcion_selec2,
                'OrdenAplic':opcion_selec3,
                'Curso': opcion_selec4,
                'AsistDiaNoche': opcion_selecDiurno,
                'TitulPrevia': opcion_selec5,
               'Desplazado':opcion_selec8,
               'NecesidadesEducativasEspeciales': opcion_selec9,
               'Deudor':opcion_selec10,
                'MatriculasAlDia':opcion_selec11,
                'Genero':opcion_selec12,
                'Becario':opcion_selec13,
                'EdadInscripcion':user_input12,
                'UC1erSemestreMatriculadas':user_input13,
                'UC1erSemestreEvaluaciones':user_input14,
                'UC1erSemestreAprobadas':user_input15,
                'UC1erSemestreCalificacion':user_input16,
                'UC1erSemestreSinEvaluaciones':user_input17,
                'UC2doSemestreMatriculadas':user_input18,
                'UC2doSemestreEvaluaciones':user_input19,
                'UC2doSemestreAprobadas':user_input20,
                'UC2doSemestreCalificacion':user_input21,
                'UC2doSemestreSinEvaluaciones':user_input22
            } 
    response = requests.post(api_url, data=json.dumps(payload)) 
     
    if response.status_code == 200: 
        api_data = response.json() 
        st.write('Sistema de Alerta Temprana:') 
        st.write(api_data["prediction"]) 
    else: 
        st.write('Error al conectar a la API. Código de estado:', response.status_code) 