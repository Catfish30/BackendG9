CREATE TYPE "tipo_usuario" AS ENUM (
  'ADMINISTRADO',
  'MOZO',
  'CLIENTE'
);

CREATE TABLE "platos" (
  "id" integer PRIMARY KEY,
  "nombre" varchar(100) NOT NULL,
  "precio" decimal(5,2) NOT NULL,
  "foto" text,
  "cantidad" integer,
  "update_at" datetime,
  "create_at" datetime
);

CREATE TABLE "usuarios" (
  "id" int PRIMARY KEY,
  "nombre" varchar(100) NOT NULL,
  "apellido" varchar(100) NOT NULL,
  "email" varchar(50),
  "tipo" tipo_usuario,
  "password" text
);

CREATE TABLE "pedidos" (
  "id" int PRIMARY KEY,
  "fecha" datetime,
  "total" decimal(5,2),
  "cliente_id" int,
  "vendedor_id" int
);

CREATE TABLE "detalles" (
  "id" int PRIMARY KEY,
  "cantidad" int,
  "sub_total" decimal(5,2),
  "plato_id" int,
  "pedido_id" int
);

ALTER TABLE "detalles" ADD FOREIGN KEY ("pedido_id") REFERENCES "pedidos" ("id");

ALTER TABLE "pedidos" ADD FOREIGN KEY ("cliente_id") REFERENCES "usuarios" ("id");

ALTER TABLE "pedidos" ADD FOREIGN KEY ("vendedor_id") REFERENCES "usuarios" ("id");

ALTER TABLE "detalles" ADD FOREIGN KEY ("plato_id") REFERENCES "platos" ("id");
