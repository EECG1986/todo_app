# ToDo App Django

## Instrucciones para Configurar y Ejecutar el Proyecto

1. Clonar el repositorio:
   ```bash
   git clone <URL_del_repositorio>
   cd todo_project

2. Crear un entorno virtual y activarlo:
   ```python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`

3. Instalar las dependencias:
   instalar python
   instalar django  # pip install django
   pip install -r requirements.txt
   
4. Realizar migraciones y correr el servidor:
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver

5. Crear un Superusuario
   Crear un superusuario para acceder a la interfaz de administración de Django:
   python manage.py createsuperuser


Estructura del Proyecto

    todo_project/: Contiene la configuración del proyecto Django.
    tasks/: Contiene la aplicación principal de tareas.
    templates/: Contiene los templates HTML.
    static/: Contiene archivos estáticos como CSS.

Decisiones de Diseño

    Se utiliza el sistema de autenticación de Django para manejar usuarios.
    Cada usuario tiene sus propias tareas y no puede acceder a las tareas de otros usuarios.
    Se utilizan templates de Django para renderizar la interfaz de usuario.

