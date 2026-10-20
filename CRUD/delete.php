<?php
include("conexion.php");

$con = conectar();

$id = $_GET['id'];

$sql = "DELETE FROM alumnos WHERE id = '$id'";
$query = mysqli_query($con,$sql);

if($query){
    header("Location: alumnos.php");
    exit();
}else{
    echo "Error al eliminar el alumno:" . mysqli_error($con);
}

?>