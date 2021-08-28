
use empresa;

select * from personal where nombre='Kevin';

select * from personal where departamento_id=2;

select * from personal inner join departamentos on personal.departamento_id = departamentos.id where departamento_id=2;

select personal.nombre as nombre_personal,
		personal.apellido as apellido_personal,
		departamentos.nombre as nombre_departamento 
	from personal inner join departamentos 
		on personal.departamento_id = departamentos.id 
	where departamento_id=2;
    
select p.nombre as nombre_personal,
		p.apellido as apellido_personal,
		d.nombre as nombre_departamento 
	from personal as p inner join departamentos as d
		on p.departamento_id = d.id 
	where departamento_id=2;
    
select p.nombre as nombre_empleado,
	   p.apellido as apellido_empleado,
       s.nombre as nombre_supervisor,
       s.apellido as apellido_supervisor,
       d.nombre as nombre_departamento
from personal  as p left join personal as s
	on p.supervisor_id = s.id
    inner join departamentos as d 
    on p.departamento_id = d.id



    
