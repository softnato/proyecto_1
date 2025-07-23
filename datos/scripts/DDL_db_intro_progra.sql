use 'proyecto_intro';

CREATE TABLE opciones_menu(
    id integer not null AUTO_INCREMENT,
    numero_opcion integer not null,
    nombre_opcion varchar(25) not null,

    constraint pk_opciones_menu primary key (id)
);

CREATE TABLE    asignaturas(
    id  integer not null AUTO_INCREMENT,
    codigo_asignatura VARCHAR(5) not null,
    nombre_asignatura VARCHAR(255) not null,

    constraint pk_asignaturas primary key(id)

);

CREATE TABLE docentes(
    id integer not null AUTO_INCREMENT,
    rut integer not null unique,
    digito_verificador char(1) not null,
    nombre_docente VARCHAR(255)not null,
    correo_docente VARCHAR(255) not null,
    direccion_docente VARCHAR(255) not null,

    constraint pk_docentes primary key (id)
);

create TABLE asignaturas_docentes(
    id integer not null AUTO_INCREMENT
    id_asignatura integer not null,
    id_docente integer not null,

    constraint pk_asignaturas_docentes primary key (id),
    constraint fk_asignaturas foreign key (id_asignatura) references asignaturas (id)
    constraint fk_docentes foreign key (id_docente) references docentes(id)
);
