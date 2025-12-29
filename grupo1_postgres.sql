-- PostgreSQL dump for SADES - Sistema de Seguimiento Estudiantil
-- Compatible with PostgreSQL 12+

-- Create database
CREATE DATABASE sades_db
    WITH 
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8';

-- Connect to the database
\c sades_db;

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Drop existing tables if they exist
DROP TABLE IF EXISTS reportes CASCADE;
DROP TABLE IF EXISTS intervenciones CASCADE;
DROP TABLE IF EXISTS seguimiento_riesgo CASCADE;
DROP TABLE IF EXISTS notas CASCADE;
DROP TABLE IF EXISTS evaluaciones CASCADE;
DROP TABLE IF EXISTS asistencias CASCADE;
DROP TABLE IF EXISTS inscripciones CASCADE;
DROP TABLE IF EXISTS cursos CASCADE;
DROP TABLE IF EXISTS ciclos CASCADE;
DROP TABLE IF EXISTS estudiantes CASCADE;
DROP TABLE IF EXISTS usuarios CASCADE;
DROP TABLE IF EXISTS alembic_version CASCADE;

-- Table: alembic_version
CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL PRIMARY KEY
);

-- Table: usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(64) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(128),
    rol VARCHAR(20),
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: estudiantes
CREATE TABLE estudiantes (
    id SERIAL PRIMARY KEY,
    codigo_estudiante VARCHAR(20) NOT NULL UNIQUE,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    telefono VARCHAR(15),
    fecha_inscripcion DATE,
    activo BOOLEAN DEFAULT TRUE
);

-- Table: ciclos
CREATE TABLE ciclos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    codigo_ciclo VARCHAR(20) NOT NULL UNIQUE,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    activo BOOLEAN DEFAULT TRUE
);

-- Table: cursos
CREATE TABLE cursos (
    id SERIAL PRIMARY KEY,
    codigo_curso VARCHAR(20) NOT NULL UNIQUE,
    nombre_curso VARCHAR(100) NOT NULL,
    creditos INTEGER,
    semestre VARCHAR(10) NOT NULL,
    ciclo_id INTEGER NOT NULL REFERENCES ciclos(id),
    activo BOOLEAN DEFAULT TRUE
);

-- Table: inscripciones
CREATE TABLE inscripciones (
    id SERIAL PRIMARY KEY,
    estudiante_id INTEGER NOT NULL REFERENCES estudiantes(id),
    curso_id INTEGER NOT NULL REFERENCES cursos(id),
    fecha_inscripcion DATE,
    estado VARCHAR(20)
);

-- Table: evaluaciones
CREATE TABLE evaluaciones (
    id SERIAL PRIMARY KEY,
    curso_id INTEGER NOT NULL REFERENCES cursos(id),
    nombre_evaluacion VARCHAR(100) NOT NULL,
    tipo_evaluacion VARCHAR(50),
    peso NUMERIC(5,2),
    fecha_creacion DATE
);

-- Table: notas
CREATE TABLE notas (
    id SERIAL PRIMARY KEY,
    inscripcion_id INTEGER NOT NULL REFERENCES inscripciones(id),
    evaluacion_id INTEGER NOT NULL REFERENCES evaluaciones(id),
    nota NUMERIC(5,2),
    fecha_registro DATE,
    observaciones TEXT
);

-- Table: asistencias
CREATE TABLE asistencias (
    id SERIAL PRIMARY KEY,
    inscripcion_id INTEGER NOT NULL REFERENCES inscripciones(id),
    fecha DATE NOT NULL,
    presente BOOLEAN,
    justificado BOOLEAN,
    observaciones TEXT
);

-- Table: seguimiento_riesgo
CREATE TABLE seguimiento_riesgo (
    id SERIAL PRIMARY KEY,
    estudiante_id INTEGER NOT NULL REFERENCES estudiantes(id),
    semestre VARCHAR(10) NOT NULL,
    categoria_riesgo VARCHAR(20),
    puntaje_riesgo NUMERIC(5,2),
    fecha_evaluacion DATE,
    factores_riesgo JSONB,
    observaciones TEXT
);

