import subprocess
import re
import os
from sys import stdout
import time
import csv


arq = []


def catchArchiveName(text):
    filename = (re.findall(
        'filename=\".+\.\w+\"', text))
    if (filename != []):
        cleanFilename = filename[0].split("=")[1].replace('\"', '')

        return cleanFilename


def sub(tipoId):
    return re.sub('<name>+|</name>|</type>|<type>|<type ref="prev"/>|<index>\[]</index>|<index>|</index>|<decl>|<specifier>.+</specifier>|<range>|<init>|<.+>|<|>|:', "", tipoId)


def catchClassName(unitName):
    name = 'Default'
    nameBracket = (re.findall("<name>\w*</name>", unitName))

    if (nameBracket):
        name = re.sub('<name>|</name>', '', nameBracket[0])

    return name


def catchTypeId(arquivos, posicao, arq, classe, metodo, projeto):

    filename = 'Identifiers.csv'.format(
        nomeProjeto=projeto)

    with open(filename, mode='a') as csv_file:

        fieldnames = ['nome', 'tipo', 'posicao', 'projeto',
                      'arquivo', 'nomeClasse', 'nomeMetodo']
        writer = csv.DictWriter(csv_file, fieldnames)

        codTipo = None
        codId = None
        # arquivoAtual = None
        for a in arquivos:
            # print(a)
            arquivoAtual = catchArchiveName(a)
            if (re.search("<name><name>Map</name>", a) == None):
                # print(a)
                a2 = re.sub('<range>.+|<init>.+|<expr>.+', '', a)

                stringFor = re.findall(
                    ' <name>\w+</name> |<type><name>\w+</name></type>|<name>\w+</name></type>|<type>.+\w+</name>|<type ref="prev"/><name>\w+</name>| <name>\w+</name><r| <name>\w+</name><init>', a)

                if (re.search('<index>', a)):
                    # print("---------",(str(re.findall('\w+</name><index>.+</type>',a))))
                    if (re.findall('\w+</name><index>.+</type>', a)):
                        x = re.findall('<decl>.+\w+</name><index>.+</type>', a)
                        # print("INDEXXXXXXXXXXXXXXXXX")
                        if (len(x) > 0):
                            # print("aqui",x[0])

                            tipo = sub(x[0])
                            # print(tipo)
                            identificador = (re.findall(
                                ' <name>\w+</name> | <name>\w+</name><r| <name>\w+</name><i| <name>\w+</name><p| <name>\w+</name></d| <name>\w+</name><[a-z]+', a))
                            codTipo = True
                            if (len(identificador) > 0):
                                identificador = re.sub(
                                    '<name>|</name>|<r|<i|<p|</d|<[a-z]+', '', identificador[0])
                                # print("ID: ",identificador)
                                codId = True

                    elif (re.findall(' <name>.+\w+</name><index>', a2)):

                        # print(a)

                        certo = re.findall('\w+</name><index>', a)
                        # certo = sub(certo)
                        # print("INDEX22222222")

                        if (len(certo) > 0):
                            certo = sub(certo[0])
                            stringFor.append(certo)

                for tipoId in stringFor:
                    # print("tipoID: ",tipoId, type(tipoId))

                    match = sub(tipoId)

                    if (re.search('</type>|<type>', tipoId)):
                        # print(tipoId)
                        if (re.search('\w+</name><index>.*</type>', a2) == None):
                            # print("----------------------------------------------------------------------------------------------------------",tipoId)
                            tipo = re.findall('\w+</name>.*</type>', tipoId)

                            # tipo = re.sub(' <name>\w+<name> ',"",tipo)

                            if (len(tipo) > 0):
                                tipo = sub(tipo[0])
                                # print("Tipo:",tipo)
                                codTipo = True
                                # tava a antes
                            identificador = (re.findall(
                                ' <name>\w+</name> | <name>\w+</name><r| <name>\w+</name><i| <name>\w+</name><p| <name>\w+</name></d| <name>\w+</name><[a-z]+', a))

                            if (len(identificador) > 0):
                                identificador = re.sub(
                                    '<name>|</name>|<r|<i|<p|</d|<[a-z]+', '', identificador[0])
                                # print("ID: ",identificador)
                                codId = True

                    elif (re.search('<type ref="prev"/>', tipoId)):
                        # print(tipoId)
                        # print("ref tipo: id",match)
                        identificador = match
                        # codTipo = True
                        codId = True

                    if (codId == True and codTipo == True):
                        # print(" ADICIONADO tipo: ", tipo, "id: ",
                        #       identificador, "classe: ", classe)
                        # print(a)
                        if (metodo):
                            metodo = metodo.replace("\"", '')
                        writer.writerow({'nome': identificador, 'tipo': tipo, 'posicao': posicao, 'projeto': arq,
                                        'arquivo': arquivoAtual, 'nomeClasse': classe, 'nomeMetodo': metodo})

                        codId = False
                        codTipo = False


