//CRUD ACTIVIDADES

const actividades = [
    {
      nombre: "Ir al gimnasio",
      hora: "6:00",
      dias: ["LUN", "MIE", "VIE"],
    },
    {
      nombre: "Aprender MongoDb",
      hora: "22:00",
      dias: ["MAR", "SAB"],
    },
  ];

export const crearActividad = (req,res) => {

    console.log(req.body) // retornara todo el body enviado dsede el front
    const {body}=req;    
    actividades.push(body);

    res.status(201).json({
        message:'Actividad creada exitosamente',
        content:body
    })
}

export const listarActividades = (req,res) => {
  
    res.status(200).json({
        message:'Las actividades son:',
        content:actividades
    })
}

export const devolverActividad = (req,res) => {

    console.log(req.params)
    const {id} = req.params;

    if (actividades.length > id) {
        return res.json({
            message:null,
            content:actividades[id],
        })
    }else{
        return res.status(404).json({
            message:"Actividad no encontrada",
            content:null,
        })
    }
}