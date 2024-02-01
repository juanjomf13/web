import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def obtener_archivos_texto(url):
    try:
        # Realizar una solicitud GET a la URL
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa (código 200)
        if response.status_code == 200:
            # Crear un objeto BeautifulSoup para analizar el HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Buscar todos los enlaces en la página
            enlaces = soup.find_all('a')

            archivos_txt = []
            # Iterar sobre los enlaces
            for enlace in enlaces:
                # Obtener la URL completa del enlace
                enlace_completo = urljoin(url, enlace.get('href'))
                # Verificar si el enlace termina con '.txt' para considerarlo un archivo de texto
                if enlace_completo.endswith('.txt'):
                    archivos_txt.append(enlace_completo)

            # Imprimir la lista de archivos de texto encontrados
            print("Archivos de texto encontrados:")
            for archivo in archivos_txt:
                print(archivo)

        else:
            print("Error al obtener la página. Código de estado:", response.status_code)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    url = input("Introduce la URL de la página web: ")
    obtener_archivos_texto(url)