-- Table: intervenciones
CREATE TABLE intervenciones (
    id SERIAL PRIMARY KEY,
    estudiante_id INTEGER NOT NULL REFERENCES estudiantes(id),
    tipo_intervencion VARCHAR(50),
    descripcion TEXT NOT NULL,
    fecha_intervencion DATE,
    responsable VARCHAR(100),
    estado VARCHAR(20),
    resultado TEXT
);

-- Table: reportes
CREATE TABLE reportes (
    id SERIAL PRIMARY KEY,
    tipo_reporte VARCHAR(50) NOT NULL,
    titulo VARCHAR(200) NOT NULL,
    descripcion TEXT,
    parametros JSONB,
    contenido TEXT,
    usuario_id INTEGER NOT NULL REFERENCES usuarios(id),
    fecha_generacion TIMESTAMP,
    archivo_path VARCHAR(500)
);

-- Create indexes for better performance
CREATE INDEX idx_estudiantes_codigo ON estudiantes(codigo_estudiante);
CREATE INDEX idx_estudiantes_email ON estudiantes(email);
CREATE INDEX idx_cursos_codigo ON cursos(codigo_curso);
CREATE INDEX idx_cursos_ciclo ON cursos(ciclo_id);
CREATE INDEX idx_inscripciones_estudiante ON inscripciones(estudiante_id);
CREATE INDEX idx_inscripciones_curso ON inscripciones(curso_id);
CREATE INDEX idx_notas_inscripcion ON notas(inscripcion_id);
CREATE INDEX idx_notas_evaluacion ON notas(evaluacion_id);
CREATE INDEX idx_asistencias_inscripcion ON asistencias(inscripcion_id);
CREATE INDEX idx_seguimiento_estudiante ON seguimiento_riesgo(estudiante_id);
CREATE INDEX idx_seguimiento_semestre ON seguimiento_riesgo(semestre);
CREATE INDEX idx_intervenciones_estudiante ON intervenciones(estudiante_id);
CREATE INDEX idx_reportes_usuario ON reportes(usuario_id);

-- Insert alembic version
INSERT INTO alembic_version VALUES ('9aad651090f7');

-- Insert usuarios
INSERT INTO usuarios (username, email, password_hash, rol, activo, fecha_creacion) VALUES
('admin', 'admin@sades.edu', 'pbkdf2:sha256:600000$Uf9TbYyF4oTV08mN$e629206c6f9d8b4800e4d2cd952c3f40902ca6a2f1f6b8fb2dc5b9b702b5ee5c', 'administrador', TRUE, '2025-11-11 13:21:40'),
('coordinador', 'coordinador@sades.edu', 'pbkdf2:sha256:600000$PM8SucBzNdmh2xuY$d37bf3998cbb7bd9aa09f9247ae38479cd5495864642d425ddfb24dcf132b5b6', 'coordinador', TRUE, '2025-11-11 13:21:40'),
('docente', 'docente@sades.edu', 'pbkdf2:sha256:600000$EDfOFijKZU1rUUEE$3f0253c4875fc407f6cc2714d0f5469b1e58fe9b37aa0a14f40f649d4f5b4583', 'docente', TRUE, '2025-11-11 13:21:40');

