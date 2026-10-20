<?php
/* Recibir la informacion del formulario */
$matricula = $_POST['matricula'];
$nombre = $_POST['nombre'];
$apellido_p = $_POST['apellido_p'];
$apellido_m = $_POST['apellido_m'];
$edad = $_POST['edad'];
// Incluir la informacion del archuvo conexion.php
include("conexion.php");

//mandamos a llamar la funcion conectar
$con = conectar();

/* Crear nuestra consulta para insertar los datos */
$sql = "INSERT INTO alumnos (matricula, nombre, apellido_p, apellido_m, edad) VALUES 
('$matricula', '$nombre', '$apellido_p', '$apellido_m', '$edad')";

//Ejecutar la consulta
$query = mysqli_query($con, $sql);

if($query){
    header("Location: alumnos.php");
}else{
    echo "Error al insertar la consulta";
}


?>