-- Comentario
create database prueba;
use prueba;

create table personas(
	-- Aqui se definiran las columnas de la tabla
    -- las llaves primarias siempre deben se ser unicas e irrepetibles
    -- nombre_col - tipo_dato - [primary key| not null]
    id int primary key not null auto_increment,
    documento varchar(20) unique not null,
    tipo_documento enum ('DNI','C.E','PASAPORTE'),
    nombre varchar(25),
    apellido varchar(50),
    correo varchar(100) unique,
    genero enum('Femenino','Masculino','Otro') not null,
    fecha_nacimiento date
);
-- MODIFICAR LA COLUMNA
-- alter table personas modify nombre varvhar(30) null;

insert into personas (nombre,apellido,fecha_nacimiento,genero)
values ('Michael','Fuentes','1997-07-30','Masculino');

-- visualizar columnas especificas
select nombre,apellido,fecha_nacimiento from personas;

-- visualizar todas las columnas
select * from personas;

insert into personas (nombre,apellido,fecha_nacimiento,genero)
values ('Pina',null,'2012-07-21','Femenino');
insert into personas (nombre,apellido,fecha_nacimiento,genero)
values ('Prin',null,'2002-04-30','Otro');
insert into personas (nombre,apellido,fecha_nacimiento,genero)
values ('Cavid','Ramon','2014-04-20','Masculino');

-- Filtrar por nombre and otros datos
select * from personas where nombre='Michael' and genero='Masculino';

-- eliminar registro

delete from personas where nombre='Prin';

-- actualizar registro

-- update personas set nombre = 'josefina' where id='1';





create table historias_vacunaciones(
	id int primary key not null auto_increment,
    vacuna enum('PFIZER','SINOPHARM', 'ASTRAZENECA'),
    lote varchar(10),
    fecha date,
    
    -- relaciones en una base de datos
    medico_id int ,
    -- relacion personas
    paciente_id int,
    
    foreign key (medico_id) references medicos(id),
    foreign key (paciente_id) references personas(id)
);

create table medicos(
    id int primary key not null auto_increment,
    cmp varchar(5) unique not null, -- colegio medico del peru
    nombre varchar(30),
    apellido varchar(50)
);


insert into medicos (cmp,nombre,apellido)
values				('234','Pina','LLanos'),
					('432','Prin','Lina'),
                    ('643','Cavi','Conio');
                    
select * from prueba.personas;

insert into historias_vacunaciones (vacuna, lote, medico_id, paciente_id, fecha) 
values                             ('PFIZER','1234',1, 1, '2021-07-24'),
                                   ('SINOPHARM','1598', 2, 2, '2021-08-01'),
                                   ('ASTRAZENECA','1959', 1, 3, '2021-08-24'),
                                   ('PFIZER','1234',1, 1, now()),
                                   ('SINOPHARM', '5948', 3, 2, now());


select * from historias_vacunaciones where vacuna='PFIZER' or vacuna="ASTRAZENECA";


-- set aql_safe_updates = 0












