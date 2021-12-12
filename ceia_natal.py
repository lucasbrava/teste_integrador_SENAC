print("Olá! Esse é o app teste da lista de comidas do natal da familia Oliveira desse ano :)")
lista_nome = []
lista_cpf = []
lista_item = []

x = 0
for x in range(10):
    nome = input("Insira seu nome aqui: ")
    print("Seu nome é: ", nome)
    confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
    print(confirma)
    if confirma == 1:
        lista_nome.append(nome)
        print("Olá, ", nome)
    while confirma == 2:
        print("Ok, insira seu nome novamente: ")
        nome = input("Insira seu nome aqui: ")
        print("Seu nome é: ", nome)
        confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
        print(confirma)
        if confirma == 1:
            lista_nome.append(nome)
            print("Olá, ",nome)
    while (confirma>2) or (confirma<1):
        print("Opção inválida. Confirme se está correto.")
        confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
        print(confirma)
        if confirma == 1:
            lista_nome.append(nome)
            print("Olá, ", nome)
        while (confirma>2) or (confirma<1):
            print("Opção inválida. Confirme se está correto.")
            confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
            print(confirma)
            if confirma == 1:
                lista_nome.append(nome)
                print("Olá, ", nome)
        while confirma == 2:
            print("Ok, insira seu nome novamente: ")
            nome = input("Insira seu nome aqui: ")
            print("Seu nome é: ", nome)
            confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
            print(confirma)
            if confirma == 1:
                lista_nome.append(nome)
                print("Olá, ", nome)
            while (confirma>2) or (confirma<1):
                print("Opção inválida. Confirme se está correto.")
                confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                print(confirma)
                if confirma == 1:
                    lista_nome.append(nome)
                    print("Olá, ", nome)


    cpf = input("Insira seu CPF aqui, apenas numeros: ")
    tamanho = len(cpf)
    while tamanho != 11:
        print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
        cpf = input("Insira seu CPF aqui, apenas numeros: ")
        tamanho = len(cpf)
    print("Seu CPF é: ", cpf)
    tamanho = len(cpf)
    while tamanho != 11:
        print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
        cpf = input("Insira seu CPF aqui, apenas numeros: ")
        tamanho = len(cpf)
    confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
    print(confirma)
    
    if confirma == 1:
        while cpf in lista_cpf:
            print("CPF indisponivel, insira um CPF disponivel.")
            cpf=input("Insira seu CPF aqui, apenas numeros: ")
            tamanho = len(cpf)
            while tamanho !=11:
                print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                cpf = input("Insira seu CPF aqui, apenas numeros: ")
                tamanho = len(cpf)
                while tamanho !=11:
                    print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                    cpf = input("Insira seu CPF aqui, apenas numeros: ")
            print("Seu CPF é: ", cpf)
            confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
            print(confirma)
        else:
            print("CPF disponivel")
            lista_cpf.append(cpf)
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
        print(confirma)
        if confirma == 1:
            while cpf in lista_cpf:
                print("CPF indisponivel, insira um CPF disponivel")
                cpf=input("Insira seu CPF aqui, apenas numeros: ")
            tamanho = len(cpf)
            while tamanho !=11:
                print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                cpf = input("Insira seu CPF aqui, apenas numeros: ")
                tamanho = len(cpf)
                while tamanho !=11:
                    print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                    cpf = input("Insira seu CPF aqui, apenas numeros: ")
                print("Seu CPF é: ", cpf)
                confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                print(confirma)
            else:
                lista_cpf.append(cpf)
                print("CPF disponivel")
    while (confirma>2) or (confirma<1):
        print("Opção inválida. Confirme se está correto.")
        confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
        print(confirma)
        if confirma == 1:
            while cpf in lista_cpf:
                print("CPF indisponivel, insira um CPF disponivel")
                cpf=input("Insira seu CPF aqui, apenas numeros: ")
            tamanho = len(cpf)
            while tamanho !=11:
                print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                cpf = input("Insira seu CPF aqui, apenas numeros: ")
                tamanho = len(cpf)
                while tamanho !=11:
                    print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                    cpf = input("Insira seu CPF aqui, apenas numeros: ")
                print("Seu CPF é: ", cpf)
                confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                print(confirma)            
            else:
                lista_cpf.append(cpf)
                print("CPF disponivel")
        while (confirma>2) or (confirma<1):
            print("Opção inválida. Confirme se está correto.")
            confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
            print(confirma)
            if confirma == 1:
                while cpf in lista_cpf:
                    print("CPF indisponivel, insira um CPF disponivel")
                    cpf=input("Insira seu CPF aqui, apenas numeros: ")
                    tamanho = len(cpf)
                    while tamanho !=11:
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
                if confirma==1:
                    while cpf in lista_cpf:
                        print("CPF indisponivel, insira um CPF disponivel")
                        cpf=input("Insira seu CPF aqui, apenas numeros: ")
                        tamanho = len(cpf)
                        while tamanho !=11:
                            print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                            cpf = input("Insira seu CPF aqui, apenas numeros: ")
                            tamanho = len(cpf)
                            while tamanho !=11:
                                print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                                cpf = input("Insira seu CPF aqui, apenas numeros: ")
                            print("Seu CPF é: ", cpf)
                            confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                            print(confirma)
                    else:
                        lista_cpf.append(cpf)
                        print("CPF disponivel")
            while (confirma>2) or (confirma<1):
                print("Opção inválida.Confirme se está correto.")
                confirma = int(input("Está correto? 1.Sim ou Não\nR:"))
                print(confirma)
                if confirma ==1:
                    while cpf in lista_cpf:
                        print("CPF indisponivel, insira um CPF disponivel")
                        cpf=input("Insira seu CPF aqui, apenas numeros: ")
                        tamanho = len(cpf)
                        while tamanho !=11:
                            print("Erro! Numero de caracteres invalidos. Digite novamente seu CPF: ")
                            cpf = input("Insira seu CPF aqui, apenas numeros: ")
                            tamanho = len(cpf)
                            while tamanho !=11:
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
            print(confirma)

    item = input("Insira o item que deseja levar aqui: ")
    print("O item selecionado é: ", item)
    confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
    print(confirma)

    if confirma == 1:
        while item in lista_item:
            print("Item já selecionado, insira outro item para levar")
            item=input("Insira outro item: \nR:")
            while item in lista_item:
                print("Item já selecionado, insira outro item para levar.")
                item=input("insira outro item: \nR:")                  
        else:
            lista_item.append(item)
            print("Item adicionado a lista")

    while (confirma>2) or (confirma<1):
        print("Opção inválida. Confirme se está correto.\n")
        confirma = int(input("Está correto? 1.Sim ou 2.não\nR:"))
        print(confirma)
        if confirma == 1:
            while item in lista_item:
                print("Item já selecionado, insira outro item para levar.")
                item=input("Insira outro item: \nR:")
                while item in lista_item:
                    print("Item já selecionado, insria outro item para levar.")
                    item=input("Insira outro item: \nR:")
            else:
                lista_item.append(item)
                print("Item adicionado a lista")
        while confirma == 2:
            print("Ok, insira o item que deseja levar. ")
            item = input("Insira o item aqui: ")
            print("Seu item é: ", item)
            confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
            print(confirma)
            if confirma == 1:
                while item in lista_item:
                    print("Item já selecionado, insira outro item para levar.")
                    item=input("Insira outro item: \nR:")
                    while item in lista_item:
                        print("Item já adicionaod, insira outro item.")
                        item=input("Insira outro item: \nR:")
                else:
                    lista_item.append(item)
                    print("Item adicionado a lista")
        while (confirma>2) or (confirma<1):
            print("Opção inválida. Confirme se está correto. \n")
            confirma = int(input("Está correto? 1.Sim ou 2.não\nR:"))
            print(confirma)
            if confirma == 1:
                while item in lista_item:
                    print("item já selecionado, insira outro item.")
                    item=input("Insira outro item: \nR:")
                    while item in lista_item:
                        print("Item já selecionado, insira outro item.")
                        item=input("Insira outro item: \nR:")
                else:
                    lista_item.append(item)
                    print("Item adicionado a lista")

    while confirma == 2:
        print("Ok, insira o item que deseja levar: ")
        item = input("Insira o item aqui: ")
        print("Seu item é:   ", item)
        confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
        print(confirma)
        if confirma == 1:
            while item in lista_item:
                print("Item já selecionado, insira outro item.")
                item=input("Insira outro item: \nR:")
                while item in lista_item:
                    print("Item já selecionado, insira outro item.")
                    item=input("insira outro item: \nR:")
            else:
                lista_item.append(item)
                print("Item adicionado a lista")
        while confirma == 2:
            print("Ok, insira o item que deseja levar:")
            item = input("Insira o item aqui:\nR: ")
            print("Seu item é: ", item)
            confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
            print(confirma)
            if confirma == 1:
                while item in lista_item:
                    print("item já selecionado, insira outro item.")
                    item = input("Insira o item aqui:\nR: ")
                    while item in lista_item:
                        print("Item já selecionado, insira outro item.")
                        item=input("Insira outro item aqui: \nR:")
                else:
                    lista_item.append(item)
                    print("item adicionado a lista")
        while (confirma > 2) or (confirma<1):
            print("Opção inválida. Confirme se está correto.")
            confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
            print(confirma)
            if confirma == 1:
                while item in lista_item:
                    print("item já selecionado, insira outro item.")
                    item=input("Insira o item aqui: \nR:")
                else:
                    lista_item.append(item)
                    print("Item adicionado a lista")
            while confirma == 2:
                print("Ok, insira o item novamente: ")
                item = input("Insira o item aqui: ")
                print("Seu item é: ", item)
                confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                print(confirma)
                if confirma == 1:
                    while item in lista_item:
                        print("Item já selecionado, insira outro item.")
                        item=input("Insira outro item aqui: \nR:")
                        while item in lista_item:
                            print("Item já selecionado, insira outro item.")
                            item=input("Insira outro item aqui: \nR:")
                    else:
                        lista_item.append(item)
                        print("Item adicionado a lista")

    adicionar = input("Deseja adicionar mais algum item? 1.Sim ou 2.Não\nR:")
    print(adicionar)
    
    while (confirma>2) or (confirma<1):
        print("Opção inválida. Confirme se está correto.")
        confirma=int(input("Está correto? 1.Sim ou 2.Não\nR:"))
        print(confirma)
        
    if adicionar == "2":
        print("Massa, finalizado! Boa ceia de natal!")

    if adicionar == "1":
        print("Ok, insira o item que deseja levar: ")
        item2 = input("Insira o item aqui: ")
        print("Seus itens são: ", item, "e", item2)
        confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
        print(confirma)

        if confirma == 1:
            while item2 in lista_item:
                print("Item já selecionado, insira outro item.")
                item2=input("Insira o segundo item aqui: \nR:")
                while item2 in lista_item:
                    print("Item já selecionado, insira outro item.")
                    item2=input("Insira o segundo item aqui: \nR:")
            else:
                lista_item.append(item2)
                print("Item adicionado a lista")
                print("Boa ceia de natal!")

        while (confirma>2) or (confirma<1):
            print("Opção inválida. Confirme se está correto.")
            confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
            print(confirma)
            if confirma == 1:
                    while item2 in lista_item:
                        print("item já selecionado, insira outro item.")
                        item=input("Insira o item aqui: \nR:")
                    else:
                        lista_item.append(item2)
                        print("Item adicionado a lista")
            while confirma ==2:
                print("Ok, insira o item novamente: ")
                item2=input("Insira o item aqui:")
                print("Seu item é: ",item2)
                confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
                print(confirma)
                if confirma==1:
                    while item2 in lista_item:
                        print("Item já selecionado, insira outro item.")
                        item2=input("Insira outro item aqui: \nR:")
                        while item2 in lista_item:
                            print("Item já selecionado, insira outro item.")
                            item2=input("Insira outro item aqui: \nR:")
                    else:
                        lista_item.append(item2)
                        print("Item adicionado a lista")
                
        while confirma == 2:
            print("Ok, insira o item novamente: ")
            item2 = input("Insira o item aqui: ")
            print("Seu item é: ", item, "e", item2)
            confirma = int(input("Está correto? 1.Sim ou 2.Não\nR:"))
            print(confirma)
            if confirma == 1:
                while item2 in lista_item:
                    print("Item já adicionado a lista, insira outro item.")
                    item2=input("Insira o segundo item aqui: \nR:")
                    while item2 in lista_item:
                        print("Item já adicionado a lista, insira outro item.")
                        item2=input("Insira o segundo item aqui: \nR:")
                else:
                    lista_item.append(item2)
                    print("Item adicionado a lista")
        
      
                    
                 
   #falta adc a confirmação do item1 e item2 no else
   #falta finalizar o app no final com break(digite fim para finalizar) ou continue(digite continue para continuar)
