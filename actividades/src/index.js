
// const {x} = require('./config/server')
// console.log(x);

import { Server } from "./config/server";

const objServidor = new Server();
objServidor.start();
