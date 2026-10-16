<?php

// Incluir la informacion del archuvo conexion.php
include("conexion.php");

//mandamos a llamar la funcion conectar
$con=conectar();

//Dame todo lo que tegnas en alumnos
$sql="SELECT * FROM alumnos";

//Ejecutar la consulta y tendremos acceso a la conexion
$query=mysqli_query($con,$sql);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<style>
    .table{
    Font-family: Sans-serif;
    text-align: center;
    }

    .header{
        Font-family: Sans-serif;
    }
    </style>
<body>
    <h1 class="header">Tabla de Alumnos</h1>
    <table border="1" class="table">
        <thead>
            <tr style="">
                <th style="text-align: center; padding: 10px;">Id</th>
                <th style="text-align: center; padding: 10px;">Matricula</th>
                <th style="text-align: center; padding: 10px;">Nombre</th>
                <th style="text-align: center; padding: 10px;">Apellido Paterno</th>
                <th style="text-align: center; padding: 10px;">Apellido Materno</th>
                <th style="text-align: center; padding: 10px;">Edad</th>
                <th style="text-align: center; padding: 10px;">Acciones</th>
            </tr>
            
        </thead>

        <tbody>
            <tr> 
                <td style="text-align: center; padding: 10px;">1 </td>
                <td style="text-align: center; padding: 10px;">125052723 </td>
                <td style="text-align: center; padding: 10px;">Mathias Santiago </td>
                <td style="text-align: center; padding: 10px;">Reyes </td>
                <td style="text-align: center; padding: 10px;">Antunez </td>
                <td style="text-align: center; padding: 10px;">18 </td>
                <td style="text-align: center; padding: 10px;">Editar <br> Eliminar </td>
             </tr> 
        </tbody>
</body>
</html>