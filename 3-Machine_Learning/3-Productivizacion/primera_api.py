from fastapi import FastAPI

app = FastAPI()

@app.get("/v1/saludos")
def saludos():
    return "Hola Cristina y Dustin"

@app.get("/v1/despidos")
def despidos():
    """
    Función para despedir a mi amigo Lepido
    """
    return "Adios Lepido"


@app.get("/v2/saludos/{nombre}")
def super_saludos(nombre):

    return f"Hola estimado {nombre.capitalize()}"


@app.get("/v2/cuadrado/{numerin}")
def cuadrado(numerin:int):

    res = numerin**2
    return res

@app.get("/v3/corta_string/")
def corta_string(cadena:str, pos_incial:int, pos_final:int):
    return cadena[pos_incial:pos_final]



@app.post("/v3/limita_string/")
def limita_string(cadena:str, pos_incial:int, pos_final:int):
    return cadena[pos_incial:pos_final]





# v4/cargar_modelo/mymodelo.pkl/14/xtrain2scaladonovariable/1
# v4/carga_modelo/?nombre_modelo=mymodelo.pkl&version=14&dataset=xtrain2scaladonovariable&servicio=1
# v4/modelo/predict 

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import numpy as np

@app.post("/v4/model/predict")
def modelo(petal_length:float,petal_width:float):
    iris = load_iris()
    X = iris.data[:, 2:] # petal length and width
    y = iris.target
    tree_clf = DecisionTreeClassifier(max_depth=2,
                                  random_state=42)
    tree_clf.fit(X, y)
    input_data = np.array([petal_length, petal_width]).reshape(1,-1)
    prediccion = tree_clf.predict(input_data)
    res = {
        'clase':str(prediccion[0]),
        'tipo_clase':"Pepito",
        "tiempo_de_ejecucion":"poco",
        "version_del_modelo":"la ultima"
    }
    return res


