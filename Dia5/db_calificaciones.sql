
create database calificaciones;
use calificaciones;

create table alumnos(
	id int primary key not null auto_increment,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    correo varchar(100) unique
);

create table cursos(
	id int primary key not null auto_increment,
    nombre varchar(50) not null,
    duracion int ,
    creditos int,
    estado boolean
);

create table alumnos_cursos(
	id int primary key not null auto_increment,
	alumno_id int,
    foreign key (alumno_id) references alumnos(id),
    curso_id int,
    foreign key (curso_id) references cursos(id)
);

