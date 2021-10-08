import express, {json} from "express";
import { tareasRouter } from "../routes/tareas.routes";
import { conexion } from "./sequelize";



export class Server {
    constructor() {
      this.app = express();
      this.puerto = process.env.PORT || 8000;
      this.bodyParser();
      this.rutas();
    }
    bodyParser() {
        this.app.use(json())
    }
    rutas() {
        this.app.get("/",(req,res)=>{
            res.json({
                message:"Bienvenidos a mi API"
            })
        })
        this.app.use(tareasRouter)
    }
    start() {
        this.app.listen(this.puerto, async () => {
          console.log(`Servidor corriendo en el puerto ${this.puerto}`
          )
          try {
              await conexion.sync()
              console.log("Base de datos conectada exitosamente")
          } catch (error) {
              console.log(error)
          }
          
        });
    }

}