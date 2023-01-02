import pandas as pd

    #Importação do arquivo html
arquivoExportado = 'NovembroCompleto.html'

    #Invocação do método que vai ler o arquivo html e interpretar
arquivoHtml = pd.read_html(arquivoExportado)

    #Vem retornado como um dataframe
analise = arquivoHtml[0]
print(analise)

#Conversão dos dados para uma planilha do excel
##doc: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html

analise.to_excel('Exportação da tabela do arquivo.xlsx')