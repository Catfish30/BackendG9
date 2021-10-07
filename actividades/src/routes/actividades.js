import {Router} from 'express'
import {crearActividad} from '../controllers/actividades'
import { listarActividades } from '../controllers/actividades';
import { devolverActividad } from '../controllers/actividades';

export const actividades_router = Router();
actividades_router.post('/actividad',crearActividad);
actividades_router.get('/actividades',listarActividades);
actividades_router.get('/actividades/:id',devolverActividad);
