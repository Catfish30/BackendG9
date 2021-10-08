import express,{json} from "express";
import morgan from "morgan";
import { actividades_router } from "../routes/actividades";


export class Server {
  constructor() {
    this.app = express();
    this.puerto = 8000;
    this.cors();
    this.bodyParser();
    this.rutas();
  }

  bodyParser(){
    // es apra indicar en el proyecto  que formatos (body) puede enviar el front
    this.app.use(json());
    // this.app.use(raw());
  }

  rutas(){
    // middleware de morgan para que haga tracking de las consultas al backend  //ctrl+space
    this.app.use(morgan('dev'));

    this.app.use(actividades_router);

    this.app.get('/',(req,res) =>{
      res.status(200).send('Bienvenido a mi API')
    })
  }
  cors(){
    this.app.use((req,res,next)=>{
      // acces-control-allow-origin => indica los origines que pueden acceder a la API
      res.header('Access-Control-Allow-Origin','*')
      res.header('Access-Control-Allow-Headers','Content-Type,Autorization')
      res.header('Access-Control-Allow-Methods','GET,POST,PUT,DELETE')

      next();
    })
  }

  start() {
    this.app.listen(this.puerto, () => {
      // alt+96 ``
      console.log(`Servidor corriendo en el puerto ${this.puerto}`);
    });
  }
}