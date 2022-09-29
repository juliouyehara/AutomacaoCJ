import pandas as pd
import datetime
from datetime import timedelta

df = pd.read_excel('testecj.xlsx')
df['Purchasing_Document'] = pd.to_numeric(df['Purchasing_Document'])
df_analise = df[['Gross_Order_Value', 'New Date Payment', 'Purchasing_Document']]

df_analise = df_analise.fillna(0)
df_analise = df_analise[df_analise['New Date Payment'] == 0]
df_analise = df_analise.reset_index(drop=True)

lista = []
lista_index_maior_10 = []
lista_data_maior_10 = []
lista_data = []
lista_index_n = []
lista_index_g = []
lista_prox_10 = []
lista_controle = []
lista0 = []
lista_g1 = []
lista_g2 = []
lista_g3 = []
lista_g4 = []
lista_g5 = []
lista_g6 = []
lista_g7 = []
lista_data1 = []
lista_data2 = []
lista_data3 = []
lista_data4 = []
lista_data5 = []
lista_data6 = []
lista_data7 = []
n = 1
soma = 0
try:

    for i in range(len(df_analise['Gross_Order_Value'])):

        if df_analise['Gross_Order_Value'][i] > 10000000:
            lista.append(df_analise['Gross_Order_Value'][i])
            lista_index_maior_10.append(i)
            if len(lista_data_maior_10) == 0:
                lista_data_maior_10.append(datetime.date.today())
            else:
                lista_data_maior_10.append(lista_data_maior_10[-1]+timedelta(7))
        else:
            pass

    if lista_index_maior_10 != 0:

        for i in lista_index_maior_10:
            dict = {}
            valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
            po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
            dict.update({'Valor': valor})
            dict.update({'Cod': po})
            lista0.append(dict)

        df_final0 = pd.DataFrame(lista0)
        df_final0['Data'] = lista_data_maior_10

    df_analise = df_analise[~df_analise['Gross_Order_Value'].isin(lista)]
    df_analise = df_analise.reset_index(drop=True)
    for i in range(len(df_analise['Gross_Order_Value'])):

        print(soma)
        if soma > 8000000 and df_analise['Gross_Order_Value'][i] > 1500000:
            lista_index_n.append(i)

            continue
        else:
            if n - len(lista_controle) < 1:
                try:
                    index = lista_index_n[0]
                    soma = soma + df_analise['Gross_Order_Value'][i] + df_analise['Gross_Order_Value'][index]
                    lista_index_n = []
                    n = n + 1
                    controle_index = len(lista_controle)

                    if controle_index == 1:
                        lista_g2.append(index)
                        lista_data2.append(lista_data1[-1]+timedelta(7))

                    elif controle_index == 2:
                        lista_g3.append(index)
                        lista_data3.append(lista_data2[-1]+timedelta(7))

                    elif controle_index == 3:
                        lista_g4.append(index)
                        lista_data4.append(lista_data3[-1]+timedelta(7))

                    elif controle_index == 4:
                        lista_g5.append(index)
                        lista_data5.append(lista_data4[-1]+timedelta(7))

                    elif controle_index == 5:
                        lista_g6.append(index)
                        lista_data6.append(lista_data5[-1]+timedelta(7))

                    print('Soma Index', soma)
                    print('Index n/', i)
                    print('O index é', index)
                except:
                    soma = soma + df_analise['Gross_Order_Value'][i]
                    n = n + 1
            else:
                soma = soma + df_analise['Gross_Order_Value'][i]

            if len(lista_controle) == 0:
                lista_g1.append(i)
                if len(lista_data_maior_10) != 0:
                    lista_data1.append(lista_data_maior_10[-1]+timedelta(7))
                else:
                    lista_data1.append(datetime.date.today())

            elif len(lista_controle) == 1:
                lista_g2.append(i)
                if len(lista_data1) != 0:
                    lista_data2.append(lista_data1[-1]+timedelta(7))
                else:
                    pass

            elif len(lista_controle) == 2:
                lista_g3.append(i)
                if len(lista_data2) != 0:
                    lista_data3.append(lista_data2[-1]+timedelta(7))
                else:
                    pass

            elif len(lista_controle) == 3:
                lista_g4.append(i)
                if len(lista_data3) != 0:
                    lista_data4.append(lista_data3[-1]+timedelta(7))
                else:
                    pass

            elif len(lista_controle) == 4:
                lista_g5.append(i)
                if len(lista_data4) != 0:
                    lista_data5.append(lista_data4[-1]+timedelta(7))
                else:
                    pass

            elif len(lista_controle) == 5:
                lista_g6.append(i)
                if len(lista_data5) != 0:
                    lista_data6.append(lista_data5[-1]+timedelta(7))
                else:
                    pass

            elif len(lista_controle) == 6:
                lista_g7.append(i)
                if len(lista_data6) != 0:
                    lista_data7.append(lista_data6[-1]+timedelta(7))
                else:
                    pass

        if soma > 10000000:
            lista_prox_10.append(soma)
            soma = 0
            lista_controle.append(0)

    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    lista6 = []

    if lista_g1 != 0:

        for i in lista_g1:
            dict = {}
            valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
            po = str(df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')])
            dict.update({'Valor': valor})
            dict.update({'Cod': po})
            lista1.append(dict)
        print(lista)
        df_final1 = pd.DataFrame(lista1)
        df_final1['Data'] = lista_data1

    if lista_g2 != 0:
        for i in lista_g2:
            dict = {}
            valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
            po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
            dict.update({'Valor': valor})
            dict.update({'Cod': po})
            lista2.append(dict)
        df_final2 = pd.DataFrame(lista2)
        df_final2['Data'] = lista_data2

    if lista_g3 != 0:
        for i in lista_g3:
            dict = {}
            valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
            po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
            dict.update({'Valor': valor})
            dict.update({'Cod': po})
            lista3.append(dict)
        print(len(lista_data3))
        df_final3 = pd.DataFrame(lista3)
        print(len(df_final3))
        df_final3['Data'] = lista_data3

    if lista_g4 != 0:
        for i in lista_g4:
            dict = {}
            valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
            po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
            dict.update({'Valor': valor})
            dict.update({'Cod': po})
            lista4.append(dict)
        df_final4 = pd.DataFrame(lista4)
        df_final4['Data'] = lista_data4

    if lista_g5 != 0:
        for i in lista_g5:
            dict = {}
            valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
            po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
            dict.update({'Valor': valor})
            dict.update({'Cod': po})
            lista5.append(dict)
        df_final5 = pd.DataFrame(lista5)
        df_final5['Data'] = lista_data5

    if lista_g6 != 0:
        for i in lista_g6:
            dict = {}
            valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
            po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
            dict.update({'Valor': valor})
            dict.update({'Cod': po})
            lista6.append(dict)
        df_final6 = pd.DataFrame(lista6)
        df_final6['Data'] = lista_data6

    df_final = pd.concat([df_final0, df_final1, df_final2, df_final3, df_final4, df_final5, df_final6])
    df_final = df_final.reset_index(drop=True)
    df_final['Cod'] = pd.to_numeric(df_final['Cod'])

    df['New Date Payment'] = df['New Date Payment'].fillna(0)

    for i in df_final['Cod']:
        data_final = df_final['Data'][df_final['Cod'] == i]
        df['New Date Payment'][(df['Purchasing_Document'] == i) & (df['New Date Payment'] == 0)] = str(data_final).split()[1]
    df['New Date Payment'] = pd.to_datetime(df['New Date Payment'])

except:
    print('Não há novos valores sem data')
