# Arquitetura Hexagonal
O projeto segue o padrão da arquitetura hexagonal. Logo todas as regras de negócio vão estar dentro de classes `Services`.
As classes `Services` serão chamadas pelas classes `Ports` que irão retornar as respostas dos `Services`
As classes `Adapters` irão receber a requisição do usuário e serão elas que vão ser chamadas no controller.