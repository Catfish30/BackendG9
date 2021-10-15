import { verify } from 'jsonwebtoken'
import { Request, Response, NextFunction } from 'express'
import { usuarioDto } from '../dtos/response/usuario.dto'
import { Model } from 'sequelize'
import { Usuarios } from '../config/models'

export interface RequestUser extends Request {
    usuario?: Model

}


export const authValidator = async (req: RequestUser, res: Response, next: NextFunction) => {
    if(!req.headers.authorization){
        return res.status(401).json({
            message: "Se necesita una token para esta peticion",
            content: null,
        })
    }
    const token = req.headers.authorization.split(" ")[1]
    try {
        const payload = verify(token, process.env.JWT_TOKEN ?? "")
        
        if(typeof payload === 'object'){
            const usuario = await Usuarios.findByPk(payload.usuarioId,{
                attributes: { exclude: ["usuarioPassword"]}
            })
            if (!usuario){
                return  res.status(400).json({
                    message:"Usuario no existe en la db"
                })
            }
            req.usuario = usuario
        }
        
        
        next()
    } catch (error: unknown) {
        if (error instanceof Error) {
            console.log(error.message)
        }
    }
        
}
