import cherrypy

class Calculadora:
    @cherrypy.expose
    def index(self):
        return '''
            <html>
                <head>
                    <title>Calculadora</title>
                </head>
                <body>
                    <h2>Calculadora Simple</h2>
                    <form method="post" action="result">
                        <label for="num1">Número 1:</label>
                        <input type="text" id="num1" name="num1"><br><br>

                        <label for="num2">Número 2:</label>
                        <input type="text" id="num2" name="num2"><br><br>

                        <label for="operation">Operación:</label>
                        <select id="operation" name="operation">
                            <option value="sumar">Sumar</option>
                            <option value="restar">Restar</option>
                        </select><br><br>

                        <button type="submit">Calcular</button>
                    </form>
                </body>
            </html>
        '''

    @cherrypy.expose
    def result(self, num1, num2, operation):
        try:
            num1 = float(num1)
            num2 = float(num2)

            if operation == 'sumar':
                resultado = num1 + num2
            elif operation == 'restar':
                resultado = num1 - num2
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Por favor ingresa números válidos"

        return f'''
            <html>
                <head><title>Resultado</title></head>
                <body>
                    <h2>Resultado</h2>
                    <p>{resultado}</p>
                    <a href="/">Volver a la calculadora</a>
                </body>
            </html>
        '''

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})
    cherrypy.quickstart(Calculadora())