-- Insert ciclos
INSERT INTO ciclos (nombre, codigo_ciclo, fecha_inicio, fecha_fin, activo) VALUES
(1, 'DSI-2025-1', '2025-1', '2025-04-08', '2025-08-12', TRUE),
(2, 'DSI-2025-2', '2025-2', '2025-08-18', '2025-12-20', TRUE),
(3, 'DSI-2026-1', '2026-1', '2026-04-08', '2026-08-12', TRUE),
(4, 'DSI-2026-2', '2026-2', '2026-08-18', '2026-12-20', TRUE),
(5, 'DSI-2027-1', '2027-1', '2027-04-08', '2027-08-12', TRUE),
(6, 'DSI-2027-2', '2027-2', '2027-08-18', '2027-12-20', TRUE),
(7, 'DSI-2028-1', '2028-1', '2028-04-08', '2028-08-12', TRUE),
(8, 'DSI-2028-2', '2028-2', '2028-08-18', '2028-12-20', TRUE);

-- Insert estudiantes
INSERT INTO estudiantes (codigo_estudiante, nombres, apellidos, email, telefono, fecha_inscripcion, activo) VALUES
('77415003', 'Jhuel Alejandro', 'Barbaran Gonzales', 'Jhuelbarbaran9@gmail.com', '903168619', '2025-11-11', TRUE),
('73546984', 'Brayan Piero', 'Bartra Montalvo', 'ppierobartra@gmail.com', '972329017', '2025-11-11', TRUE),
('61265730', 'Pool Angelo', 'Carranza Pereyra', 'poolangelocarranzapereyra@gmail.com', '922899339', '2025-11-11', TRUE),
('74191818', 'Leysglin Riquelmer', 'Fachin Rojas', 'riquelmerrojas@gmail.com', '951957617', '2025-11-11', TRUE),
('61122710', 'Sandy Margarita', 'Garcia Gongora', 'sandygraciasgongora@gmail.com', '974636828', '2025-11-11', TRUE),
('76029422', 'Jhonatan Nijar', 'Gonzales De Souza', 'jhonatannijargonzalesdesouza@gmail.com', '961853888', '2025-11-11', TRUE),
('63123442', 'Isai', 'Huaman Salas', 'isaihuamansalas@gmail.com', '963123442', '2025-11-11', TRUE),
('61122419', 'Jhonatan Smith', 'Kong Novoa', 'jhonatan.smith10820@gmail.com', '922514228', '2025-11-11', TRUE),
('61201824', 'Benjamin', 'Mamani Chino', 'chino31benjamin@gmail.com', '935486964', '2025-11-11', TRUE),
('71238372', 'Mayra Tahina', 'Oliveira Huayta', 'mayratahinaoliveirahuayta19@gmail.com', '958687401', '2025-11-11', TRUE),
('73885601', 'Carlos Alexis', 'Perea Saldaña', 'caps6954@gmail.com', '912849419', '2025-11-11', TRUE),
('72122196', 'Luis Elmer', 'Ramirez Castilla', 'zlkarozr3@gmail.com', '986085391', '2025-11-11', TRUE),
('70710170', 'Piero Alexandro', 'Rojas Diaz', 'rojasdiazpiero@gmail.com', '912078239', '2025-11-11', TRUE),
('61006146', 'Geric Aldair', 'Salas Ormeño', 'cuageri10@gmail.com', '962002254', '2025-11-11', TRUE),
('61088684', 'Noemi', 'Sanchez Cumapa', 'nohemysan84@gmail.com', '940348776', '2025-11-11', TRUE),
('61237674', 'Valerys Brillyth', 'Sandi Nunta', 'sandinuntav@gmail.com', '948933998', '2025-11-11', TRUE),
('74799549', 'segundo geiner', 'tange Hidalgo', 'geinertange25@gmail.com', '922643482', '2025-11-11', TRUE),
('60014134', 'clider', 'Urquia Lopez', 'cliderlex@gmail.com', '913826706', '2025-11-11', TRUE),
('60818621', 'Tania Lorena', 'Tapullima Navarro', 'Tanialorenatapullimanavarro@gmail.com', '972885623', '2025-11-11', TRUE),
('74370827', 'Angel Jesus', 'Vasquez Godoy', 'vasquezgodoyangeljesus@gmail.com', '912785092', '2025-11-11', TRUE);

