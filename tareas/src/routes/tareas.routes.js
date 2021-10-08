import {Router} from 'express'
import * as tareasController from '../controllers/tareas.controllers'

export const tareasRouter = Router();

tareasRouter.route("/tareas").post(tareasController.crearTarea);