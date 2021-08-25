console.log("Hola")

const BASE_URL = "http://127.0.0.1:8000"
const btnProductos = document.getElementById('btn-traer-productos')
const nombre_producto = document.getElementById('nom_producto')
const precio_producto = document.getElementById('prec_producto')
const btnAgregar = document.getElementById('btn-agregar-producto')

fetch(`${BASE_URL}/`,{ method:"GET" }).then((respuesta) =>{
    console.log(respuesta.status)
})

 btnProductos.onclick = (e) => {
    fetch(`${BASE_URL}/productos`, { method:"GET"})
        .then((respuesta) =>{
           return respuesta.json()
        })
        .then((productos) => {
            console.log(productos)
        })
    
}

btnAgregar.onclick = async(e) => {
    
    console.log(nombre_producto.value)
    console.log(precio_producto.value)

    const respuesta = await fetch(`${BASE_URL}/productos`,{
        method: 'POST', 
        body: JSON.stringify({
            nombre: nombre_producto.value,
            precio: precio_producto.value
        }),
        headers: {
            "Content-Type":"application/json"
        },
    });

    const resultado = await respuesta.json();
    console.log(resultado)

}

// btnProductos.addEventListener("click", async () => {
//     const respuesta = await fetch(`${BASE_URL}/`,{ method:"GET" })
//     const productos = await respuesta.json()

//     console.log(productos)
// })