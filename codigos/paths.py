"""Modulo de los distintos Paths que se dispone para la tarea.

L_WNN -> list[str]:
    Lista con las semanas en formato 'wNN', donde NN es un valor entre 14 y 17.

PATH_DATA -> str:
    Path para la carpeta 'data'.
PATH_RAW -> str:
    Path para la carpeta 'raw'.

dict_path_raw -> dict[str]:
    Diccionario de las distintas rutas de las carpetas 'wNN'.
dict_csv_mc_a -> dict[str]:
    Diccionario de las distintas rutas para acceder a los 
    archivos .csv del formato 'metrocuadrado_all_wNN.csv'.
dict_csv_mc_f -> dict[str]:
    Diccionario de las distintas rutas para acceder a los 
    archivos .csv del formato 'metrocuadrado_furnished_wNN.csv'.
"""
import os.path

# Lista de las semanas, formato 'wNN'
L_WNN = ['w' + str(week) for week in [13, 14, 15, 16, 17]] 
MC_A = 'metrocuadrado_all_'
MC_F = 'metrocuadrado_furnished_'

#: Path principal
PATH_MAIN = '..'
#: Path de la data
PATH_DATA = os.path.join(PATH_MAIN, 'data')
#: Path de la carpeta 'raw'
PATH_RAW = os.path.join(PATH_DATA, 'raw')
#: Path de asignacion_upz
PATH_ASIG_UPZ = os.path.join(PATH_DATA, 'asignacion_upz')
#: Path de estadisticas_upz
PATH_EST_UPZ = os.path.join(PATH_DATA, 'estadisticas_upz')

#: Diccionario de las carpetas wNN. Se ingresa con la llave 'wNN'
dict_path_raw = {
    wNN:os.path.join(PATH_RAW, wNN) for wNN in L_WNN
}
#: Diccionario de los path a los .csv de 'metrocuadrado_all_wNN.csv'
dict_csv_mc_a = {
    wNN:os.path.join(dict_path_raw[wNN], MC_A+wNN+'.csv') for wNN in L_WNN
}
#: Diccionario de los path a los .csv de 'metrocuadrado_furnished_wNN.csv'
dict_csv_mc_f = {          
    wNN:os.path.join(dict_path_raw[wNN], MC_F+wNN+'.csv') for wNN in L_WNN
}

#: Path al .csv de 'barrio-upz.csv'
path_csv_barrio_upz = os.path.join(PATH_ASIG_UPZ, 'barrio-upz.csv')

#: Diccionario para las rutas de la carpeta estadisticas_upz
L_est_upz = [
    'estadisticas_poblacion',
    'indice_inseguridad',
    'porcentaje_areas_verdes'
]
dict_csv_est_upz = {
    name_csv:os.path.join(PATH_EST_UPZ, name_csv + '.csv') for name_csv in L_est_upz
}