def run(arq):
    # print(arq)
    identificadoresGeraisComClasse = subprocess.Popen('srcml --xpath "//src:class " {}'.format(
        arq), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    identificadoresGeraisComClasse = identificadoresGeraisComClasse.stdout.read()
    identificadoresGeraisComClasse = identificadoresGeraisComClasse.decode(
        'utf-8')
    identificadoresGeraisComClasse = identificadoresGeraisComClasse.split(
        "</unit>")
    tamanhoString = len(identificadoresGeraisComClasse)
    # print(identificadoresGeraisComClasse)
    # print(identificadoresGeraisComClasse)
    # identificadoresGeraisComClasse[0] = re.sub('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',"",identificadoresGeraisComClasse[0])
    # print(re.match('</name>',identificadoresGeraisComClasse[0]) , "--",arq)
    # identificadoresGeraisComClasse = identificadoresGeraisComClasse.decode('utf-8').split("\n")

    for i in range(tamanhoString):
        # print("---------------")
        # print(identificadoresGeraisComClasse[i])
        # print("---------------FIM DA CLASSE")
        #     ids = str(ids)
        fileId = open("classeXpath.xml", "w")
        if (i != 0):

            fileId.write(
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
            fileId.write(
                '\n<unit xmlns="http://www.srcML.org/srcML/src" revision="1.0.0" url=".">')

        identificadoresGeraisComClasse[i] = re.sub(
            'item="\d*"| item="\d* " ', " ", identificadoresGeraisComClasse[i])
        fileId.write(identificadoresGeraisComClasse[i])
        fileId.write("\n</unit></unit>")
        fileId.close()
        nomefunc = None

        # print(identificadoresGeraisComClasse[i])

        # atributo = subprocess.Popen('srcml --xpath "//src:decl " classeXpath.xml', shell=True,stdout=subprocess.PIPE)
        # atributo = atributo.stdout.read()
        # atributo = atributo.decode('utf-8')
        # print(atributo)

        # nome da classe
        nomeClasse = subprocess.Popen('srcml --xpath "//src:class/src:name" classeXpath.xml',
                                      shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        nomeClasse = nomeClasse.stdout.read()
        nomeClasse = nomeClasse.decode('utf-8')
        if (nomeClasse != '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<unit xmlns="http://www.srcML.org/srcML/src" revision="1.0.0"/>\n'):

            nomeClasseUse = catchClassName(nomeClasse)

        nomeClasse = subprocess.Popen('srcml --xpath "//src:class/src:super/src:name" classeXpath.xml',
                                      shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        nomeClasse = nomeClasse.stdout.read()
        nomeClasse = nomeClasse.decode('utf-8')
        if (nomeClasse != '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<unit xmlns="http://www.srcML.org/srcML/src" revision="1.0.0"/>\n'):
            nomeClasseUse = catchClassName(nomeClasse)

        nomeClasse = subprocess.Popen('srcml --xpath "//src:class/src:annotation/src:name" classeXpath.xml',
                                      shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        nomeClasse = nomeClasse.stdout.read()
        nomeClasse = nomeClasse.decode('utf-8')
        if (nomeClasse != '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<unit xmlns="http://www.srcML.org/srcML/src" revision="1.0.0"/>\n'):
            nomeClasseUse = catchClassName(nomeClasse)

        # print(nomeClasseUse)

        # todos ids atributos
        identificadoresAtributo = subprocess.Popen(
            'srcml --xpath "//src:decl[not(ancestor::src:for) and not(ancestor::src:while) and not(ancestor::src:do) and not(ancestor::src:if_stmt) and not(ancestor::src:switch) and not(ancestor::src:case) and not(ancestor::src:function) and not(ancestor::src:parameter_list)] " classeXpath.xml', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        identificadoresAtributo = identificadoresAtributo.stdout.read()

        identificadoresAtributo = identificadoresAtributo.decode(
            'utf-8').split("</unit>")
        catchTypeId(identificadoresAtributo, "Atributo",
                    arq, nomeClasseUse, nomefunc, arq)
        # for ids in identificadoresAtributo:
        #     print(ids)

        identificadoresGeraisFuncao = subprocess.Popen(
            'srcml --xpath "//src:function " classeXpath.xml', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        identificadoresGeraisFuncao = identificadoresGeraisFuncao.stdout.read()
        identificadoresGeraisFuncao = identificadoresGeraisFuncao.decode(
            'utf-8')
        identificadoresGeraisFuncao = identificadoresGeraisFuncao.split(
            "</unit>")
        tamanhoFunc = len(identificadoresGeraisFuncao)
        # for func in identificadoresGeraisFuncao:
        #     print(func)
        #     print("--------")
        for j in range(tamanhoFunc):

            # print(identificadoresGeraisFuncao[j])
            fileFunc = open("funcXpath.xml", "w")

            if (j != 0):

                fileFunc.write(
                    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
                fileFunc.write(
                    '\n<unit xmlns="http://www.srcML.org/srcML/src" revision="1.0.0" url=".">')
            # print(identificadoresGeraisFuncao[j])

            identificadoresGeraisFuncao[j] = re.sub(
                'item="\d*"| item="\d* " ', " ", identificadoresGeraisFuncao[j])
            # identificadoresGeraisFuncao[j] = re.sub('item="\d*">', ">",identificadoresGeraisFuncao[j])

            fileFunc.write(identificadoresGeraisFuncao[j])
            fileFunc.write("\n</unit></unit>")
            fileFunc.close()
            # print(identificadoresGeraisFuncao[j])

            # nome da funcao
            nomefunc = subprocess.Popen(
                'srcml --xpath "string(//src:function/src:name) " funcXpath.xml', shell=True, stdout=subprocess.PIPE)
            nomefunc = nomefunc.stdout.read()
            nomefunc = nomefunc.decode('utf-8')

            # variaveis dentro de uma funcao
            idVariavel = subprocess.Popen(
                'srcml --xpath "//src:decl_stmt[ancestor::src:function[1]] " funcXpath.xml', shell=True, stdout=subprocess.PIPE)
            idVariavel = idVariavel.stdout.read()
            idVariavel = idVariavel.decode('utf-8').split("</unit>")

            catchTypeId(idVariavel, "Variavel", arq,
                        nomeClasseUse, nomefunc, arq)

            # if
            identificadorIf = subprocess.Popen(
                'srcml --xpath "//src:decl[ancestor::src:if_stmt[1]]" funcXpath.xml', shell=True, stdout=subprocess.PIPE)
            identificadorIf = identificadorIf.stdout.read()
            identificadorIf = identificadorIf.decode('utf-8').split("\n")

            catchTypeId(identificadorIf, "if", arq,
                        nomeClasseUse, nomefunc, arq)

            # for
            identificadorFor = subprocess.Popen(
                'srcml --xpath "//src:decl_stmt[ancestor::src:for[1]]" funcXpath.xml', shell=True, stdout=subprocess.PIPE)
            identificadorFor = identificadorFor.stdout.read()
            identificadorFor = identificadorFor.decode('utf-8').split("\n")

            catchTypeId(identificadorFor, "For", arq,
                        nomeClasseUse, nomefunc, arq)

            # while
            identificadorWhile = subprocess.Popen(
                'srcml --xpath "//src:decl[ancestor::src:while[1]]" funcXpath.xml', shell=True, stdout=subprocess.PIPE)
            identificadorWhile = identificadorWhile.stdout.read()
            identificadorWhile = identificadorWhile.decode('utf-8').split("\n")

            catchTypeId(identificadorWhile, "while",
                        arq, nomeClasseUse, nomefunc, arq)

            # do
            identificadorDo = subprocess.Popen(
                'srcml --xpath "//src:decl[ancestor::src:do[1]]" funcXpath.xml', shell=True, stdout=subprocess.PIPE)
            identificadorDo = identificadorDo.stdout.read()
            identificadorDo = identificadorDo.decode('utf-8').split("\n")

            catchTypeId(identificadorDo, "Do", arq,
                        nomeClasseUse, nomefunc, arq)

            # switch
            identificadorswitch = subprocess.Popen(
                'srcml --xpath "//src:decl[ancestor::src:switch[1]]" funcXpath.xml', shell=True, stdout=subprocess.PIPE)
            identificadorswitch = identificadorswitch.stdout.read()
            identificadorswitch = identificadorswitch.decode(
                'utf-8').split("\n")

            catchTypeId(identificadorswitch, "switch",
                        arq, nomeClasseUse, nomefunc, arq)

            # case
            identificadorCase = subprocess.Popen(
                'srcml --xpath "//src:decl[ancestor::src:case[1]]" funcXpath.xml', shell=True, stdout=subprocess.PIPE)
            identificadorCase = identificadorCase.stdout.read()
            identificadorCase = identificadorCase.decode('utf-8').split("\n")

            catchTypeId(identificadorCase, "Case",
                        arq, nomeClasseUse, nomefunc, arq)


def main():

    arq = os.listdir()
    # print(arq)
    for arquivo in arq:

        if (re.search(".xml", arquivo) and arquivo != "classeXpath.xml" and arquivo != "funcXpath.xml"):

            filename = 'Identifiers.csv'.format(
                nomeProjeto=arquivo)
            with open(filename, mode='a') as csv_file:

                fieldnames = ['nome', 'tipo', 'posicao',
                              'projeto', 'arquivo', 'nomeClasse', 'nomeMetodo']

                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

            # print(arquivo)
            run(arquivo)


if __name__ == '__main__':

    main()

