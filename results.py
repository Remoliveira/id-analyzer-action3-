import re 
import csv
import time
import pandas as pd



def camelSplit(identifier):
    matches = re.finditer(
        '.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$|_)', identifier)
    return [m.group(0).replace("_", "") for m in matches]



identificadoresCsv = pd.read_csv('IdentificadoresPosProcessamentoDeCategorira.csv')


with open('FinalResultCategories.csv', mode = 'w') as csv_file:

    fieldnames = ['IDENTIFICADOR', 'TIPO', 'POSICAO', 'NUM_DE_PALAVRAS', 'NOME_NUM_FINAL','NOME_NUM_MEIO','NOME_TIPO_IGUAL', 'TIPO_PARTE_NOME','NOME_PARTE_TIPO','NOME_UMA_LETRA','NOME_INICIA_UNDERLINE','LETRA_INICIA_TIPO']
    writer = csv.DictWriter(csv_file,fieldnames = fieldnames)
    writer.writeheader()
    categoria = 0   
  
    
    for row in identificadoresCsv.iterrows():
     
            csvEntries = row[1]

            identificador = csvEntries.Identificador
   
            tipo = csvEntries.Tipo
    
            posicao = csvEntries.Posicao
        

            # skip = False
            # if(re.search('=',identificador)):
            #     if(re.search("number",identificador)):
            #         # print(identificador)
            #         # print(tipo)
            #         identificador = tipo
            #         # print(identificador)
            #         tipo  = "int"
            #         # print(variacao)
            #     else:
            #         skip = True


            idSplit = camelSplit(identificador)
            tipoSplit = camelSplit(tipo)
            # variacao = identificadorTupla[3]
            # print(len(idSplit) , " ", idSplit) 
            
            if(re.search("^_\w",identificador) and len(idSplit) == 1):
                # print(identificador)
                # identificador = identificador.lstrip("_")
               
                # print(identificador)
                idIniciado_ = 1
            else:
                idIniciado_ = 0

            
            # if(posicao == None):
            #     posicao = variacao


            numeroPalavra = len(idSplit)
            # print(numeroPalavra)

         

            if(re.search("\D+[a-zA-z]+\d+$",identificador)):
                # print("id com numero no final: ",identificador , "tipo: ", tipo, projeto)
                numFinal = 1
            else:
                numFinal = 0
            
            if(re.search("\d+.*\D+$",identificador)):
                # print("id com numero no meio: ",identificador, "tipo: ",tipo, projeto)
                numMeio = 1
            else:
                numMeio = 0
            
            if(identificador.casefold() == tipo.casefold()):
                # print("id == tipo ", identificador, "--", tipo)
                idIgualTipo = 1
            else:
                idIgualTipo = 0

            idNoTipo = 0
            tipoNoId = 0
            for idUnico in idSplit:
                for tipoUnico in tipoSplit:
           
                    if(idUnico == tipoUnico):
            
                        # print(identificador,"-----",tipo)
                        
                        if(len(idSplit)> len(tipoSplit)):
                            # print(identificador,"-----",tipo, projeto)
                            tipoNoId = 1

                        elif(len(tipoSplit)> len(idSplit)):
                            # print(identificador,"-----",tipo, projeto)
                            idNoTipo = 1

                        # elif(identificador.casefold() != tipo.casefold()):
                        #     # print(identificador,"-----",tipo)
                        #     print((identificador.casefold()))
                        #     print("--")
                        #     print(tipo.casefold())
                        #     tipoNoId = 1
                        # else:
                        #     print(identificador,"-----",tipo)
                        
                    
            letraInicioTipo = 0
            if(len(identificador) == 1):
                # print(identificador,"--", tipo) 
                idUmaLetra = 1
                if(len(tipo)>0):
                    if(identificador == tipo[0]):
                        # print(identificador,"--",tipo, projeto)
                        letraInicioTipo = 1
                    else:
                        letraInicioTipo = 0
            else:
                idUmaLetra = 0           

            # 0 - Id que nao se encaixa
            # 1 - Número final
            # 2 - Número meio
            # 3 - Id igual ao tipo
            # 4 - Id de uma letra
            # 5 - Tem o tipo no meio do id 
            # 6 - Id camel case 2 partes
            # 7 - Id camel case 3+
            # 8 - Id separado por underscore
            # 9 - Id iniciado por underscore
            # 10 - Id somente uma palavra

            # juntar 6 7 8 no mesmo padrão
            # duas analise, uma palavra ou mais de uma palava
            # todos os outros
            # atributo ou classe metodo. 
            # substring contido no nome do tipo
            # nome do id contido no tipo

            # UMA IDEIA NOVA PRA QUANDO FOR ESCREVER O ARTIGO: IDENTIFICADOR DE UMA LETRA SENDO A MESMA LETRA INICIAL DE SEU TIPO  PODE COLOCAR

          
            writer.writerow({'IDENTIFICADOR':identificador, 'TIPO':tipo, 'POSICAO':posicao, 'NUM_DE_PALAVRAS':numeroPalavra, 
            'NOME_NUM_FINAL':numFinal,'NOME_NUM_MEIO':numMeio,'NOME_TIPO_IGUAL':idIgualTipo, 'TIPO_PARTE_NOME':tipoNoId,'NOME_PARTE_TIPO':idNoTipo,'NOME_UMA_LETRA':idUmaLetra,'NOME_INICIA_UNDERLINE':idIniciado_,'LETRA_INICIA_TIPO':letraInicioTipo})

          
            
        
   





