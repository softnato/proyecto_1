alter TABLE opciones_menu add column tipo_menu integer not null;
alter TABLE opciones_menu add column habilitado TINYINT not null default 1;
alter TABLE asignaturas add column habilitado TINYINT not null default 1;
alter TABLE docentes add column habilitado TINYINT not null default 1;