-- Insert cursos
INSERT INTO cursos (codigo_curso, nombre_curso, creditos, semestre, ciclo_id, activo) VALUES
('MAT101', 'diseño grafico', 4, '2025-1', 1, TRUE),
('PROG102', 'Programación Python', 3, '2025-1', 1, TRUE),
('DSI-I-AE', 'Aplicaciones Empresariales', 2, 'I', 3, TRUE),
('DSI-I-ACIT', 'Arquitectura de computadoras e integracion de TIC', 3, 'I', 3, TRUE),
('DSI-I-CO', 'Comunicacion Oral', 2, 'I', 3, TRUE),
('DSI-I-FP', 'Fundamentos de programacion', 3, 'I', 3, TRUE),
('DSI-I-LP', 'Lenguaje de programacion', 3, 'I', 3, TRUE),
('DSI-I-O', 'Ofimatica', 2, 'I', 3, TRUE),
('DSI-I-RCC', 'Redes y conectividad de computadoras', 3, 'I', 3, TRUE),
('DSI-II-ADS', 'Analisis y diseño de sistemas', 2, 'II', 4, TRUE),
('DSI-II-HPD', 'Herramientas de programacion distribuida', 4, 'II', 4, TRUE),
('DSI-II-HPC', 'Herramientas de programacion concurrente', 4, 'II', 4, TRUE),
('DSI-II-ARS', 'Administracion de redes y servidores', 3, 'II', 4, TRUE),
('DSI-II-LP', 'Logica de programacion', 2, 'II', 4, TRUE),
('DSI-II-IPT', 'Interpretacion y produccion de textos ', 2, 'II', 4, TRUE),
('DSI-II-AI', 'Aplicaciones en Internet', 2, 'II', 4, TRUE),
('DSI-II-EFSRT', 'Experiencias formativas en situaciones reales de trabajo 2', 4, 'II', 4, TRUE),
('DSI-III-ABD', 'Arquitectura de base de datos', 2, 'III', 5, TRUE),
('DSI-III-PD', 'Programacion Distribuida', 4, 'III', 5, TRUE),
('DSI-III-PC', 'Programacion Concurrente', 4, 'III', 5, TRUE),
('DSI-III-POO', 'Programacion orientada a objetos', 4, 'III', 5, TRUE),
('DSI-III-MS', 'Modelamiento de software', 2, 'III', 5, TRUE),
('DSI-III-ICO', 'Ingles para la comunicacion oral', 2, 'III', 5, TRUE),
('DSI-III-IT', 'Innovacion Tecnologica', 2, 'III', 5, TRUE),
('DSI-IV-TBD', 'Taller de base de datos ', 4, 'IV', 6, TRUE),
('DSI-IV-TS', 'Taller se software', 4, 'IV', 6, TRUE),
('DSI-IV-SI', 'Seguridad Informatica', 4, 'IV', 6, TRUE),
('DSI-IV-DG', 'Diseño grafico', 4, 'IV', 6, TRUE),
('DSI-IV-CRI', 'Comprension y redaccion en ingles', 2, 'IV', 6, TRUE),
('DSI-IV-CA', 'Cultura ambiental', 2, 'IV', 6, TRUE),
('DSI-IV-EFSRT', 'Experiencias formativas en situaciones reales de trabajo 4', 4, 'IV', 6, TRUE),
('DSI-V-GAW', 'Gestion y administracion web', 3, 'V', 7, TRUE),
('DSI-V-AG', 'Animacion grafica ', 4, 'V', 7, TRUE),
('DSI-V-DW', 'Diseño Web', 4, 'V', 7, TRUE),
('DSI-V-DAM', 'Diseño de Aplicaciones moviles', 4, 'V', 7, TRUE),
('DSI-V-CE', 'Comportamiento Etico', 3, 'V', 7, TRUE),
('DSI-V-EFSRT', 'Experiencias formativas en situaciones reales de trabajo 5', 4, 'V', 7, TRUE),
('DSI-VI-TPW', 'Taller de Programacion Web', 5, 'VI', 8, TRUE),
('DSI-VI-TAM', 'Taller de Aplicaciones Móviles', 4, 'VI', 8, TRUE),
('DSI-VI-IN', 'Inteligencia de Negocios', 3, 'VI', 8, TRUE),
('DSI-VI-HM', 'Herramientas Multimedia', 3, 'VI', 8, TRUE),
('DSI-VI-SP', 'Solución de problemas', 2, 'VI', 8, TRUE),
('DSI-VI-ON', 'Oportunidades de negocios', 2, 'VI', 8, TRUE),
('DSI-VI-EFSRT', 'Experiencias formativas en situaciones reales de trabajo 6', 4, 'VI', 8, TRUE),
('DSI-I-EFSRT', 'Experiencias formativas en situaciones reales de trabajo 1 ', 4, 'I', 3, TRUE),
('DSI-III-EFSRT', 'Experiencias formativas en situaciones reales de trabajo 3 ', 4, 'III', 5, TRUE);

