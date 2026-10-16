<?php

/* Creamos uan funcion llamada conectar  */
function conectar(){
/* Informacion del servidor  */

$host='localhost';
$user='root';
$pass='';

/* Base de datos      */
$db='appsweb';

/* Permitir conectarnos a MySQL */
$con=mysqli_connect($host,$user,$pass);

mysqli_select_db($con, $db);

return $con;
}


?>