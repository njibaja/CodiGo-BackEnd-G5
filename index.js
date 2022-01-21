import express, {json} from "express";
import { append } from "vary";
//const express = require("express");

const productos = [
    {
        nombre:"leche de almendra",
        precio: 9.5,
        estado: true,
    }
]

const app = express();
//middleware > es un intermerdiario entre todas las peticiones que se realicen a determinado endpoint o si no se indica a todas las peticiones de mi API

//aqui digo que mi aplicacion de express podra entender toda la informacion enviada por el cliente siempre y cuando sea un json.
app.use(json());
const port = 3000;

app.get('/', (req, res)=> {
    // req > es la informacion que viene del cliente
    // res > es la respuesta que le dare al cliente
    res.status(200).json({
        message : 'Peticion realizada existosamente',
    })
})



app.post('/producto', (req, res)=>{
    console.log(req.body);

    if(req.body){
        productos.push(req.body);
        res.status(201).json({
            message: "Producto agregado existosamente",
            producto: req.body,
        });
    } else {
        res.status(400).json({
            message: "Informacion incorrecta",            
        });
    }
})


app.get('/productos', (req, res)=> {    
    res.status(200).json({
        message : 'Los productos son',
        content : productos
    })
});


app
    .route('/producto/:id')
    .get((req,res)=>{
        //destructuracion
        const { id } = req.params;
        //const { id: nuevoId } = req.params; > destructuracion con renombre de variable.
        //const id = req.params.id > OBSOLETO
        
        //buscar ese producto por ese id (posicion del array) y si existe, retornar el producto 200 
        //si no existe retornar un estado 200 e indicar en el mensaje que el producto no existe

        if(productos[id-1] != undefined){
            console.log(productos[id-1]);
            return res.status(200).json({
                message: "Existe",            
                content: productos[id]
            });            
        } else {
            res.status(200).json({
                message: "No existe",            
            });            
        }
    })
    .put((req,res)=>{
        const { id } = req.params;
        if(productos[id-1] != undefined){
            productos[id -1] = req.body;

            return res.status(200).json({
                message: "Producto actualizado exitosamente",            
                content: productos[id-1],
            });            
        } else {
            res.status(400).json({
                message: "Producto no existe",            
                content: null,
            });            
        }
    })
    .delete((req,res)=>{
        const { id } = req.params;
        if(productos[id-1]) {
            const producto = productos[id-1];

            productos.splice(id-1,1);

            return res.status(200).json({
                message: "Producto eliminado exitosamente",            
                content: producto,
            });            
        } else {
            res.status(400).json({
                message: "Producto no existe",            
                content: null,
            });            
        }
    })

// se mantendra escuchando las consultas realzadas a este servidor mediante el puerto definido
app.listen(port, () =>{
    //esto sucedera cuando se levante el servidor de express
    console.log(`Servidor levantado exitosamente! ${port}`);
});



