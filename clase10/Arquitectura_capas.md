# Arquitectura por capas

La arquitectura basada en capas se enfoca en la distribución de roles y responsabilidades de forma jerárquica proveyendo una forma muy efectiva de separación de responsabilidades. El rol indica el modo y tipo de interacción con otras capas, y la responsabilidad indica la funcionalidad que está siendo desarrollada.

![Arquitectura multi capa](https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/assets/sapr_0101.png)

## Ventajas y Desventajas
### Ventajas
- Reutilización de capas
- Facilita la estandarización
- Dependencias se limitan a intra-capa
- Contención de cambios a una o pocas capas

### Desventajas
- A veces no se logra la contención del cambio y se requiere una cascada de cambios en varias capas
- Pérdida de eficiencia
- Trabajo innecesario por parte de capas más internas o redundante entre varias capas
- Dificultad de diseñar correctamente la granularidad de las capas

## Arquitectura de N-Capas

Este estilo de despliegue arquitectónico describe la separación de la funcionalidad en segmentos separados de forma muy parecida al estilo de capas, pero en el cual cada segmento está localizado en un computador físicamente separado. Este estilo ha evolucionado desde la aproximación basada en componentes generalmente usando métodos específicos de comunicación asociados a una plataforma en vez de la aproximación basada en mensajes. 

![Arquitectura multi capa 2](https://geeks.ms/cfs-file.ashx/__key/CommunityServer.Blogs.Components.WeblogFiles/jkpelaez/clip_5F00_image002_5F00_thumb_5F00_1C48303C.gif)

