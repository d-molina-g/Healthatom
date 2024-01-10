import requests
from google.cloud import bigquery
from google.cloud import secretmanager
from datetime import datetime


#Google Cloud
project_id = "david-molina-test"
secret_id = "cmf_api_key"
dataset_id = "HealthAtom"
table_id = "exchange_rates"

#Secret Manager
client = secretmanager.SecretManagerServiceClient()
name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
response = client.access_secret_version(name=name)
api_key = response.payload.data.decode("UTF-8")


#Dolar
def obtener_valor_dolar(api_key):
    url = f"https://api.sbif.cl/api-sbifv3/recursos_api/dolar?apikey={api_key}&formato=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['Dolares'][0]
    else:
        return None

#Euro
def obtener_valor_euro(api_key):
    url = f"https://api.sbif.cl/api-sbifv3/recursos_api/euro?apikey={api_key}&formato=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['Euros'][0]
    else:
        return None



valor_dolar = obtener_valor_dolar(api_key)
valor_euro = obtener_valor_euro(api_key)



#BigQuery
client = bigquery.Client(project=project_id)
table_ref = client.dataset(dataset_id).table(table_id)

#Verificamos e insertamos los datos 
if valor_dolar is not None and valor_euro is not None:
    fecha = datetime.strptime(valor_dolar["Fecha"], "%Y-%m-%d").date()
    tipo_cambio_usd = float(valor_dolar["Valor"].replace(",", "."))
    tipo_cambio_euro = float(valor_euro["Valor"].replace(",", "."))

    fila_a_insertar = [{
        "date": fecha.isoformat(),
        "usd_rate": tipo_cambio_usd,
        "euro_rate": tipo_cambio_euro
    }]

    # Insertamos la fila en BigQuery
    errores = client.insert_rows_json(table_ref, fila_a_insertar)
    if errores == []:
        print("Los datos de tipo de cambio se han insertado correctamente.")
    else:
        print("Se encontraron errores al insertar los datos:", errores)
else:
    print("No se pudo obtener los valores de tipo de cambio.")