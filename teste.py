print("Bem vindo a LFM Boutique\nby lucasbrava")

lista_cliente = []
lista_cpf = []
lista_fornecedor = []
lista_produto = []
lista_usuario = []
lista_vendas = []

acesso = int(input("Digite a opção desejada:\n1-Acessar conta existente\n2-Cadastrar nova conta\nR:"))
if acesso == 1:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    # realizar consulta no banco de dados para confirmar acesso
if acesso == 2:
    cadastro_user = input("Insira um nome de usuário: ")
    senha1 = input("Insira sua senha: ")
    senha2 = input("Insira a senha novamente: ")
    if senha1 == senha2:
        print("Usuário cadastrado com sucesso!")
        usuario = cadastro_user
        lista_usuario.append(usuario)
    while senha1 != senha2:
        print("As senhas não coincidem. Tente novamente.")
        senha1 = input("Insira sua senha: ")
        senha2 = input("Insira a senha novamente: ")
        if senha1 == senha2:
            print("Usuário cadastrado com sucesso!")
            usuario = cadastro_user
            lista_usuario.append(usuario)
while acesso > 2 or acesso < 1:
    print("Opção inválida. Digite uma opção válida.")
    acesso = int(input("Digite a opção desejada:\n1-Acessar conta existente\n2-Cadastrar nova conta\nR:"))
    if acesso == 1:
        usuario = input("Usuário: ")
        senha = input("Senha: ")
    elif acesso == 2:
        cadastro_user = input("Insira um nome de usuário: ")
        senha1 = input("Insira sua senha: ")
        senha2 = input("Insira a senha novamente: ")
        if senha1 == senha2:
            print("Usuário cadastrado com sucesso!")
            usuario = cadastro_user
            lista_usuario.append(usuario)
        while senha1 != senha2:
            print("As senhas não coincidem. Tente novamente.")
            senha1 = input("Insira sua senha: ")
            senha2 = input("Insira a senha novamente: ")
            if senha1 == senha2:
                print("Usuário cadastrado com sucesso!")
                usuario = cadastro_user
                lista_usuario.append(usuario)
