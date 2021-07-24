## API REST Django
API realizada en el framework Django usando serializadores y las tres formas principales de creacion de APIs, utilizando tambien los protocolos GET, POST, PUT, DELETE.

### Function-based Views
Usando el decorador
```sh
@api_view
```
Se diseño un access point para crear, modificar y eliminar mascotas usando funciones, el decorador permite modificar el comportamiento de las funciones para indicar que dicha función va a ser un punto de acceso
para alguna determinada peticion.

Las rutas de acceso son 
```sh
localhost:8000/pets/
```
```sh
localhost:8000/pets/<int:pk>/
```
Donde `pk` es un id de algun elemento que se quiera ver, editar o eliminar



### Class-based Views

Heredando de la clase
```sh
APIView
```
Se diseñaron clases que sirven como access point para crear, modificar y eliminar personas, al heredar de la clase `APIView` 
se obtienen de los metodos necesarios para la creacion, modificacion y eliminacion de objetos, lo que permite tener un codigo mas limpio
y mas estructurado.

Las rutas de acceso son 
```sh
localhost:8000/persons/
```
```sh
localhost:8000/persons/<int:pk>/
```
Donde `pk` es un id de algun elemento que se quiera ver, editar o eliminar



### Generic-Class-based Views

Usando la clase
```sh
generics
```
Y heredando de las clases `ListCreateAPIView` y `RetrieveUpdateDestroyAPIView` se desarrolló un access point para 
agregar, editar y eliminar vehiculos

Una de las principales ventajas de las vistas basadas en clases genericas es que el marco REST se aprovecha del uso de patrones comunes como la insersion o eliminacion de datos para proporcionar una serie de vistas preconstruidas que se encargan de realizar los patrones anteriores.

Esto permite tener un código mucho más compacto ya que las clases que se heredan de `generics` se encargan de hacer todos los procesos de forma interna


Las rutas de acceso son 
```sh
localhost:8000/cars/
```
```sh
localhost:8000/cars/<int:pk>/
```
Donde `pk` es un id de algun elemento que se quiera ver, editar o eliminar



_Para mayor compresion de como funcionan los tres metodos anteriores, ir a  [Documentacion](https://www.django-rest-framework.org/tutorial/1-serialization/)_



## Getting Started

Para poder utilizar el api, siga los pasos siguientes


### Installation

1. Clone el repositorio
   ```sh
   git clone https://github.com/elJuanjoRamos/API-REST-Python-Django.git
   ```
2. Dirijase al directorio del proyecto, dentro de la carpeta `tutorial` introduzca el comando 
   ```sh
   python manage.py runserver
   ```
4. Dirijase a 
   ```JS
   http://localhost:8000/url;
   ```

Donde `url` es cada una de las rutas de acceso indicadas con anterioridad.
