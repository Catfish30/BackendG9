import express, {Express,json} from 'express';
import conexion from "./sequelize"
import usuarioRouter from "../routes/usuario.routes"
import imagenRouter from '../routes/imagen.routes';
import { v2 } from 'cloudinary'
import productoRouter from '../routes/producto.routes';

export class Server{

    private readonly app: Express;
    private readonly puerto: number;

    constructor(){
         this.app = express();
         this.puerto = 8000;
         this.bodyParser();
         this.rutas();
         v2.config({
            cloud_name: process.env.CLOUDINARY_NAME,
            api_key: process.env.CLOUDINARY_API_KEY,
            api_secret: process.env.CLOUDINARY_API_SECRET,
          });
    }

    private bodyParser() {
        this.app.use(json())
    }
    private rutas() {
        this.app.use(usuarioRouter);
        this.app.use(imagenRouter)
        this.app.use(productoRouter)
    }

    public start(){
        this.app.listen(this.puerto, async ()=>{
            console.log(`Servidor corriendo exitosamente en el puerto ${this.puerto}`)
            await conexion.sync();
            console.log("Base de datos conectada exitosamente")
        })
    }


}