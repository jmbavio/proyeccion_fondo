# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:13:10 2024

@author: jose
"""

#  python -m streamlit run (arbol de directorio/app.py 


def fecha_nac(fecha,sexo):
    import datetime

    fecha_nac1=datetime.datetime.strptime(str(fecha)[5:15], "%Y-%m-%d")
    # hacer control de lo ingresado
    # convertirlo en formato
    if sexo=='M':
        edad_66 = fecha_nac1.replace(year=fecha_nac1.year + 65)
    else:
        edad_66 = fecha_nac1.replace(year=fecha_nac1.year + 60)


    return fecha_nac1.strftime("%d-%m-%Y"),edad_66



import io
import pandas as pd

# d,sexo,Fnacimiento,EdadEnAños,Edad,fechaIngreso,AñosActividad,porcentajeAporte,fondoActual,salarioBruto,Escalafon


# df_aportes=pd.read_csv(io.StringIO(str_aportes), sep=",")

def datos_iniciales(id):


    return df_aportes[df_aportes.Id==id]


from datetime import datetime, timedelta
import datetime
def rango_meses(fecha_inicio, fecha_fin,edad_66):
    import datetime
    from datetime import timedelta
    # Convertir las fechas de string a objetos datetime
    fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d")
    if fecha_fin=='':
        fecha_fin=edad_66.strftime("%d-%m-%Y")

    fecha_fin = datetime.datetime.strptime(fecha_fin, "%d-%m-%Y")

    # Inicializar la lista de resultados
    lista_meses = []

    # Iterar desde la fecha de inicio hasta la fecha de fin
    while fecha_inicio <= fecha_fin:
        # Agregar el mes y año a la lista en formato "YYYY-MM"
        lista_meses.append(fecha_inicio.strftime("%Y-%m"))
        # Avanzar al siguiente mes
        # Si el mes es diciembre, incrementar el año y resetear el mes a enero
        year = fecha_inicio.year + (fecha_inicio.month // 12)
        month = (fecha_inicio.month % 12) + 1
        fecha_inicio = fecha_inicio.replace(year=year, month=month)

    return lista_meses



def calcular_ant(fecha_inicio, fecha_consulta):
    import datetime
    from dateutil.relativedelta import relativedelta
    # Convertir ambas fechas en objetos datetime
    fecha_nacimiento = datetime.datetime.strptime(fecha_inicio, "%Y-%m")
    fecha_consulta = datetime.datetime.strptime(fecha_consulta, "%Y-%m")

    # Calcular la diferencia en años
    diferencia = relativedelta(fecha_consulta, fecha_nacimiento)
    return min(diferencia.years,24)

# def generar_df_cargo(cargo1):
#     df=pd.DataFrame(columns=['Mes','Cargo','Ded','Antig','Edad','Bruto','Aporte'])
#     iterable= rango_meses(cargo1[2],cargo1[3],cumple66)


#     for i in iterable:

#         idx=iterable.index(i)
#         if pd.isna(df.Mes.min()):
#             inicio=iterable[0]
#         else:
#             inicio=iterable[0]

#         try:
#             df.loc[idx]=[i,cargo1[0],cargo1[1],calcular_ant(inicio,i),calcular_edad(nacim,i),None,None]
#         except:
#             pass# df.Cargo[idx]=cargo1[0]
#         # df.Ded[idx]=cargo1[1]
#         # df.Edad[idx]=40
#     for i in df.index:

#         df.Aporte[i]=calc_aporte(cargo1[0], cargo1[1], df.Antig[i], df.Edad[i],df.Mes[i][-2:])
#     return df

import numpy as np
aporte_fondo=np.array([[20, 2.0],
 [21, 2.0],
 [22, 2.0],
 [23, 2.0],
 [24, 2.0],
 [25, 2.0],
 [26, 2.0],
 [27, 2.0],
 [28, 2.0],
 [29, 2.5],
 [30, 2.5],
 [31, 2.5],
 [32, 2.5],
 [33, 2.5],
 [34, 2.5],
 [35, 2.5],
 [36, 2.5],
 [37, 2.5],
 [38, 2.5],
 [39, 2.5],
 [40, 2.5],
 [41, 3.0],
 [42, 3.0],
 [43, 3.0],
 [44, 3.0],
 [45, 3.0],
 [46, 3.0],
 [47, 3.0],
 [48, 3.0],
 [49, 3.0],
 [50, 3.0],
 [51, 3.5],
 [52, 3.5],
 [53, 3.5],
 [54, 3.5],
 [55, 3.5],
 [56, 3.5],
 [57, 3.5],
 [58, 3.5],
 [59, 3.5],
 [60, 3.5],
 [61, 3.5],
 [62, 3.5],
 [63, 3.5],
 [64, 3.5],
 [65, 3.5],
 [66, 3.5],
 [67, 3.5],
 [68, 3.5],
 [69, 3.5],
 [70, 3.5]])






# id=141
# afiliado=datos_iniciales(id)

# nacim,cumple66=fecha_nac(afiliado.Fnacimiento)

# hoy=str(datetime.datetime.today())[0:10]
# iterable= rango_meses(hoy,'',cumple66)


# mask_ordi=df_cargos[df_cargos.id==id].caracter=='ORDI'
# cargos_continuan=df_cargos[df_cargos.id==id].categoriaDescripcion[mask_ordi]



def calcular_edad(fecha_nacimiento, fecha_consulta):
    from dateutil.relativedelta import relativedelta
    import datetime
    # Convertir ambas fechas en objetos datetime
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
    fecha_consulta = datetime.datetime.strptime(fecha_consulta, "%Y-%m")

    # Calcular la diferencia en años
    diferencia = relativedelta(fecha_consulta, fecha_nacimiento)
    return diferencia.years









def calculo_flujo(df_aportes):
    import pandas as pd
    import numpy as np
    import datetime
    from dateutil.relativedelta import relativedelta

    # afiliado=datos_iniciales(id)
    afiliado=df_aportes
    nacim,cumple66=fecha_nac(afiliado.Fnacimiento,afiliado.sexo.values[0])

    hoy=str(datetime.datetime.today())[0:10]

    iterable= rango_meses(hoy,'',cumple66)


    df_flujo=pd.DataFrame(columns=['Mes','Edad','Antig','porcentajeAporte','Aporte','Acumulado','salarioBruto'])
    df_flujo.loc[0]=[iterable[0],calcular_edad(nacim,iterable[0]),calcular_ant(afiliado.fechaIngreso.values[0][:7],hoy[:7]),afiliado.porcentajeAporte.values[0]/100,afiliado.salarioBruto.values[0]*afiliado.porcentajeAporte.values[0]/100,afiliado.fondoActual.values[0],afiliado.salarioBruto.values[0]]
    fondo_actual=afiliado.fondoActual.values[0]
    basico=afiliado.salarioBruto.values[0]/(1+antiguedad[calcular_ant(afiliado.fechaIngreso.values[0][:7],hoy[:7])][1])
    print(fondo_actual)
    for i in iterable[1:]:
        print(i)

        idx=iterable.index(i)
        edad=calcular_edad(nacim,i)
        antig=calcular_ant(afiliado.fechaIngreso.values[0][:7],i)
        if antig>24:
            antig=24


        aporte_segun_edad=aporte_fondo[aporte_fondo[:,0]==edad][0][1]/100
        print(aporte_segun_edad)
        salarioBruto=basico+(basico*antiguedad[antig][1])
        fondo_actual+=salarioBruto*aporte_segun_edad
        df_flujo.loc[idx]=[i,edad,antig,aporte_segun_edad,salarioBruto*aporte_segun_edad,fondo_actual,salarioBruto]

    return df_flujo.round(3)








def suma_con_interes(interes):
    # interes=1.02
    int02=[df_flujo.Acumulado.values[0]]
    for i in total_df.index:
        if i[-2:]=='08':
            int02.append(int02[-1]*(interes)+df_flujo.Aporte[df_flujo.Mes==i].values[0])
        else:
            int02.append(int02[-1]+df_flujo.Aporte[df_flujo.Mes==i].values[0])
    return int02[1:]



















# for i in range(len(mask_ordi)):
#     nombre='cargo'+str(i)
#     exec('afiliado["'+nombre+'"]=[cargos_continuan.iloc['+str(i)+']]')








#     try:
#         df.loc[idx]=[i,,cargo1[1],calcular_ant(inicio,i),calcular_edad(nacim,i),None,None]
#     except:
#         pass# df.Cargo[idx]=cargo1[0]
#     # df.Ded[idx]=cargo1[1]
#     # df.Edad[idx]=40
























antiguedad= [
    [0, 0.2],
    [1, 0.2],
    [2, 0.2],
    [3, 0.2],
    [4, 0.2],
    [5, 0.3],
    [6, 0.3],
    [7, 0.4],
    [8, 0.4],
    [9, 0.4],
    [10, 0.5],
    [11, 0.5],
    [12, 0.6],
    [13, 0.6],
    [14, 0.6],
    [15, 0.7],
    [16, 0.7],
    [17, 0.8],
    [18, 0.8],
    [19, 0.8],
    [20, 1.0],
    [21, 1.0],
    [22, 1.1],
    [23, 1.1],[24, 1.2]
]














import streamlit as st
from datetime import datetime

# Título de la aplicación
st.title("Cálculo con Datos Ingresados")

# Campo para ingresar la fecha de nacimiento
fecha_nacimiento = str(st.date_input("Ingrese su fecha de nacimiento",datetime(1990, 5, 5, 0, 0),min_value=datetime(1950, 5, 5, 0, 0),format='YYYY-MM-DD'),)

sexo = st.selectbox("Sexo",['M','F'])

# Campo para ingresar la fecha de inicio de actividad
fecha_inicio = str(st.date_input("Ingrese la fecha de ingreso en la uns",datetime(2005, 5, 5, 0, 0),min_value=datetime(1950, 5, 5, 0, 0),format='YYYY-MM-DD'))

# Campo para ingresar una cantidad de dinero
cantidad_dinero = st.number_input("Ingrese su sueldo bruto", min_value=100000)

# Desplegable para seleccionar el nivel educativo
# nivel_educativo = st.selectbox("Seleccione su nivel educativo", ["Ninguno","Doctorado", "Magister", "Especialización"])


# d,sexo,Fnacimiento,EdadEnAños,Edad,fechaIngreso,AñosActividad,porcentajeAporte,fondoActual,salarioBruto,Escalafon

df_aportes=pd.DataFrame(columns=['id','sexo','Fnacimiento','EdadEnAños','Edad','fechaIngreso','AñosActividad','porcentajeAporte','fondoActual','salarioBruto','Escalafon'])
df_aportes.loc[len(df_aportes)]=[None,sexo,fecha_nacimiento,None,None,fecha_inicio,None,0,0.0,cantidad_dinero,None]

st.set_option('deprecation.showPyplotGlobalUse', False)
# Botón para calcular
if st.button("Calcular"):
    # Aquí llamas a tu función con los datos ingresados
    df_flujo = calculo_flujo(df_aportes)
    # resultado= 5000
    
    
    
    total_df=pd.DataFrame({'Edad':df_flujo.Edad.values,'0%':df_flujo.Aporte.values.cumsum()+df_flujo.Acumulado[0]},index=df_flujo.Mes)
    # total_df['acumulado']=total_df['0%'].values.cumsum()
    import datetime
    mask_mes=[datetime.datetime.strptime(total_df.index[i],"%Y-%m").month==8 for i in range(len(total_df))]
    
    total_df['2%']=suma_con_interes(1.02)
    total_df['4%']=suma_con_interes(1.04)
    total_df['6%']=suma_con_interes(1.06)
    total_df['8%']=suma_con_interes(1.08)
    
    
    total_df['0%_rel']=total_df['0%']/df_flujo.salarioBruto.values[-1]
    
    total_df['2%_rel']=suma_con_interes(1.02)/df_flujo.salarioBruto.values[-1]
    total_df['4%_rel']=suma_con_interes(1.04)/df_flujo.salarioBruto.values[-1]
    total_df['6%_rel']=suma_con_interes(1.06)/df_flujo.salarioBruto.values[-1]
    total_df['8%_rel']=suma_con_interes(1.08)/df_flujo.salarioBruto.values[-1]
    
    
    
    total_df.round(2)

    ax=total_df.plot(y=total_df.columns[1:6], use_index=True)
    import matplotlib.pyplot as plt
    
    len(total_df)
    plt.text(0.0, total_df['0%'].values[0], 'Fondo actual: '+str(total_df['0%'].values[0]), fontsize=10)
    # plt.text(0.0, 0.0, 'Aporte actual: '+str(total_df.acumulado.values[0]), fontsize=10)
    
    sep=(total_df['0%'].values[-1]-total_df['0%'].values[0])/4
    plt.text(0.0, total_df['0%'].values[-1]+sep, 'Edad: '+str(df_flujo.Edad[0]), fontsize=10)
    plt.text(0.0, total_df['0%'].values[-1]+2*sep, 'Bruto Inicial: '+str(df_flujo.salarioBruto[0]), fontsize=10)
    plt.text(0.0, total_df['0%'].values[-1]+3*sep, 'Meses: '+str(len(df_flujo)), fontsize=10)
    
    
    plt.text(len(total_df)*.66, total_df['0%'].values[-1], 'Fondo proy. jubilacion: '+str(total_df['0%'].values[-1].round(2))+'--'+str(total_df['0%_rel'].values[-1].round(2)), fontsize=10)
    
    
    plt.text(len(total_df)*.66, total_df['2%'].values[-1], 'Fondo proy. jubilacion: '+str(total_df['2%'].values[-1].round(2))+'--'+str(total_df['2%_rel'].values[-1].round(2)), fontsize=10)
    
    
    plt.text(len(total_df)*.66, total_df['4%'].values[-1], 'Fondo proy. jubilacion: '+str(total_df['4%'].values[-1].round(2))+'--'+str(total_df['4%_rel'].values[-1].round(2)), fontsize=10)
    
    
    plt.text(len(total_df)*.66, total_df['6%'].values[-1], 'Fondo proy. jubilacion: '+str(total_df['6%'].values[-1].round(2))+'--'+str(total_df['6%_rel'].values[-1].round(2)), fontsize=10)
    
    
    plt.text(len(total_df)*.66, total_df['8%'].values[-1], 'Fondo proy. jubilacion: '+str(total_df['8%'].values[-1].round(2))+'--'+str(total_df['8%_rel'].values[-1].round(2)), fontsize=10)

    st.pyplot()    
    
    st.write("El resultado del cálculo es:", df_flujo)
    
    
    

