-- Insert inscripciones
INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES
(1, 1, '2025-12-27', 'ACTIVO'),
(1, 2, '2025-12-27', 'ACTIVO'),
(2, 1, '2025-12-27', 'ACTIVO'),
(2, 2, '2025-12-27', 'ACTIVO'),
(3, 1, '2025-12-27', 'ACTIVO'),
(3, 2, '2025-12-27', 'ACTIVO'),
(4, 1, '2025-12-27', 'ACTIVO'),
(4, 2, '2025-12-27', 'ACTIVO'),
(5, 1, '2025-12-27', 'ACTIVO'),
(5, 2, '2025-12-27', 'ACTIVO'),
(6, 1, '2025-12-27', 'ACTIVO'),
(6, 2, '2025-12-27', 'ACTIVO'),
(7, 1, '2025-12-27', 'ACTIVO'),
(7, 2, '2025-12-27', 'ACTIVO'),
(8, 1, '2025-12-27', 'ACTIVO'),
(8, 2, '2025-12-27', 'ACTIVO'),
(9, 1, '2025-12-27', 'ACTIVO'),
(9, 2, '2025-12-27', 'ACTIVO'),
(10, 1, '2025-12-27', 'ACTIVO'),
(10, 2, '2025-12-27', 'ACTIVO'),
(11, 1, '2025-12-27', 'ACTIVO'),
(11, 2, '2025-12-27', 'ACTIVO'),
(12, 1, '2025-12-27', 'ACTIVO'),
(12, 2, '2025-12-27', 'ACTIVO'),
(13, 1, '2025-12-27', 'ACTIVO'),
(13, 2, '2025-12-27', 'ACTIVO'),
(14, 1, '2025-12-27', 'ACTIVO'),
(14, 2, '2025-12-27', 'ACTIVO'),
(15, 1, '2025-12-27', 'ACTIVO'),
(15, 2, '2025-12-27', 'ACTIVO'),
(16, 1, '2025-12-27', 'ACTIVO'),
(16, 2, '2025-12-27', 'ACTIVO'),
(17, 1, '2025-12-27', 'ACTIVO'),
(17, 2, '2025-12-27', 'ACTIVO'),
(18, 1, '2025-12-27', 'ACTIVO'),
(18, 2, '2025-12-27', 'ACTIVO'),
(19, 1, '2025-12-27', 'ACTIVO'),
(19, 2, '2025-12-27', 'ACTIVO'),
(20, 1, '2025-12-27', 'ACTIVO'),
(20, 2, '2025-12-27', 'ACTIVO');

