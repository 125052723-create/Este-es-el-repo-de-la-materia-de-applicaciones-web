<?php

// Incluir la informacion del archuvo conexion.php
include("conexion.php");

//mandamos a llamar la funcion conectar
$con = conectar();

//Dame todo lo que tegnas en alumnos
$sql = "SELECT * FROM alumnos";

//Ejecutar la consulta y tendremos acceso a la conexion
$query = mysqli_query($con, $sql);

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<style>
    .table {
        Font-family: Sans-serif;
        text-align: center;
    }

    .header {
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
            <?php
            while($row=mysqli_fetch_array($query)){
            ?>
            <tr style="text-align: center; Font-family: Sans-serif; padding: 10px;">
                <td style="text-align: center; padding: 10px"><?php echo $row['id']?></td>
                <td style="text-align: center; padding: 10px"><?php echo $row['matricula']?></td>
                <td style="text-align: center; padding: 10px;"><?php echo $row['nombre']?></td>
                <td style="text-align: center; padding: 10px;"><?php echo $row['apellido_p']?></td>
                <td style="text-align: center; padding: 10px;"><?php echo $row['apellido_m']?></td>
                <td style="text-align: center; padding: 10px;"><?php echo $row['edad']?></td>
                <td> 
                    <a href="delete.php?id=<?php echo $row['id']; ?>"> Eliminar <br> Editar</a>
                </td>
            </tr>
            <?php
            }
            ?>
        </tbody>
    </table>

    <h1 style="Font-family: Sans-serif;">FORMULARIO</h1>
    <form action="insertar.php" method="POST">
        <input type="text" class="form-control" name="matricula" placeholder="Matricula">
        <input type="text" class="form-control" name="nombre" placeholder="Nombre(s)">
        <input type="text" class="form-control" name="apellido_p" placeholder="Apellido Paterno">
        <input type="text" class="form-control" name="apellido_m" placeholder="Apellido Materno">
        <input type="text" class="form-control" name="edad" placeholder="Edad">
        <button type="submit">Guardar</button>
    </form>
</body>

</html>