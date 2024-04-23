"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    df.sexo = df.sexo.str.lower()


    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()

    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.str.replace("-", " ")
    df.idea_negocio = df.idea_negocio.str.replace("_", " ")
    #df.idea_negocio = df.idea_negocio.str.strip()
    #df.idea_negocio = df.idea_negocio.str.replace("y", "")
    #df.idea_negocio = df.idea_negocio.str.replace("de", "")
    #df.idea_negocio = df.idea_negocio.str.strip()
    #df.idea_negocio = df.idea_negocio.str.replace(".", " ")
    #df = df.assign(key=df.idea_negocio)
    #df = set(df.key.to_list())
    # df.key = df.key.str.lower()
    # df.key = df.key.str.replace("-", " ")
    # df.key = df.key.str.replace("_", " ")
    # df.key = df.key.map(lambda x: [word.lemmatize("v") for word in TextBlob(x).words])
    # df.key = df.key.map(sorted)
    # df.key = df.key.str.join(" ")
    # df.key = df.key.str.replace(r"\bde\b", "", regex=True)
    # df.key = df.key.str.replace(r"\bpara\b", "", regex=True)
    # df.key = df.key.str.replace(r"\bel\b", "el", regex=True)
    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.str.replace("-", " ")
    df.barrio = df.barrio.str.replace("_", " ")
    #df.barrio = df.barrio.str.replace(".", " ")

    df.estrato = df.estrato.astype("category")
    
    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)
    #df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, infer_datetime_format=True, dayfirst= False, format="%Y-%m-%d",errors="ignore")
    df.fecha_de_beneficio = pd.to_datetime(
        df.fecha_de_beneficio,
        dayfirst = True,
        format='mixed',
    )

    df.monto_del_credito = df.monto_del_credito.str.replace(",", "")
    df.monto_del_credito = df.monto_del_credito.str.replace(".00", "")
    
    df.monto_del_credito = df.monto_del_credito.str.replace(" ", "")
    df.monto_del_credito = df.monto_del_credito.str.strip("$")


    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.str.replace("-", " ")
    df.línea_credito = df.línea_credito.str.replace("_", " ")
    #df.línea_credito = df.línea_credito.str.replace(" ", "")
    #df.línea_credito = df.línea_credito.str.replace(".", "")


    df.dropna(inplace = True)
    df.drop_duplicates(inplace=True)
    #df = df.tipo_de_emprendimiento.value_counts()
    #df = df.tipo_de_emprendimiento.value_counts()


    return df

#print(clean_data())