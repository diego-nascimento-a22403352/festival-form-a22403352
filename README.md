# Festival

## Explicação da ordenação
A linha `ordering = ["dia__data", "hora"]` faz com que a lista de concertos seja ordenada primeiro pela data. Se houver concertos no mesmo dia, são ordenados pela hora.

## Alterações feitas
* **Dias:** Configurei os dias para aparecerem por ordem crescente.
* **Concertos:** * O formulário foi alterado para permitir editar todos os campos do concerto.
  * Criei a opção para apagar concertos.
  * Criei uma nova página para adicionar concertos.
* **Palcos:**
  * Adicionei um campo na base de dados para indicar se o palco tem acessibilidade.
  * A página dos palcos agora mostra a capacidade, o número de concertos e a acessibilidade.
  * Criei a opção para editar as informações e a imagem dos palcos.