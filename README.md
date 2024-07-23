# Simulador de Empréstimos

Este projeto é um simulador de empréstimos baseado no desafio do GitHub da [backend-br](https://github.com/backend-br/desafios), que visa criar uma aplicação para simular diferentes tipos de empréstimos para clientes.

## Funcionalidades

- **Cadastro de Clientes**: Permite cadastrar clientes com CPF, nome, idade, salário e estado de residência.
- **Simulação de Empréstimos**: Permite simular diferentes tipos de empréstimos (pessoal, consignado e com garantia) para os clientes cadastrados.
- **Validação de CPF**: O CPF é formatado automaticamente no padrão `000.000.000-00`.
- **Requisitos de Empréstimos**: Verifica se o cliente atende aos requisitos para os tipos de empréstimos disponíveis.
- **Limitação de Empréstimo**: O valor do empréstimo solicitado não pode exceder 5 vezes o salário do cliente.
- **Confirmação de Empréstimo**: Após a simulação, o cliente pode confirmar ou cancelar o empréstimo.

## Tecnologias Utilizadas

- Python
- Git

## Como Utilizar

### Pré-requisitos

- Python 3.x instalado
- Git instalado

 ##  Exemplo de Uso
   
Cadastro de Cliente
O usuário será solicitado a inserir as seguintes informações:

CPF (apenas números, será formatado automaticamente)
Nome
Idade
Salário
Estado (sigla do estado)
Simulação de Empréstimo
O usuário pode simular:

Empréstimo pessoal
Empréstimo consignado
Empréstimo com garantia
Limitação de Valor do Empréstimo
O valor do empréstimo solicitado não pode exceder 5 vezes o salário do cliente. Se o valor exceder, o usuário será solicitado a inserir um novo valor.

Confirmação
Após a simulação do empréstimo, o valor dos juros e o valor total serão exibidos. O usuário poderá confirmar ou cancelar o empréstimo.

Contribuição
Sinta-se à vontade para contribuir com o projeto. Para isso, siga os passos abaixo:

Fork o projeto
Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)
Commit suas mudanças (git commit -m 'Add some AmazingFeature')
Push para a branch (git push origin feature/AmazingFeature)
Abra um Pull Request
Licença
Este projeto está licenciado sob a MIT License.

Contato
Robson Avelar - @rob-avelar - rob.avelar.nl@gmail.com - https://www.linkedin.com/in/robson-avelar-053881245/

Link do Projeto: https://github.com/rob-avelar/simulador-emprestimos
