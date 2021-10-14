import { DataTypes } from "sequelize/types";
import conexion from '../config/sequelize'

enum TipoUsuario {
    ADMIN='ADMIN',
    CLIENTE='CLIENTE'
}

export default () => conexion.define(
    'usuario',{
        usuarioId:{
            type: DataTypes.UUID,
            primaryKey: true,
            defaultValue: DataTypes.UUIDV4,
            field: "id"
        },
        usuarioNombre:{
            type: DataTypes.STRING(40),
            field: 'nombre',
            allowNull:false,
        },
        usuarioCorreo:{
            type: DataTypes.STRING(50),
            field: 'correo',
            validate:{
                isEmail: true
            },
            allowNull:false,
            unique:true
        },
        usuarioPassword: {
            type: DataTypes.TEXT,
            field:'password'
        },
        usuarioTipo: {
            type: DataTypes.ENUM(TipoUsuario.ADMIN,TipoUsuario.CLIENTE),
            field: 'tipo',
            defaultValue: TipoUsuario.CLIENTE,
        },
        usuarioFoto: {
            type: DataTypes.TEXT,
            field: 'foto'
        }
    },{
        tableName:"usuarios",
        timestamps: false,
    }
) 