from analizador import AnalizadorLogs

if __name__ == '__main__':
    analizador = AnalizadorLogs('file/trafico_web.txt')
    estadisticas = analizador.procesar_logs()
    print(estadisticas)