-- Insert evaluaciones
INSERT INTO evaluaciones (curso_id, nombre_evaluacion, tipo_evaluacion, peso, fecha_creacion) VALUES
(1, 'PC1', 'Parcial', 25.00, '2025-12-27'),
(1, 'PC2', 'Parcial', 25.00, '2025-12-27'),
(1, 'EX1', 'Examen', 25.00, '2025-12-27'),
(1, 'EX2', 'Examen', 25.00, '2025-12-27'),
(2, 'PC1', 'Parcial', 25.00, '2025-12-27'),
(2, 'PC2', 'Parcial', 25.00, '2025-12-27'),
(2, 'EX1', 'Examen', 25.00, '2025-12-27'),
(2, 'EX2', 'Examen', 25.00, '2025-12-27');

-- Insert intervenciones
INSERT INTO intervenciones (estudiante_id, tipo_intervencion, descripcion, fecha_intervencion, responsable, estado, resultado) VALUES
(1, 'Tutoría Académica', 'Intervención preventiva por bajo rendimiento', '2025-12-27', 'Coordinación Académica', 'PENDIENTE', NULL),
(2, 'Tutoría Académica', 'Intervención preventiva por bajo rendimiento', '2025-12-27', 'Coordinación Académica', 'PENDIENTE', NULL),
(3, 'Tutoría Académica', 'Intervención preventiva por bajo rendimiento', '2025-12-27', 'Coordinación Académica', 'PENDIENTE', NULL),
(4, 'Tutoría Académica', 'Intervención preventiva por bajo rendimiento', '2025-12-27', 'Coordinación Académica', 'PENDIENTE', NULL),
(5, 'Tutoría Académica', 'Intervención preventiva por bajo rendimiento', '2025-12-27', 'Coordinación Académica', 'PENDIENTE', NULL);

