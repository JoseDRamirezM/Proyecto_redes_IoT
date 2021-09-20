# Proyecto monitor invernaderos IoT
Universidad Distrital Francisco José de Caldas  
José David Ramírez Maldonado 20181020047  
Bogotá, Colombia

<hr>

Este proyecto utiliza el framework Django para desarrollo web y la tecnologia arduino.
Junto con un cluster de MongoDB Cloud con una comunicación segura utilizando el protocolo SSL.
Por tanto un prerequisito es la instalacion de Python (version 2.7 o posteriores).

Proceso de instalación.  

<ol>
  <li>En el CMD de windows, ingresar <code>pip install django</code></li>
  <li>En el CMD de windows, ingresar <code>pip install djongo</li>
  <li>En la carpeta monitor abrir CMD</li>
  <li>Ingresar <code>python manage.py runserver</code></li>
</ol>

De esta manera se tiene ejecutando el proyecto en la direccion IP y puerto especificados por el CMD.  
El correcto funcionamiento implica tener el sistema de adquisición de datos conectado correctamente.  

# Control de acceso a los datos

Página de inicio de sesión


<img src="https://i.ibb.co/XxSfMK3/login.png" align="left"/>


Aquí el usuario deberá ingresar las siguientes credenciales.

<ul>
  <li>Usuario: admin</li>
  <li>Constraseña: inverdadero4dmin</li>
</ul>

Una vez se inicia sesión se tiene acceso a los datos en vivo y al histórico.

<hr>

# Interfaces de usuario    
Página principal    


<img src="https://i.ibb.co/12F0N4P/UI-1.png" align="left"/>   

Página de datos historicos   


<img src="https://i.ibb.co/85PX1x3/UI-2.png" align="left"/>  

Como los datos se leen cada segundo, podemos ver lecturas similares o iguales  

<hr>

# Cluster de MongoDB cloud  
<img src="https://i.ibb.co/vsGJpXS/DB-1.png" align="left"/>  

Datos almancenados   


<img src="https://i.ibb.co/THTLxYp/DB-2.png" align="left"/>

Gráficos de datos


<img src="https://i.ibb.co/8c6xQFf/Opera-Snapshot-2021-02-23-095353-charts-mongodb-com.png" align="left"/>

<hr>