print("Bem vindo, ", usuario)
x = 0
while x == 0:
    menu = int(input("O que deseja consultar?\n1-CLIENTES\n2-ESTOQUE\n3-FORNECEDORES\n4-PRODUTOS\n5-VENDAS\n6-FINALIZAR E SAIR\nR:"))
    while menu>6 or menu<1:
        print("Você escolheu retornar ao Menu Inicial ou digitou uma opção inválida.")
        menu = int(input("O que deseja consultar?\n1-CLIENTES\n2-ESTOQUE\n3-FORNECEDORES\n4-PRODUTOS\n5-VENDAS\nR:"))
    if menu == 1:
        confirma = int(input("Você acessou: CLIENTES\nEstá correto? 1. Sim, continuar ou 2.Voltar ao Menu\nR:"))
        if confirma == 1:
            opcao_cliente = int(input("Seção de clientes\n1. Novo cliente\n2. Consultar clientes cadastrados\nR:"))
            if opcao_cliente == 2:
                print("Consulta de clientes cadastrados.")
                id_cliente=input("Informe o ID do cliente para ser consultado: ")
                #printar informações do cliente a ser consultado no BD
            if opcao_cliente == 1:
                print("Cadastre o novo cliente.")
                id_cliente = int(input("ID Cliente: "))
                nome = input("Nome: ")
                telefone = int(input("Telefone: "))
                cpf = input("CPF: ")
                tamanho = len(cpf)
                while tamanho != 11:
                    print("Erro! Numero de caracteres invalidos. Digite novamente o CPF: ")
                    cpf = input("Insira o CPF aqui, apenas numeros: ")
                    tamanho = len(cpf)
                print("O CPF é: ", cpf)
                tamanho = len(cpf)
                while tamanho != 11:
                    print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                    cpf = input("Insira seu CPF aqui, apenas numeros: ")
                    tamanho = len(cpf)
                confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                if confirma == 1:
                    while cpf in lista_cpf:
                        print("CPF indisponivel, insira um CPF disponivel.")
                        cpf = input("Insira seu CPF aqui, apenas numeros: ")
                        tamanho = len(cpf)
                        while tamanho != 11:
                            print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                            cpf = input("Insira seu CPF aqui, apenas numeros: ")
                            tamanho = len(cpf)
                            while tamanho != 11:
                                print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                                cpf = input("Insira seu CPF aqui, apenas numeros: ")
                        print("Seu CPF é: ", cpf)
                        confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                        
                    else:
                        print("CPF disponivel")
                        lista_cpf.append(cpf)
                        
                while confirma == 2:
                    print("Ok, insira o CPF novamente: ")
                    cpf = input("Insira o CPF aqui: ")
                    tamanho = len(cpf)
                    while tamanho != 11:
                        print("Erro! Numero de caracteres invalidos. Digite novamente o CPF: ")
                        cpf = input("Insira o CPF aqui, apenas numeros: ")
                        tamanho = len(cpf)
                    print("Seu CPF é: ", cpf)
                    confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                    print(confirma)
                    if confirma == 1:
                        while cpf in lista_cpf:
                            print("CPF indisponivel, insira um CPF disponivel")
                            cpf = input("Insira o CPF aqui, apenas numeros: ")
                        tamanho = len(cpf)
                        while tamanho != 11:
                            print("Erro! Numero de caracteres invalidos. Digite novamente o CPF: ")
                            cpf = input("Insira o CPF aqui, apenas numeros: ")
                            tamanho = len(cpf)
                            while tamanho != 11:
                                print("Erro! Numero de caracteres invalidos. Digite novamente o CPF: ")
                                cpf = input("Insira o CPF aqui, apenas numeros: ")
                            print("O CPF é: ", cpf)
                            confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                        else:
                            lista_cpf.append(cpf)
                            print("CPF disponivel")
                while (confirma > 2) or (confirma < 1):
                    print("Opção inválida. Confirme se está correto.")
                    confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                    print(confirma)
                    if confirma == 1:
                        while cpf in lista_cpf:
                            print("CPF indisponivel, insira um CPF disponivel")
                            cpf = input("Insira oCPF aqui, apenas numeros: ")
                        tamanho = len(cpf)
                        while tamanho != 11:
                            print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                            cpf = input("Insira o CPF aqui, apenas numeros: ")
                            tamanho = len(cpf)
                            while tamanho != 11:
                                print("Erro! Numero de caracteres invalidos. Digite novamente o CPF: ")
                                cpf = input("Insira o CPF aqui, apenas numeros: ")
                            print("O CPF é: ", cpf)
                            confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                            print(confirma)
                        else:
                            lista_cpf.append(cpf)
                            print("CPF disponivel")
                    while (confirma > 2) or (confirma < 1):
                        print("Opção inválida. Confirme se está correto.")
                        confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                        print(confirma)
                        if confirma == 1:
                            while cpf in lista_cpf:
                                print("CPF indisponivel, insira um CPF disponivel")
                                cpf = input("Insira seu CPF aqui, apenas numeros: ")
                                tamanho = len(cpf)
                                while tamanho != 11:
                                    print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                                    cpf = input("Insira seu CPF aqui, apenas numeros: ")
                                print("Seu CPF é: ", cpf)
                                confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                                print(confirma)
                            else:
                                lista_cpf.append(cpf)
                                print("CPF disponivel")
                        while confirma == 2:
                            print("Ok, insira seu CPF novamente: ")
                            cpf = input("Insira seu CPF aqui:")
                            tamanho = len(cpf)
                            while tamanho != 11:
                                print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                                cpf = input("Insria seu CPF aqui: ")
                                tamanho = len(cpf)
                            print("Seu CPF é: ", cpf)
                            confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                            print(confirma)
                            if confirma == 1:
                                while cpf in lista_cpf:
                                    print("CPF indisponivel, insira um CPF disponivel")
                                    cpf = input("Insira seu CPF aqui, apenas numeros: ")
                                    tamanho = len(cpf)
                                    while tamanho != 11:
                                        print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                                        cpf = input("Insira seu CPF aqui, apenas numeros: ")
                                        tamanho = len(cpf)
                                        while tamanho != 11:
                                            print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                                            cpf = input("Insira seu CPF aqui, apenas numeros: ")
                                        print("Seu CPF é: ", cpf)
                                        confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                                        print(confirma)
                                else:
                                    lista_cpf.append(cpf)
                                    print("CPF disponivel")
                        while (confirma > 2) or (confirma < 1):
                            print("Opção inválida.Confirme se está correto.")
                            confirma = int(input("Está correto? 1.Sim ou Não\nR:"))
                            print(confirma)
                            if confirma == 1:
                                while cpf in lista_cpf:
                                    print("CPF indisponivel, insira um CPF disponivel")
                                    cpf = input("Insira seu CPF aqui, apenas numeros: ")
                                    tamanho = len(cpf)
                                    while tamanho != 11:
                                        print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                                        cpf = input("Insira seu CPF aqui, apenas numeros: ")
                                        tamanho = len(cpf)
                                        while tamanho != 11:
                                            print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                                            cpf = input("Insira seu CPF aqui, apenas numeros: ")
                                    print("Seu CPF é: ", cpf)
                                    confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                                    print(confirma)
                                else:
                                    lista_cpf.append(cpf)
                                    print("CPF disponivel")

                    while confirma == 2:
                        print("Ok, insira seu CPF novamente: ")
                        cpf = input("Insira seu CPF aqui: ")
                        tamanho = len(cpf)
                        while tamanho != 11:
                            print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                            cpf = input("Insira seu CPF aqui, apenas numeros: ")
                            tamanho = len(cpf)
                        print("Seu CPF é: ", cpf)
                        confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                        if confirma ==1:
                            print("CPF cadastrado com sucesso.")
                while id_cliente in lista_cliente:
                    print("ID indisponivel, esse ID está cadastrado no banco de dados da empresa.")
                    id_cliente = int(input("ID Cliente: "))
            
                else:
                    lista_cliente.append(id_cliente)
                    print("ID disponivel. Cliente cadastrado com sucesso!")
    if menu == 2:
        confirma = int(input("Você acessou: ESTOQUE\nEstá correto? 1.Sim, continuar ou 2.Voltar ao Menu\nR:"))
        if confirma == 1:
            opcao_estoque = int(input("SEÇÃO DE ESTOQUE\n1. Consultar estoque disponivel\nR:"))
            if opcao_estoque ==1:
                print("Consulta de estoque disponivel em loja.")
                id_produto=input("Informe o ID do produto a ser consultado: ")
                #printar informações do produto em estoque a ser consultado no BD
    if menu == 3:
        confirma = int(input("Você acessou: FORNECEDOR\nEstá correto? 1. Sim, continuar ou 2.Voltar ao Menu\nR:"))
        if confirma == 1:
            opcao_fornecedor = int(input("Seção de fornecedores\n1. Novo fornecedor\n2. Consultar fornecedores cadastrados\nR:"))
            if opcao_fornecedor == 2:
                print("Consulta de fornecedores cadastrados.")
                id_fornecedor=input("Informe o ID do fornecedor para ser consultado: ")
                #printar informações do cliente a ser consultado no BD
            elif opcao_fornecedor == 1:
                print("Cadastre o novo fornecedor.")
                id_fornecedor = int(input("ID Fornecedor: "))
                nome = input("Nome: ")
                telefone = int(input("Telefone: "))
                telefone2 =int(input("Telefone 2: "))
                while id_fornecedor in lista_fornecedor:
                    print("ID indisponivel, esse ID está cadastrado no banco de dados da empresa.")
                    id_fornecedor= int(input("ID Fornecedor: "))
                else:
                    lista_fornecedor.append(id_fornecedor)
                    print("ID disponível. Fornecedor cadastrado com sucesso!")
    if menu == 4:
        confirma= int(input("Você acessou: PRODUTO\nEstá correto? 1. Sim, continuar ou 2.Voltar ao Menu\nR:"))
        if confirma == 1:
            opcao_produto = int(input("Seção de produtos\n1. Cadastrar novo produto\n2. Consultar produtos cadastrados\nR:"))
            if opcao_produto == 2:
                print("Consulta de produtos cadastrados.")
                id_cliente=input("Informe o ID do produto para ser consultado: ")
                #printar informações do produto a ser consultado no BD
            elif opcao_produto == 1:
                print("Cadastre o novo produto.")
                id_produto = int(input("Digite a ID do produto: "))
                id_fornecedor = int(input("ID Fornecedor: "))
                nome_produto = input("Nome do produto: ")
                valor_produto = float(input("Valor do produto: "))
                descricao_produto =str(input("Descrição do produto: "))
                qtde_produto = int(input("Quantidade de produtos disponiveis: "))
                while id_produto in lista_produto:
                    print("ID indisponivel, esse ID está cadastrado no banco de dados da empresa.")
                    id_produto=int(input("Digite a ID do Produto: "))
                else:
                    lista_produto.append(id_produto)
                    print("ID disponivel. Produto cadastrado com sucesso!")
    if menu == 5:
        confirma = int(input("Você acessou: VENDAS\nEstá correto? 1. Sim, continuar ou 2.Voltar ao Menu\nR:"))
        if confirma == 1:
            opcao_vendas = int(input("Seção de vendas\n1. Nova venda\n2. Consultar vendas anteriores\nR:"))
        if opcao_vendas == 1:
            print("Cadastre uma nova venda.")
            id_vendas = print("ID da venda:")
            id_cliente = int(input("Digite a ID do cliente: "))
            id_produto = int(input("Digite a ID do produto: "))
            vendas_qtd = int(input("Digite a quantidade de produtos para venda: "))
            vendas_preco_unit = float(input("Digite o valor do produto:"))
            vendas_total = print("Total de", vendas_qtd, "por R$", vendas_preco_unit, "valor total da venda R$",(vendas_qtd * vendas_preco_unit))
        elif opcao_vendas == 2:
            print("Consulte a venda desejada:")
            id_vendas=input("Informe o ID da venda para ser consultado: ")
        while confirma > 2 or confirma < 1:
            print("Opção inválida. Digite uma opção válida.")
            confirma = int(input("Você acessou: VENDAS\nEstá correto? 1. Sim, continuar ou 2.Voltar ao Menu\n"))
            if confirma == 1:
                opcao_vendas = int(input("Seção de vendas\n1. Nova venda\n2.Consultar vendas anteriores\n"))
            if opcao_vendas == 1:
                print("Cadastre uma nova venda: ")
            if opcao_vendas == 2:
                print("Consulte a venda desejada: ")
    if menu == 6:
        print("LFM Boutique agradece sua colaboração.")
        break
