from typing import Dict, Any
from collections import defaultdict


class AnalizadorLogs:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_logs(self) -> Dict[str, Any]:
        # Diccionarios para llevar un registro de las estadísticas
        solicitudes_por_metodo = defaultdict(int)
        solicitudes_por_codigo = defaultdict(int)
        tamanio_total_respuesta = 0
        num_solicitudes = 0
        urls_solicitadas = defaultdict(int)

        with open(self.nombre_archivo) as f:
            for linea in f:
                elementos = linea.split()
                if len(elementos) != 12:
                    continue
                direccion_ip = elementos[2]
                fecha_hora = elementos[5] + ' ' + elementos[6]
                metodo_http = elementos[8]
                url = elementos[10]
                codigo_respuesta = elementos[11]
                tamanio_respuesta = int(elementos[12])

                # Actualizamos las estadísticas
                solicitudes_por_metodo[metodo_http] += 1
                solicitudes_por_codigo[codigo_respuesta] += 1
                tamanio_total_respuesta += tamanio_respuesta
                num_solicitudes += 1
                urls_solicitadas[url] += 1

        # Calculamos el tamaño promedio de respuesta
        tamanio_promedio_respuesta = tamanio_total_respuesta / num_solicitudes if num_solicitudes > 0 else 0

        # Ordenamos las URLs más solicitadas y nos quedamos con las 10 primeras
        urls_mas_solicitadas = dict(sorted(urls_solicitadas.items(), key=lambda x: x[1], reverse=True)[:10])

        # Creamos un diccionario con las estadísticas calculadas
        estadisticas = {
            "num_solicitudes": num_solicitudes,
            "solicitudes_por_metodo": dict(solicitudes_por_metodo),
            "solicitudes_por_codigo": dict(solicitudes_por_codigo),
            "tamanio_total_respuesta": tamanio_total_respuesta,
            "tamanio_promedio_respuesta": tamanio_promedio_respuesta,
            "urls_mas_solicitadas": urls_mas_solicitadas
        }

        return estadisticas



