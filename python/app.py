from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Saludo desde Arauca, Colombia</title>
            <style>
                body {
                    background-color: #f2f2f2;
                    font-family: Arial, sans-serif;
                    text-align: center;
                }
                
                .container {
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #fff;
                    border-radius: 10px;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                }
                
                h1 {
                    color: #333;
                    font-size: 28px;
                    margin-bottom: 20px;
                }
                
                p {
                    color: #666;
                    font-size: 18px;
                    line-height: 1.5;
                }
                
                .highlight {
                    color: #ff6f00;
                    font-weight: bold;
                }
                
                .logo {
                    width: 150px;
                    margin-bottom: 20px;
                }
                
                .footer {
                    margin-top: 30px;
                    color: #999;
                    font-size: 14px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <img class="logo" src="https://upload.wikimedia.org/wikipedia/commons/d/df/Logo_UNIR.png" alt="Logo UNIR">
                <h1>¡Un saludo desde Arauca, Colombia!</h1>
                <p>Queridos compañeros de la <span class="highlight">UNIR</span>,</p>
                <p>Les envío un cálido saludo desde la hermosa tierra de Arauca, Colombia. Espero que todos se encuentren bien y disfrutando de esta increíble experiencia de aprendizaje.</p>
                <p>Sigamos adelante con entusiasmo y dedicación en nuestros estudios. ¡Juntos alcanzaremos grandes logros!</p>
                <p>Un abrazo virtual,<br>
                Javier Dario Diaz Torres</p>
                <div class="footer">
                    Universidad Internacional de La Rioja (UNIR) - 2024
                </div>
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)