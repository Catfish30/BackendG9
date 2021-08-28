use empresa;

select * from personal;

select count(departamento_id), departamento_id,nombre
from personal
group by departamento_id, nombre
order by departamento_id;

select 'departamento 2' as departamento, count(nombre) as total, departamento_id 
from personal where departamento_id = 2;

select count(*) Total, departamento_id from personal where supervisor_id is null 
group by departamento_id order by total desc;

-- inner join departamentos on personal.departamento_id = departamentos.id ;



-- right join personal as s on personal.supervisor_id > 0


select count(*) as Total_Empleados, d.nombre as Departamento from personal
inner join departamentos as d on  personal.departamento_id = d.id group by d.nombre order by 1 desc;


