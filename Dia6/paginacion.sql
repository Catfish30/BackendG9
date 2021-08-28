
-- funciones de agregacion
-- promedio avg(column)
-- maximo max(column)
-- minimo min(column)
-- contar count(column)
-- sumar sum(column)
-- primero first(column)
-- ultimo last(column)

use emrpesa;
--  LIMIT 7 =>trae solo los 7 primeros datp OFFSET 30 => salta los datos hasta el 30 y devuelve 7
select * from personal limit 7 offset 30;

-- select columnas |*
-- from tablas[join]
-- where condicion
-- [group by agrupamientos]
-- [order by col asc| desc]
-- limit 0
-- offset 0