import {Sequelize} from 'sequelize'
require("dotenv").config()

export const conexion = new Sequelize(process.env.DATABASE_URL,{ logging: false } );