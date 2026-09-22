# Proyecto Git - BiblioStock CLI (Biblioteca Horizonte)

Este repositorio contiene el sistema de inventario y préstamos "BiblioStock CLI" desarrollado en Python para la Biblioteca Comunitaria Horizonte. El objetivo principal de este proyecto es evidenciar el dominio y la aplicación de un flujo de trabajo colaborativo utilizando Git y GitHub.

## Integrantes del Equipo y Roles

* *Juan José Ardila:* Integrador de Repositorio (Creación del repo, .gitignore, estructura base, aprobación de PRs y resolución de conflictos).
* *Miguel Ricardo Calderon:* Desarrollador (Gestión de inventario y corrección de errores en la persistencia JSON).
* *Diego Gomez:* Desarrollador (Gestión de préstamos, devoluciones y documentación).

---

## Enlace al Repositorio
[https://github.com/JuanJArdilaA/Proyecto_Git](https://github.com/JuanJArdilaA/Proyecto_Git)

---

## Comandos de Git Utilizados

Durante el desarrollo del proyecto, el equipo utilizó los siguientes comandos para mantener un control de versiones ordenado:

* *Configuración e Inicialización:*
  * git config --global user.name / user.email: Para vincular los commits a nuestras cuentas.
  * git init: Para inicializar el repositorio local.
  * git clone <url>: Utilizado por Miguel y Diego para descargar el repositorio a sus equipos locales.
* *Gestión de Cambios (Commits):*
  * git add .: Para preparar los archivos modificados (staging area).
  * git commit -m "mensaje": Para registrar los cambios. Utilizamos Conventional Commits (feat:, chore:, fix:, docs:) para mantener un historial claro.
* *Gestión de Ramas (Branches):*
  * git checkout -b <nombre-rama>: Para crear y movernos a ramas de trabajo independientes (feature/, fix/, docs/*).
  * git checkout main: Para regresar a la rama principal.
* *Sincronización con Remoto (GitHub):*
  * git push origin <rama>: Para subir nuestras ramas y cambios al repositorio remoto.
  * git pull origin main: Para actualizar nuestros repositorios locales con los últimos cambios aprobados en la rama principal.

---

## Flujo de Ramas (Git Flow)
El proyecto se dividió en las siguientes ramas, integradas mediante Pull Requests:
1. main: Rama principal, siempre estable.
2. feature/menu-principal: Estructura inicial (Juan).
3. feature/registro-inventario: Lógica de ítems y JSON (Miguel).
4. feature/prestamos: Lógica de préstamos y devoluciones (Diego).
5. fix/error-json-vacio: Parche para evitar caídas si el archivo no existe (Miguel).
6. docs/readme-final: Documentación y evidencias (Diego).

---

## Resolución del Conflicto de Merge

Durante la integración de la rama feature/prestamos, se generó un conflicto de merge real. 
* Causas: El integrador (Juan) realizó un cambio directo en la línea del título del menú en la rama main al mismo tiempo que Diego modificaba esa misma línea en su rama local desactualizada.
* Solución: Al intentar hacer el Pull Request, GitHub detectó el conflicto. El integrador abrió el editor web de GitHub, analizó las diferencias entre <<<<<<< HEAD y >>>>>>>, eliminó los marcadores de Git y unificó el título a una versión final consensuada. Posteriormente, se realizó el Commit merge.

(Evidencia de la resolución del conflicto):
https://drive.google.com/file/d/1dToIquQp_p_HSQpPYn6_mSJWnhTWawJZ/view?usp=drive_link
https://drive.google.com/file/d/167m_-oiKT4QUyMo-RKK8UaOunPvB5tC7/view?usp=drive_link
---

## Evidencias Fotográficas

A continuación, se presentan las capturas de pantalla de los momentos clave del flujo de trabajo:

1. Creación del repositorio y primer Commit:
https://drive.google.com/file/d/1NEEq0y69gwpdHi7gcS5mpTt6DXQjJ4j2/view?usp=drive_link

2. Sincronización (Push y Pull):
https://drive.google.com/file/d/1Q2m35CL-ylx7EoVkj_3sUP5TiVTBZrxJ/view?usp=drive_link

3. Creación y Aprobación de un Pull Request (Merge):
https://drive.google.com/file/d/1PBLuJQrGqicwWJQEGqn8UxvS-TtWVLxb/view?usp=drive_link

4. Historial de Commits (Git Graph):
https://drive.google.com/file/d/1VSHT1tOSKorg3NMW0KUUg9M3y_QrIyKx/view?usp=sharing

---
Proyecto desarrollado para la evaluación de Control de Versiones con Git y GitHub.