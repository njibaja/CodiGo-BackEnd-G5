import express from "express";
import { append } from "vary";
//const express = require("express");

const app = express();
const port = 3000;

append.get('/', (req, res)=> {
    // req > es la informacion que viene del cliente
    // res > es la respuesta que le dare al cliente
    res.status(200).json({
        message : 'Peticion realizada existosamente',
    })
})

// se mantendra escuchando las consultas realzadas a este servidor mediante el puerto definido
app.listen(port, () =>{
    //esto sucedera cuando se levante el servidor de express
    console.log(`Servidor levantado exitosamente! ${port}`);
});



