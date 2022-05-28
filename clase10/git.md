# Git

Git es un **software de control de versiones** diseñado por Linus Torvalds, pensando en la eficiencia, la confiabilidad y compatibilidad del mantenimiento de versiones de aplicaciones cuando estas tienen un gran número de archivos de código fuente.  
Su propósito es _llevar registro de los cambios en archivos de computadora_ incluyendo _coordinar el trabajo que varias personas realizan sobre archivos compartidos_ en un repositorio de código. 

**Recursos importantes**
- [Hoja de referencia para GIT](https://training.github.com/downloads/es_ES/github-git-cheat-sheet.pdf)
- [Una referencia visual de Git](https://marklodato.github.io/visual-git-guide/index-es.html)
- [Aprende GIT ahora! curso completo GRATIS desde cero](https://www.youtube.com/watch?v=VdGzPZ31ts8)

## Instalar GIT
Descarga la aplicación para la gestión de versiones desde la [página oficial](https://git-scm.com)

Para verificar si quedó bien instalado el git en el sistema, abriremos un terminal (o símbolo del sistema CMD) y usamos el comando:
```powershell
git --version
```
**Nota (solo para windows)**: Si no funciona, probablemente no habilitaste la integración de Git con los terminales del equipo. Vuelve a lanzar el instalador y verifica que en el paso de integración elegiremos la opción de integrar con CMD o PowerShell.

## Configuración inicial
- Establece el nombre que desea esté anexado a sus transacciones
de commit
```powershell
git config --global user.name "[name]"
```

- Establece el e-mail que desea esté anexado a sus transacciones de commit
```powershell
git config --global user.email "[email address]"
```

- Habilita la opción de ver a color algunos comandos en la línea de comando (opcional)
```powershell
git config --global color.ui auto
```

- Consulta la configuración realizada de manera global
```powershell
git config --global --list
```

- Elimina el valor de una variable mal ingresada
```powershell
git config --global --unset [variable]
```

# GitHub

GitHub es una **plataforma de desarrollo colaborativo** para alojar proyectos utilizando el _sistema de control de versiones_ Git en la nube.  
Se utiliza principalmente para la creación de código fuente de programas de ordenador.  
El código de los proyectos alojados en GitHub se almacena generalmente de forma pública. 

**Recursos importantes**
- [GitHub for Developers](https://githubtraining.github.io/training-manual/#/01_getting_ready_for_class)
- [Video Curso de Git y Github](https://www.youtube.com/embed/videoseries?list=PLU8oAlHdN5BlyaPFiNQcV0xDqy0eR35aU)

## Creación de cuenta en GitHub.com

1. Acceda a [GitHub.com](https://github.com/) y dé click en **Sign up**
1. Agregue su cuenta de correo electrónico
1. Asigne una contraseña
1. Elija un nombre de usuario
1. Elija si desea recibir actualizaciones de productos de github por email (y o n)
1. Resuelva el acertijo para validar que eres una persona real
1. Presiona el botón de crear cuenta
1. Recibirás un correo con un código de validación. Ingresa este código en el proceso de creación de cuenta.
1. Te pedirá el tamaño de su equipo de trabajo y si eres estudiante o profesor. Elige las opciones que más se ajusten a su realidad. Recomiendo no elegir ninguno de ellos. Luego **continue**.
1. Te preguntará por cuales herramientas de github esta interesado. Elige las opciones que más se ajusten a su realidad. Recomiendo elegir solo **Collaborative coding**. Luego **continue**.
1. Elije el plan Free y presiona el botón **Continue for free**

Listo!!
Ya tenemos nuestra cuenta de Github creada

## Crear y habilitar la llave ssh para asegurar la cuenta

[ver tutorial original](https://docs.github.com/es/authentication/connecting-to-github-with-ssh)

### Generar una nueva llave SSH
1. Abrir el `Git bash`
2. Crear la llave con el correo electrónico que se usó para crear la cuenta de GitHub
```bash
ssh-keygen -t ed25519 -C "[email]"
```
3. Agregar al servidor (dominio) de GitHub como un equipo conocido para enviar información por ssh para las claves de tipo `ed25519`
```bash
ssh-keyscan -t ed25519 github.com >> ~/.ssh/known_hosts
```
### Adicionar la llave SSH al agente ssh-agent
1. Abrir el `Git bash` (o en el mismo del paso anterior)
2. Asegurarse que el agente se encuentra en ejecución. 
```bash
eval "$(ssh-agent -s)"
```
3. Adicionar su llave **SSH privada** al agente  
```bash
ssh-add ~/.ssh/id_ed25519
```
4. Copiar la llave **SSH pública** al portapapeles
```bash
clip < ~/.ssh/id_ed25519.pub
```

## Agregar llave SSH a cuenta GitHub.com
Siga las instrucciones del [manual](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) en la página de GitHub

# Comandos importantes que usaremos con Git y Github

## Crear Repositorios
- Crea un nuevo repositorio local
```powershell
git init
```
- Descarga un proyecto desde un repositorio global (como Github) y toda su historia de versión
```powershell
git clone [url]
```

## Ver y comprometer cambios
- Enumera todos los archivos nuevos o modificados que se deben confirmar
```powershell
git status
```

- Muestra las diferencias de archivos que no se han enviado aún al área de espera
```powershell
git diff
```

- Agrega archivo para preparar la versión
```powershell
git add [file]
```

- Agrega todos los archivos con cambios para preparar la versión
```powershell
git add .
```

- Registra las instantáneas del archivo permanentemente en el historial de versión
```powershell
git commit -m "[descriptive message]"
```

## Sincronizar cambios con GitHub
- Descarga todo el historial del marcador del repositorio
```powershell
 git fetch [bookmark]
```

- Descarga el historial del marcador e incorpora cambios
```powershell
git pull
```

- Carga todos los commits de la rama local al GitHub
```powershell
git push [alias] [branch]
```