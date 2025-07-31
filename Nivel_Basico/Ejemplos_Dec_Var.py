"""
Ejemplos Varios de Declaracion de Variables
"""

# Asignacion simple

nom_per="Armando" 
ape_per='Ruiz'
edad_per=49
sue_per=1200.98
act_per=True

# Asignaciones multiples

cant_prod,msj_bien,estado = 5,"Hola",True
#print(cant_prod)


# Asignar el mismo valor a varias variables

nom_per = 200

x = y = z = 10
#print(x)
#print(y)
#print(z)


# Tipos de Datos especiales (Estructura de datos)
"""
LIST
DICCIONARIOS
TUPLAS
CONJUNTOS
"""


cursos = ["PYTHON","DJANGO","FLASK",20,130.70,True,["FASTAPI","PANDAS"]] #list
#cursos.append()

empleados = {
              "CODIGO":"200","NOMBRE":"ARMANDO","APELLIDO":"RUIZ",
} #dict

valores = (100,200,300) #tuple  

datos = {12,45,67,89,45} #set


print(datos)

#print(empleados["NOMBRE"])

#Utiliza Keyword para mostrar una lista de palabras reservadas que tiene python
import keyword
 #print(keyword.kwlist)

#Averiguar si mi nombre de variable es palabra reservada
empleado_nom="Armando"
print(keyword.iskeyword(empleado_nom))


#Constantes se recomiendan en Mayusculas
cant=0
PI=3.14

"""
- Reglas de Nomenclatura

Nombres Descriptivos: 
    Usa nombres que reflejen el propósito de la variable. Ejemplo: total_price en lugar de tp.

Convención snake_case: 
    Para variables y nombres de funciones, usa minúsculas y separa las palabras con guiones bajos. Ejemplo: user_age.

Constantes en Mayúsculas: 
    Usa mayúsculas y guiones bajos para constantes que no deberían cambiar. Ejemplo: PI = 3.14159.

Evitar Palabras Clave: 
    No uses palabras reservadas de Python como nombres de variables. Ejemplo: class, if.

Nombres Simples y Claros: 
    Evita nombres genéricos como data o info a menos que el contexto sea claro. Prefiere nombres más específicos.
    
"""    