
select * from alumnos where nombre like 'a%';
select * from alumnos where nombre like '%a';
select * from alumnos where nombre like '%p%';
select * from alumnos where nombre like 'a%e%';
select * from alumnos where nombre like 'angel' ;

select nombre,correo from alumnos where correo like '%hotmail%';

-- COUNT es una funcion de agregacion de sql que se usa para calculos en multiples valores 
-- realizados por un select retorna un unico valor 
select count(correo) from alumnos where correo like '%hotmail%';

-- si usamos una funcion de agregacion esta tiene que ir acompaniada de la clausila GROUP BY en los casos
-- que agreguemos una columna adicional que no tenga anda que ver con la funcion agregacion ( tambien esta having by)
select count(correo), nombre from alumnos where correo like '%hotmail%' group by nombre;

-- el ORDER BY siempre va despues del GROUP BY y del where o from
select count(nombre) total ,nombre from alumnos group by nombre order by total desc, nombre asc ; 

-- select columnas |*
-- where condicion
-- from tablas[join]
-- [group by agrupamientos]
-- [order by col asc| desc]

-- traer nombre alumno, apellido y curso, estado del curso
use calificaciones;

select alumnos.nombre as Nombre_Alumno, alumnos.apellido as Apellido_Alumno,
			cursos.nombre as Nombre_Curso, cursos.estado as Estado_Curso
from alumnos
inner join alumnos_cursos on alumnos.id = alumnos_cursos.alumno_id
inner join cursos on cursos.id = alumnos_cursos.curso_id;

select * from cursos;

-- on => donde
select count(alumno_id) as alumnos_inscritos , nombre as curso_nombre
from alumnos_cursos inner join cursos on alumnos_cursos.curso_id = cursos.id
group by nombre
order by count(alumno_id) desc, nombre asc;
-- order by 1 desc, 2 asc;




