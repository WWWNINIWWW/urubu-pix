# API Urubu do Pix
Backend que simula o sistema de negociação utilizado pelo urubu do pix utilizando Django Rest Framework

## Dependências 
- Django==4.2.4
- djangorestframework==3.14.0

## Funções
1. Criar e obter usuários (`GET`, `POST`  >> `/users/`)
2. Mudar e deletar usuarios (`GET`, `PUT`, `DELETE` >> `/users/id/`)
3. Acesso a valores dos usuarios (`GET` >> `/values/` e `/values/id/`)
4. Opções de transações - Deposito e Saque (`GET`, `PUT` >> `/transactions/id`)
5. Rendimento de 1000% ao mês (33.33% ao dia)

## Sistema
- Dar opções de criaçoes de usuarios, podendo alterar o nome atraves do model `users` (`GET`, `POST` >> `/users/` e `GET`, `PUT`, `DELETE` >> `/users/id/` )
- Criação de valores aos usuarios sem alterar os valores por PUT atraves do model `values` (somente `GET`)
- Transações de saque e deposito ao model `values` atraves do model `transactions` (realizada atraves do `PUT` em `deposit` e `withdraw`)
- Rendimento por dia atraves somente da model `values` (33.33%)
