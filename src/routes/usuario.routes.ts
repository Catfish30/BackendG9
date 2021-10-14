import { Router } from "express";

import * as usuarioController from '../controllers/usuario.controllers'

const usuarioRouter = Router()

usuarioRouter.post("/registro",usuarioController.registroController);

export default usuarioRouter;