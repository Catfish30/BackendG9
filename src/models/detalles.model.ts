import { DataTypes } from "sequelize";
import conexion from '../config/sequelize';

export default () => conexion.define('detalles',{
        detalleId:{
            primaryKey:true,
            type: DataTypes.UUID,
            defaultValue: DataTypes.UUIDV4,
            field:"id"
        },
        detalleCantidad: {
          type: DataTypes.INTEGER,
          allowNull: false,
          field:"cantidad",
          validate:{
              min:1,
          },
        },
        detalleTotal: {
            type: DataTypes.DECIMAL(5,2),
            allowNull: false,
            field:"total",
            validate:{
                min:0.1,
            },
        },
    },{
      tableName: 'detalles',
      timestamps:false
    })

