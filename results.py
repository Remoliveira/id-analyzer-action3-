import re 
import pandas as pd
from pyfiglet import Figlet


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
        arquivo = csvEntries.arquivo
        posicao = csvEntries.posicao
    


        idSplit = camelSplit(identificador)
        tipoSplit = camelSplit(tipo)
        # variacao = identificadorTupla[3]
        # print(len(idSplit) , " ", idSplit) 
        
        numeroPalavra = len(idSplit)


        # if(re.search("\D+[a-zA-z]+\d+$",identificador)):
    
        if(re.search("\d$", identificador)):
 
            numFinal = 1

            id = {
                "name": identificador,
                "arquivo":arquivo
            }
      
            kings.append(id)
        else:
            numFinal = 0
        
        if(re.search("\d+.*\D+$",identificador)):
            # print("id com numero no meio: ",identificador, "tipo: ",tipo, projeto)
            numMeio = 1
            id = {
                "name": identificador,
                "arquivo":arquivo
            }
            median.append(id)
        else:
            numMeio = 0
        
        if(identificador.casefold() == tipo.casefold()):
            # print("id == tipo ", identificador, "--", tipo)
            id = {
                "name": identificador,
                "arquivo":arquivo
            }
            ditto.append(id)
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
                        id = {
                            "name": identificador,
                            "arquivo":arquivo
                        }
                        cognome.append(id)
                        tipoNoId = 1

                    elif(len(tipoSplit)> len(idSplit)):
                        # print(identificador,"-----",tipo, projeto)
                        id = {
                            "name": identificador,
                            "arquivo":arquivo
                        }
                        diminutive.append(id)
                        idNoTipo = 1

          
                
        letraInicioTipo = 0
        if(len(identificador) == 1):

            idUmaLetra = 1
            id = {
                "name": identificador,
                "arquivo":arquivo
            }
            index.append(id)
            if(len(tipo)>0):
      
                tipoLower = tipo[0].lower()
      
                if(identificador == tipoLower):
             
                    id = {
                        "name": identificador,
                        "arquivo":arquivo
                    }
                    shorten.append(id)
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

    # kings = ' '.join(kings)
    # median = ' '.join(median)
    # ditto = ' '.join(ditto)
    # diminutive = ' '.join(diminutive)
    # cognome = ' '.join(cognome)
    # index = ' '.join(index)
    # shorten = ' '.join(shorten)

    f = Figlet(font='slant')
    x = f.renderText('Id. Analyzer')
    arquivo.write(x)   

    if(len(kings) > 0):
        arquivo.write(f'Kings:\n')
        for id in kings:  
            arquivo.write(id["name"])
            arquivo.write(" - ")
            arquivo.write(id["arquivo"])
            arquivo.write("\n")

        arquivo.write("\n")
    


    if(len((median)) >0 ):
        arquivo.write(f'Median:\n')
    
        for id in median:  
            arquivo.write(id["name"])
            arquivo.write(" - ")
            arquivo.write(id["arquivo"])
            arquivo.write("\n")
            
            arquivo.write("\n")
        
    
   
    if(len(ditto) > 0):
        arquivo.write(f'Ditto:\n')
        for id in ditto:  
            arquivo.write(id["name"])
            arquivo.write(" - ")
            arquivo.write(id["arquivo"])
            arquivo.write("\n")
        
        arquivo.write("\n")

    
    if(len(cognome) > 0):
        arquivo.write(f'Cognome:\n')
        for id in cognome:  
            arquivo.write(id["name"])
            arquivo.write(" - ")
            arquivo.write(id["arquivo"])
            arquivo.write("\n")

        arquivo.write("\n")

    if(len(index) > 0):
        arquivo.write(f'Index:\n')
        for id in index:  
            arquivo.write(id["name"])
            arquivo.write(" - ")
            arquivo.write(id["arquivo"])
            arquivo.write("\n")

        arquivo.write("\n")

    
    if(len(shorten) >0):
        arquivo.write(f'Shorten:\n')
        for id in shorten:  
            arquivo.write(id["name"])
            arquivo.write(" - ")
            arquivo.write(id["arquivo"])
            arquivo.write("\n")

        arquivo.write("\n")



    
        
   