-- Insert seguimiento_riesgo
INSERT INTO seguimiento_riesgo (estudiante_id, semestre, categoria_riesgo, puntaje_riesgo, fecha_evaluacion, factores_riesgo, observaciones) VALUES
(1, '2025-1', 'ALERTA_ROJA', 0.81, '2025-12-26', '[{"peso": 0.5, "valor": 0.9, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 8.9 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.45}, {"peso": 0.3, "valor": 0.6, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 72.5% (29/40 clases)", "contribucion": 0.18}, {"peso": 0.2, "valor": 0.9, "nombre": "Distribución de Riesgo", "descripcion": "2.0 de 2 cursos requieren atención", "contribucion": 0.18}]', NULL),
(2, '2025-1', 'SIN_RIESGO', 0.45, '2025-12-26', '[{"peso": 0.5, "valor": 0.3, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 12.9 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.15}, {"peso": 0.3, "valor": 0.6, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 70.0% (28/40 clases)", "contribucion": 0.18}, {"peso": 0.2, "valor": 0.6, "nombre": "Distribución de Riesgo", "descripcion": "1.0 de 2 cursos requieren atención", "contribucion": 0.12}]', NULL),
(3, '2025-1', 'SIN_RIESGO', 0.36, '2025-12-26', '[{"peso": 0.5, "valor": 0.3, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 13.6 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.15}, {"peso": 0.3, "valor": 0.3, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 82.5% (33/40 clases)", "contribucion": 0.09}, {"peso": 0.2, "valor": 0.6, "nombre": "Distribución de Riesgo", "descripcion": "1.0 de 2 cursos requieren atención", "contribucion": 0.12}]', NULL),
(4, '2025-1', 'SIN_RIESGO', 0.45, '2025-12-26', '[{"peso": 0.5, "valor": 0.3, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 12.7 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.15}, {"peso": 0.3, "valor": 0.6, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 70.0% (28/40 clases)", "contribucion": 0.18}, {"peso": 0.2, "valor": 0.6, "nombre": "Distribución de Riesgo", "descripcion": "1.0 de 2 cursos requieren atención", "contribucion": 0.12}]', NULL),
(5, '2025-1', 'ALERTA_AMARILLA', 0.57, '2025-12-26', '[{"peso": 0.5, "valor": 0.6, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 11.7 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.3}, {"peso": 0.3, "valor": 0.3, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 75.0% (30/40 clases)", "contribucion": 0.09}, {"peso": 0.2, "valor": 0.9, "nombre": "Distribución de Riesgo", "descripcion": "2.0 de 2 cursos requieren atención", "contribucion": 0.18}]', NULL),
(6, '2025-1', 'SIN_RIESGO', 0.20, '2025-12-26', '[{"peso": 0.5, "valor": 0.3, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 13.4 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.15}, {"peso": 0.3, "valor": 0.1, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 85.0% (34/40 clases)", "contribucion": 0.03}, {"peso": 0.2, "valor": 0.1, "nombre": "Distribución de Riesgo", "descripcion": "0.0 de 2 cursos requieren atención", "contribucion": 0.02}]', NULL),
(7, '2025-1', 'SIN_RIESGO', 0.36, '2025-12-26', '[{"peso": 0.5, "valor": 0.3, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 12.8 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.15}, {"peso": 0.3, "valor": 0.3, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 77.5% (31/40 clases)", "contribucion": 0.09}, {"peso": 0.2, "valor": 0.6, "nombre": "Distribución de Riesgo", "descripcion": "1.0 de 2 cursos requieren atención", "contribucion": 0.12}]', NULL),
(8, '2025-1', 'ALERTA_ROJA', 0.72, '2025-12-26', '[{"peso": 0.5, "valor": 0.9, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 9.5 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.45}, {"peso": 0.3, "valor": 0.3, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 82.5% (33/40 clases)", "contribucion": 0.09}, {"peso": 0.2, "valor": 0.9, "nombre": "Distribución de Riesgo", "descripcion": "2.0 de 2 cursos requieren atención", "contribucion": 0.18}]', NULL),
(9, '2025-1', 'ALERTA_AMARILLA', 0.60, '2025-12-26', '[{"peso": 0.5, "valor": 0.6, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 11.3 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.3}, {"peso": 0.3, "valor": 0.6, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 72.5% (29/40 clases)", "contribucion": 0.18}, {"peso": 0.2, "valor": 0.6, "nombre": "Distribución de Riesgo", "descripcion": "1.0 de 2 cursos requieren atención", "contribucion": 0.12}]', NULL),
(10, '2025-1', 'ALERTA_AMARILLA', 0.60, '2025-12-26', '[{"peso": 0.5, "valor": 0.6, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 11.2 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.3}, {"peso": 0.3, "valor": 0.6, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 70.0% (28/40 clases)", "contribucion": 0.18}, {"peso": 0.2, "valor": 0.6, "nombre": "Distribución de Riesgo", "descripcion": "1.0 de 2 cursos requieren atención", "contribucion": 0.12}]', NULL),
(11, '2025-1', 'SIN_RIESGO', 0.35, '2025-12-26', '[{"peso": 0.5, "valor": 0.3, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 13.8 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.15}, {"peso": 0.3, "valor": 0.6, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 70.0% (28/40 clases)", "contribucion": 0.18}, {"peso": 0.2, "valor": 0.1, "nombre": "Distribución de Riesgo", "descripcion": "0.0 de 2 cursos requieren atención", "contribucion": 0.02}]', NULL),
(12, '2025-1', 'SIN_RIESGO', 0.35, '2025-12-26', '[{"peso": 0.5, "valor": 0.3, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 12.9 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.15}, {"peso": 0.3, "valor": 0.6, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 72.5% (29/40 clases)", "contribucion": 0.18}, {"peso": 0.2, "valor": 0.1, "nombre": "Distribución de Riesgo", "descripcion": "0.0 de 2 cursos requieren atención", "contribucion": 0.02}]', NULL),
(13, '2025-1', 'SIN_RIESGO', 0.45, '2025-12-26', '[{"peso": 0.5, "valor": 0.6, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 10.8 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.3}, {"peso": 0.3, "valor": 0.1, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 85.0% (34/40 clases)", "contribucion": 0.03}, {"peso": 0.2, "valor": 0.6, "nombre": "Distribución de Riesgo", "descripcion": "1.0 de 2 cursos requieren atención", "contribucion": 0.12}]', NULL),
(14, '2025-1', 'ALERTA_AMARILLA', 0.57, '2025-12-26', '[{"peso": 0.5, "valor": 0.6, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 11.1 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.3}, {"peso": 0.3, "valor": 0.3, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 77.5% (31/40 clases)", "contribucion": 0.09}, {"peso": 0.2, "valor": 0.9, "nombre": "Distribución de Riesgo", "descripcion": "2.0 de 2 cursos requieren atención", "contribucion": 0.18}]', NULL),
(15, '2025-1', 'SIN_RIESGO', 0.35, '2025-12-26', '[{"peso": 0.5, "valor": 0.3, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 13.2 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.15}, {"peso": 0.3, "valor": 0.6, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 67.5% (27/40 clases)", "contribucion": 0.18}, {"peso": 0.2, "valor": 0.1, "nombre": "Distribución de Riesgo", "descripcion": "0.0 de 2 cursos requieren atención", "contribucion": 0.02}]', NULL),
(16, '2025-1', 'SIN_RIESGO', 0.36, '2025-12-26', '[{"peso": 0.5, "valor": 0.3, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 12.3 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.15}, {"peso": 0.3, "valor": 0.3, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 75.0% (30/40 clases)", "contribucion": 0.09}, {"peso": 0.2, "valor": 0.6, "nombre": "Distribución de Riesgo", "descripcion": "1.0 de 2 cursos requieren atención", "contribucion": 0.12}]', NULL),
(17, '2025-1', 'ALERTA_AMARILLA', 0.54, '2025-12-26', '[{"peso": 0.5, "valor": 0.3, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 12.8 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.15}, {"peso": 0.3, "valor": 0.9, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 60.0% (24/40 clases)", "contribucion": 0.27}, {"peso": 0.2, "valor": 0.6, "nombre": "Distribución de Riesgo", "descripcion": "1.0 de 2 cursos requieren atención", "contribucion": 0.12}]', NULL),
(18, '2025-1', 'SIN_RIESGO', 0.45, '2025-12-26', '[{"peso": 0.5, "valor": 0.3, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 12.2 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.15}, {"peso": 0.3, "valor": 0.6, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 70.0% (28/40 clases)", "contribucion": 0.18}, {"peso": 0.2, "valor": 0.6, "nombre": "Distribución de Riesgo", "descripcion": "1.0 de 2 cursos requieren atención", "contribucion": 0.12}]', NULL),
(19, '2025-1', 'SIN_RIESGO', 0.16, '2025-12-26', '[{"peso": 0.5, "valor": 0.1, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 14.8 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.05}, {"peso": 0.3, "valor": 0.3, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 75.0% (30/40 clases)", "contribucion": 0.09}, {"peso": 0.2, "valor": 0.1, "nombre": "Distribución de Riesgo", "descripcion": "0.0 de 2 cursos requieren atención", "contribucion": 0.02}]', NULL),
(20, '2025-1', 'SIN_RIESGO', 0.36, '2025-12-26', '[{"peso": 0.5, "valor": 0.3, "nombre": "Rendimiento Actual", "descripcion": "Promedio: 12.2 | 8 evaluaciones | Completitud: 100%", "contribucion": 0.15}, {"peso": 0.3, "valor": 0.3, "nombre": "Asistencia Actual", "descripcion": "Asistencia: 75.0% (30/40 clases)", "contribucion": 0.09}, {"peso": 0.2, "valor": 0.6, "nombre": "Distribución de Riesgo", "descripcion": "1.0 de 2 cursos requieren atención", "contribucion": 0.12}]', NULL);
