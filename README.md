# Despliegue de aplicaciones web en contenedores Docker

Este repositorio contiene ejemplos de despliegue de aplicaciones web en contenedores Docker utilizando diferentes lenguajes de programación. Los lenguajes incluidos son:

- Node.js
- Python
- Go
- Rust

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- Docker: [Instrucciones de instalación](https://docs.docker.com/get-docker/)

## Estructura del repositorio

El repositorio se organiza de la siguiente manera:
.
├── node
│   ├── Dockerfile
│   ├── index.js
│   └── package.json
├── python
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── go
│   ├── Dockerfile
│   ├── go.mod
│   └── main.go
└── rust
├── Cargo.toml
├── Dockerfile
└── src
└── main.rs
Copy code
Cada directorio contiene los archivos necesarios para desplegar una aplicación web en un contenedor Docker utilizando el lenguaje de programación correspondiente.

## Instrucciones de uso

1. Clona este repositorio en tu máquina local:
git clone https://github.com/tu-usuario/nombre-repositorio.git
Copy code
2. Navega hasta el directorio del lenguaje de programación que deseas utilizar:
cd nombre-repositorio/lenguaje-programacion
Copy code
3. Construye la imagen Docker:
docker build -t nombre-imagen .
Copy code
4. Ejecuta el contenedor:
docker run -p puerto-host:puerto-contenedor nombre-imagen
Copy code
Asegúrate de reemplazar `puerto-host` y `puerto-contenedor` con los puertos adecuados.

5. Abre un navegador web y accede a la aplicación en `http://localhost:puerto-host`.

## Documentación detallada

Para obtener una documentación detallada sobre cada lenguaje de programación y el proceso de despliegue en contenedores Docker, consulta los siguientes archivos:

- [Node.js](node/README.md)
- [Python](python/README.md)
- [Go](go/README.md)
- [Rust](rust/README.md)

## Contribución

Si deseas contribuir a este repositorio, siéntete libre de enviar pull requests o abrir issues para discutir mejoras o problemas encontrados.

## Licencia

Este repositorio se encuentra bajo la [Licencia MIT](LICENSE).
