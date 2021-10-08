import { DataTypes } from 'sequelize'
import { conexion } from '../config/sequelize'

export const tareaModel = () => 
    conexion.define('tarea',{
        tareaId:{
            primaryKey:true,
            unique:true,
            autoIncrement:true,
            allowNull:false,
            field:'id',
            type: DataTypes.INTEGER
        },
        tareaNombre:{
            type:DataTypes.STRING(50),
            allowNull:false,
            field:'nombre',
        },
        tareaHora:{
            type:DataTypes.TIME,
            allowNull:true,
            field:'hora',
        },
        tareaDias:{
            type:DataTypes.ARRAY(DataTypes.ENUM(["LUN","MAR","MIE","JUE","VIE","SAB","DOM"])),
            allowNull:true,
            field:'dias',
        },
    },{
        tableName:'tareas',
        timestamps:true,
        updatedAt:'fecha_de_actualizacion',
    })
