# 🤖 Boti - Bot de Telegram en Python

Este proyecto es un bot de Telegram desarrollado en Python que utiliza la biblioteca `python-telegram-bot`. El bot está diseñado para interactuar con los usuarios y proporcionar diversas funcionalidades, como recordar eventos y manejar comandos personalizados.

## 🌟 Funcionalidades Principales

- **🚀 Inicio**: El bot puede iniciar y saludar a los usuarios.
- **⏰ Recordatorios**: Permite a los usuarios establecer recordatorios para eventos importantes.
- **🛠️ Manejo de Comandos**: Responde a comandos específicos y maneja entradas no válidas de manera adecuada.
- **📅 Programación de Tareas**: Utiliza `APScheduler` para programar tareas y eventos.

## 🛠️ Tecnologías Utilizadas

- **🐍 Python**: Lenguaje de programación principal.
- **🤖 python-telegram-bot**: Biblioteca para interactuar con la API de Telegram.
- **🔐 dotenv**: Para manejar variables de entorno de manera segura.
- **⏲️ APScheduler**: Para la programación de tareas.

## 📋 Requisitos

- Python 3.6 o superior
- Un archivo `.env` con la clave de API de Telegram (`TELEGRAM_API_KEY`).

## 🚀 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/cristianeze16/bot_telegram.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd bot_telegram
   ```
3. Crea y activa un entorno virtual:
   ```bash 
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
5. Crea un archivo .env en el directorio raíz del proyecto y añade tu clave de API de Telegram:
   ```bash
   TELEGRAM_API_KEY=tu_clave_de_api
   ```

📄 Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.