import re 
import pandas as pd



def camelSplit(identifier):
    matches = re.finditer(
        '.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$|_)', identifier)
    return [m.group(0).replace("_", "") for m in matches]



identificadoresCsv = pd.read_csv('Identifiers.csv')


kings = []
median =[]
ditto = []
diminutive = []
cognome = []
index = []
shorten = []

for row in identificadoresCsv.iterrows():
        
        csvEntries = row[1]
        # print(csvEntries)
        identificador = csvEntries.nome.replace(" ", "")
        # print(identificador)
        tipo = csvEntries.tipo

        posicao = csvEntries.posicao
    


        idSplit = camelSplit(identificador)
        tipoSplit = camelSplit(tipo)
        # variacao = identificadorTupla[3]
        # print(len(idSplit) , " ", idSplit) 
        
        numeroPalavra = len(idSplit)


        # if(re.search("\D+[a-zA-z]+\d+$",identificador)):
    
        if(re.search("\d$", identificador)):
 
            numFinal = 1
      
            kings.append(identificador)
        else:
            numFinal = 0
        
        if(re.search("\d+.*\D+$",identificador)):
            # print("id com numero no meio: ",identificador, "tipo: ",tipo, projeto)
            numMeio = 1
            median.append(identificador)
        else:
            numMeio = 0
        
        if(identificador.casefold() == tipo.casefold()):
            # print("id == tipo ", identificador, "--", tipo)
            ditto.append(identificador)
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
                        cognome.append(identificador)
                        tipoNoId = 1

                    elif(len(tipoSplit)> len(idSplit)):
                        # print(identificador,"-----",tipo, projeto)
                        diminutive.append(identificador)
                        idNoTipo = 1

          
                
        letraInicioTipo = 0
        if(len(identificador) == 1):

            idUmaLetra = 1
            index.append(identificador)
            if(len(tipo)>0):
      
                tipoLower = tipo[0].lower()
      
                if(identificador == tipoLower):
             
                    shorten.append(identificador)
                    letraInicioTipo = 1
                else:
                    letraInicioTipo = 0
        else:
            idUmaLetra = 0           


        # juntar 6 7 8 no mesmo padrão
        # duas analise, uma palavra ou mais de uma palava
        # todos os outros
        # atributo ou classe metodo. 
        # substring contido no nome do tipo
        # nome do id contido no tipo

        # UMA IDEIA NOVA PRA QUANDO FOR ESCREVER O ARTIGO: IDENTIFICADOR DE UMA LETRA SENDO A MESMA LETRA INICIAL DE SEU TIPO  PODE COLOCAR

        



with open('results.txt', 'w') as arquivo:
    arquivo.write("Nomes de identificadores que possuem alguma categoria de nomeação:\n")    

    kings = ' '.join(kings)
    median = ' '.join(median)
    ditto = ' '.join(ditto)
    diminutive = ' '.join(diminutive)
    cognome = ' '.join(cognome)
    index = ' '.join(index)
    shorten = ' '.join(shorten)

    arquivo.write(f'Kings: {kings}\n')
    arquivo.write(f'Median: {median}\n')
    arquivo.write(f'Ditto: {ditto}\n')
    arquivo.write(f'Diminutive: {diminutive}\n')
    arquivo.write(f'Cognome: {cognome}\n')
    arquivo.write(f'Index: {index}\n')
    arquivo.write(f'Shorten: {shorten}\n')

    
        
   





