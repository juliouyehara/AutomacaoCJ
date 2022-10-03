import pandas as pd
import datetime
from datetime import timedelta

df = pd.read_csv('data.csv', sep=',')
df['Purchasing_Document'] = pd.to_numeric(df['Purchasing_Document'])
df_analise = df[['Gross_Order_Value', 'New Date Payment', 'Purchasing_Document']]
df_analise = df_analise.fillna(0)
df_analise = df_analise[df_analise['New Date Payment'] == 0]
df_analise = df_analise.reset_index(drop=True)

lista = []
lista_index_maior_10 = []
lista_valor_maior_10 = []
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
lista_g8 = []
lista_g9 = []
lista_g10 = []
lista_g11 = []
lista_g12 = []
lista_g13 = []
lista_g14 = []
lista_g15 = []
lista_g16 = []
lista_g17 = []
lista_g18 = []
lista_g19 = []
lista_g20 = []
lista_g21 = []
lista_g22 = []
lista_g23 = []
lista_g24 = []
lista_g25 = []
lista_g26 = []
lista_g27 = []
lista_g28 = []
lista_g29 = []
lista_g30 = []
lista_g31 = []
lista_g32 = []
lista_g33 = []
lista_g34 = []
lista_g35 = []
lista_g36 = []
lista_g37 = []
lista_g38 = []
lista_g39 = []
lista_g40 = []
lista_g41 = []
lista_g42 = []
lista_g43 = []
lista_g44 = []
lista_g45 = []
lista_g46 = []
lista_g47 = []
lista_g48 = []
lista_g49 = []
lista_g50 = []

lista_data1 = []
lista_data2 = []
lista_data3 = []
lista_data4 = []
lista_data5 = []
lista_data6 = []
lista_data7 = []
lista_data8 = []
lista_data9 = []
lista_data10 = []
lista_data11 = []
lista_data12 = []
lista_data13 = []
lista_data14 = []
lista_data15 = []
lista_data16 = []
lista_data17 = []
lista_data18 = []
lista_data19 = []
lista_data20 = []
lista_data21 = []
lista_data22 = []
lista_data23 = []
lista_data24 = []
lista_data25 = []
lista_data26 = []
lista_data27 = []
lista_data28 = []
lista_data29 = []
lista_data30 = []
lista_data31 = []
lista_data32 = []
lista_data33 = []
lista_data34 = []
lista_data35 = []
lista_data36 = []
lista_data37 = []
lista_data38 = []
lista_data39 = []
lista_data40 = []
lista_data41 = []
lista_data42 = []
lista_data43 = []
lista_data44 = []
lista_data45 = []
lista_data46 = []
lista_data47 = []
lista_data48 = []
lista_data49 = []
lista_data50 = []

n = 1
soma = 0
# try:

for i in range(len(df_analise['Gross_Order_Value'])):

    if df_analise['Gross_Order_Value'][i] > 10000000:
        x = df_analise['Gross_Order_Value'][i] / 10000000
        print(x)
        controle_pn = str(x).split('.')[0]
        controle_pn = int(controle_pn)
        controle_sn = '0.' + str(x).split('.')[-1]
        controle_sn = float(controle_sn)

        if controle_sn >= 0.3:
            resultado = df_analise['Gross_Order_Value'][i] / controle_pn + 1
            for n in range(controle_pn + 1):
                lista_index_maior_10.append(i)
                lista_valor_maior_10.append(resultado)
                if len(lista_data_maior_10) == 0:
                    lista_data_maior_10.append(datetime.date.today())
                else:
                    lista_data_maior_10.append(lista_data_maior_10[-1] + timedelta(7))

        elif controle_sn < 0.3:
            resultado = df_analise['Gross_Order_Value'][i] / controle_pn
            for n in range(controle_pn):
                lista_index_maior_10.append(i)
                lista_valor_maior_10.append(resultado)
                if len(lista_data_maior_10) == 0:
                    lista_data_maior_10.append(datetime.date.today())
                else:
                    lista_data_maior_10.append(lista_data_maior_10[-1] + timedelta(7))
        else:
            valor = df_analise['Gross_Order_Value'][i]
            lista_index_maior_10.append(i)
            lista_valor_maior_10.append(valor)
            if len(lista_data_maior_10) == 0:
                lista_data_maior_10.append(datetime.date.today())
            else:
                lista_data_maior_10.append(lista_data_maior_10[-1] + timedelta(7))

if lista_index_maior_10 != 0:
    for i in range(len(lista_index_maior_10)):
        dict = {}
        valor = lista_valor_maior_10[i]
        index_10 = lista_index_maior_10[i]
        po = df_analise.iloc[index_10, df_analise.columns.get_loc('Purchasing_Document')]
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
                    lista_data2.append(lista_data1[-1] + timedelta(7))

                elif controle_index == 2:
                    lista_g3.append(index)
                    lista_data3.append(lista_data2[-1] + timedelta(7))

                elif controle_index == 3:
                    lista_g4.append(index)
                    lista_data4.append(lista_data3[-1] + timedelta(7))

                elif controle_index == 4:
                    lista_g5.append(index)
                    lista_data5.append(lista_data4[-1] + timedelta(7))

                elif controle_index == 5:
                    lista_g6.append(index)
                    lista_data6.append(lista_data5[-1] + timedelta(7))

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
                lista_data1.append(lista_data_maior_10[-1] + timedelta(7))
            else:
                lista_data1.append(datetime.date.today())

        elif len(lista_controle) == 1:
            lista_g2.append(i)
            if len(lista_data1) != 0:
                lista_data2.append(lista_data1[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 2:
            lista_g3.append(i)
            if len(lista_data2) != 0:
                lista_data3.append(lista_data2[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 3:
            lista_g4.append(i)
            if len(lista_data3) != 0:
                lista_data4.append(lista_data3[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 4:
            lista_g5.append(i)
            if len(lista_data4) != 0:
                lista_data5.append(lista_data4[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 5:
            lista_g6.append(i)
            if len(lista_data5) != 0:
                lista_data6.append(lista_data5[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 6:
            lista_g7.append(i)
            if len(lista_data6) != 0:
                lista_data7.append(lista_data6[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 7:
            lista_g8.append(i)
            if len(lista_data7) != 0:
                lista_data8.append(lista_data7[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 8:
            lista_g9.append(i)
            if len(lista_data8) != 0:
                lista_data9.append(lista_data8[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 9:
            lista_g10.append(i)
            if len(lista_data9) != 0:
                lista_data10.append(lista_data9[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 10:
            lista_g11.append(i)
            if len(lista_data10) != 0:
                lista_data11.append(lista_data10[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 11:
            lista_g12.append(i)
            if len(lista_data11) != 0:
                lista_data12.append(lista_data11[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 12:
            lista_g13.append(i)
            if len(lista_data12) != 0:
                lista_data13.append(lista_data12[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 13:
            lista_g14.append(i)
            if len(lista_data13) != 0:
                lista_data14.append(lista_data13[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 14:
            lista_g15.append(i)
            if len(lista_data14) != 0:
                lista_data15.append(lista_data14[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 15:
            lista_g16.append(i)
            if len(lista_data15) != 0:
                lista_data16.append(lista_data15[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 16:
            lista_g17.append(i)
            if len(lista_data16) != 0:
                lista_data17.append(lista_data16[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 17:
            lista_g18.append(i)
            if len(lista_data17) != 0:
                lista_data18.append(lista_data17[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 18:
            lista_g19.append(i)
            if len(lista_data18) != 0:
                lista_data19.append(lista_data18[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 19:
            lista_g20.append(i)
            if len(lista_data19) != 0:
                lista_data20.append(lista_data19[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 20:
            lista_g21.append(i)
            if len(lista_data20) != 0:
                lista_data21.append(lista_data20[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 21:
            lista_g22.append(i)
            if len(lista_data21) != 0:
                lista_data22.append(lista_data21[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 22:
            lista_g23.append(i)
            if len(lista_data22) != 0:
                lista_data23.append(lista_data22[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 23:
            lista_g24.append(i)
            if len(lista_data23) != 0:
                lista_data24.append(lista_data23[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 24:
            lista_g25.append(i)
            if len(lista_data24) != 0:
                lista_data25.append(lista_data24[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 25:
            lista_g26.append(i)
            if len(lista_data25) != 0:
                lista_data26.append(lista_data25[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 26:
            lista_g27.append(i)
            if len(lista_data26) != 0:
                lista_data27.append(lista_data26[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 27:
            lista_g28.append(i)
            if len(lista_data27) != 0:
                lista_data28.append(lista_data27[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 28:
            lista_g29.append(i)
            if len(lista_data28) != 0:
                lista_data29.append(lista_data28[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 29:
            lista_g30.append(i)
            if len(lista_data29) != 0:
                lista_data30.append(lista_data29[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 30:
            lista_g31.append(i)
            if len(lista_data30) != 0:
                lista_data31.append(lista_data30[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 31:
            lista_g32.append(i)
            if len(lista_data31) != 0:
                lista_data32.append(lista_data31[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 32:
            lista_g33.append(i)
            if len(lista_data32) != 0:
                lista_data33.append(lista_data32[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 33:
            lista_g34.append(i)
            if len(lista_data33) != 0:
                lista_data34.append(lista_data33[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 34:
            lista_g35.append(i)
            if len(lista_data34) != 0:
                lista_data35.append(lista_data34[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 35:
            lista_g36.append(i)
            if len(lista_data35) != 0:
                lista_data36.append(lista_data35[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 36:
            lista_g37.append(i)
            if len(lista_data36) != 0:
                lista_data37.append(lista_data36[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 37:
            lista_g38.append(i)
            if len(lista_data37) != 0:
                lista_data38.append(lista_data37[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 38:
            lista_g39.append(i)
            if len(lista_data38) != 0:
                lista_data39.append(lista_data38[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 39:
            lista_g40.append(i)
            if len(lista_data39) != 0:
                lista_data40.append(lista_data39[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 40:
            lista_g41.append(i)
            if len(lista_data40) != 0:
                lista_data41.append(lista_data40[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 41:
            lista_g42.append(i)
            if len(lista_data41) != 0:
                lista_data42.append(lista_data41[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 42:
            lista_g43.append(i)
            if len(lista_data42) != 0:
                lista_data43.append(lista_data42[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 43:
            lista_g44.append(i)
            if len(lista_data43) != 0:
                lista_data44.append(lista_data43[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 44:
            lista_g45.append(i)
            if len(lista_data44) != 0:
                lista_data45.append(lista_data44[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 45:
            lista_g46.append(i)
            if len(lista_data45) != 0:
                lista_data46.append(lista_data45[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 46:
            lista_g47.append(i)
            if len(lista_data46) != 0:
                lista_data47.append(lista_data46[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 47:
            lista_g48.append(i)
            if len(lista_data40) != 0:
                lista_data48.append(lista_data47[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 48:
            lista_g49.append(i)
            if len(lista_data48) != 0:
                lista_data49.append(lista_data48[-1] + timedelta(7))
            else:
                pass

        elif len(lista_controle) == 49:
            lista_g50.append(i)
            if len(lista_data49) != 0:
                lista_data450.append(lista_data49[-1] + timedelta(7))
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
lista7 = []
lista8 = []
lista9 = []
lista10 = []
lista11 = []
lista12 = []
lista13 = []
lista14 = []
lista15 = []
lista16 = []
lista17 = []
lista18 = []
lista19 = []
lista20 = []
lista21 = []
lista22 = []
lista23 = []
lista24 = []
lista25 = []
lista26 = []
lista27 = []
lista28 = []
lista29 = []
lista30 = []
lista31 = []
lista32 = []
lista33 = []
lista34 = []
lista35 = []
lista36 = []
lista37 = []
lista38 = []
lista39 = []
lista40 = []
lista41 = []
lista42 = []
lista43 = []
lista44 = []
lista45 = []
lista46 = []
lista47 = []
lista48 = []
lista49 = []
lista50 = []

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

if lista_g7 != 0:
    for i in lista_g7:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista7.append(dict)
    df_final7 = pd.DataFrame(lista7)
    df_final7['Data'] = lista_data7

if lista_g8 != 0:
    for i in lista_g8:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista8.append(dict)
    df_final8 = pd.DataFrame(lista8)
    df_final8['Data'] = lista_data8

if lista_g9 != 0:
    for i in lista_g9:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista9.append(dict)
    df_final9 = pd.DataFrame(lista9)
    df_final9['Data'] = lista_data9

if lista_g10 != 0:
    for i in lista_g10:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista10.append(dict)
    df_final10 = pd.DataFrame(lista10)
    df_final10['Data'] = lista_data10

if lista_g11 != 0:
    for i in lista_g11:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista11.append(dict)
    df_final11 = pd.DataFrame(lista11)
    df_final11['Data'] = lista_data11

if lista_g12 != 0:
    for i in lista_g12:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista12.append(dict)
    df_final12 = pd.DataFrame(lista12)
    df_final12['Data'] = lista_data12

if lista_g13 != 0:
    for i in lista_g13:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista13.append(dict)
    df_final13 = pd.DataFrame(lista13)
    df_final13['Data'] = lista_data13

if lista_g14 != 0:
    for i in lista_g14:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista14.append(dict)
    df_final14 = pd.DataFrame(lista14)
    df_final14['Data'] = lista_data14

if lista_g15 != 0:
    for i in lista_g15:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista15.append(dict)
    df_final15 = pd.DataFrame(lista15)
    df_final15['Data'] = lista_data15

if lista_g16 != 0:
    for i in lista_g16:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista16.append(dict)
    df_final16 = pd.DataFrame(lista16)
    df_final16['Data'] = lista_data16

if lista_g17 != 0:
    for i in lista_g17:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista17.append(dict)
    df_final17 = pd.DataFrame(lista17)
    df_final17['Data'] = lista_data17

if lista_g18 != 0:
    for i in lista_g18:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista18.append(dict)
    df_final18 = pd.DataFrame(lista18)
    df_final18['Data'] = lista_data18

if lista_g19 != 0:
    for i in lista_g19:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista19.append(dict)
    df_final19 = pd.DataFrame(lista19)
    df_final19['Data'] = lista_data19

if lista_g20 != 0:
    for i in lista_g20:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista20.append(dict)
    df_final20 = pd.DataFrame(lista20)
    df_final20['Data'] = lista_data20

if lista_g21 != 0:
    for i in lista_g21:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista21.append(dict)
    df_final21 = pd.DataFrame(lista21)
    df_final21['Data'] = lista_data21

if lista_g22 != 0:
    for i in lista_g22:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista22.append(dict)
    df_final22 = pd.DataFrame(lista22)
    df_final22['Data'] = lista_data22

if lista_g23 != 0:
    for i in lista_g23:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista23.append(dict)
    df_final23 = pd.DataFrame(lista23)
    df_final23['Data'] = lista_data23

if lista_g24 != 0:
    for i in lista_g24:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista24.append(dict)
    df_final24 = pd.DataFrame(lista24)
    df_final24['Data'] = lista_data24

if lista_g25 != 0:
    for i in lista_g25:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista25.append(dict)
    df_final25 = pd.DataFrame(lista25)
    df_final25['Data'] = lista_data25

if lista_g26 != 0:
    for i in lista_g26:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista26.append(dict)
    df_final26 = pd.DataFrame(lista26)
    df_final26['Data'] = lista_data26

if lista_g27 != 0:
    for i in lista_g27:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista27.append(dict)
    df_final27 = pd.DataFrame(lista27)
    df_final27['Data'] = lista_data27

if lista_g28 != 0:
    for i in lista_g28:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista28.append(dict)
    df_final28 = pd.DataFrame(lista28)
    df_final28['Data'] = lista_data28

if lista_g29 != 0:
    for i in lista_g29:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista29.append(dict)
    df_final29 = pd.DataFrame(lista29)
    df_final29['Data'] = lista_data29

if lista_g30 != 0:
    for i in lista_g30:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista30.append(dict)
    df_final30 = pd.DataFrame(lista30)
    df_final30['Data'] = lista_data30

if lista_g31 != 0:
    for i in lista_g31:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista31.append(dict)
    df_final31 = pd.DataFrame(lista31)
    df_final31['Data'] = lista_data31

if lista_g32 != 0:
    for i in lista_g32:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista32.append(dict)
    df_final32 = pd.DataFrame(lista32)
    df_final32['Data'] = lista_data32

if lista_g33 != 0:
    for i in lista_g33:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista33.append(dict)
    df_final33 = pd.DataFrame(lista33)
    df_final33['Data'] = lista_data33

if lista_g34 != 0:
    for i in lista_g34:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista34.append(dict)
    df_final34 = pd.DataFrame(lista34)
    df_final34['Data'] = lista_data34

if lista_g35 != 0:
    for i in lista_g35:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista35.append(dict)
    df_final35 = pd.DataFrame(lista35)
    df_final35['Data'] = lista_data35

if lista_g36 != 0:
    for i in lista_g36:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista36.append(dict)
    df_final36 = pd.DataFrame(lista36)
    df_final36['Data'] = lista_data36

if lista_g37 != 0:
    for i in lista_g37:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista37.append(dict)
    df_final37 = pd.DataFrame(lista37)
    df_final37['Data'] = lista_data37

if lista_g38 != 0:
    for i in lista_g38:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista38.append(dict)
    df_final38 = pd.DataFrame(lista38)
    df_final38['Data'] = lista_data38

if lista_g39 != 0:
    for i in lista_g39:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista39.append(dict)
    df_final39 = pd.DataFrame(lista39)
    df_final39['Data'] = lista_data39

if lista_g40 != 0:
    for i in lista_g40:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista40.append(dict)
    df_final40 = pd.DataFrame(lista40)
    df_final40['Data'] = lista_data40

if lista_g41 != 0:
    for i in lista_g41:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista41.append(dict)
    df_final41 = pd.DataFrame(lista41)
    df_final41['Data'] = lista_data41

if lista_g42 != 0:
    for i in lista_g42:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista42.append(dict)
    df_final42 = pd.DataFrame(lista42)
    df_final42['Data'] = lista_data42

if lista_g43 != 0:
    for i in lista_g43:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista43.append(dict)
    df_final43 = pd.DataFrame(lista43)
    df_final43['Data'] = lista_data43

if lista_g44 != 0:
    for i in lista_g44:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista44.append(dict)
    df_final44 = pd.DataFrame(lista44)
    df_final44['Data'] = lista_data44

if lista_g45 != 0:
    for i in lista_g45:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista45.append(dict)
    df_final45 = pd.DataFrame(lista45)
    df_final45['Data'] = lista_data45

if lista_g46 != 0:
    for i in lista_g46:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista46.append(dict)
    df_final46 = pd.DataFrame(lista46)
    df_final46['Data'] = lista_data46

if lista_g47 != 0:
    for i in lista_g47:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista47.append(dict)
    df_final47 = pd.DataFrame(lista47)
    df_final47['Data'] = lista_data47

if lista_g48 != 0:
    for i in lista_g48:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista48.append(dict)
    df_final48 = pd.DataFrame(lista48)
    df_final48['Data'] = lista_data48

if lista_g49 != 0:
    for i in lista_g49:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista49.append(dict)
    df_final49 = pd.DataFrame(lista49)
    df_final49['Data'] = lista_data49

if lista_g50 != 0:
    for i in lista_g50:
        dict = {}
        valor = df_analise.iloc[i, df_analise.columns.get_loc('Gross_Order_Value')]
        po = df_analise.iloc[i, df_analise.columns.get_loc('Purchasing_Document')]
        dict.update({'Valor': valor})
        dict.update({'Cod': po})
        lista50.append(dict)
    df_final50 = pd.DataFrame(lista50)
    df_final50['Data'] = lista_data50

df_final = pd.concat([df_final0, df_final1, df_final2, df_final3, df_final4, df_final5, df_final6,
                      df_final7, df_final8, df_final9, df_final10, df_final11, df_final12,
                      df_final13, df_final14, df_final15, df_final16, df_final17, df_final18,
                      df_final19, df_final20, df_final21, df_final22, df_final23, df_final24,
                      df_final25, df_final26, df_final27, df_final28, df_final29, df_final30,
                      df_final31, df_final32, df_final33, df_final34, df_final35, df_final36,
                      df_final37, df_final38, df_final39, df_final40, df_final41, df_final42,
                      df_final43, df_final44, df_final45, df_final46, df_final47, df_final48,
                      df_final49, df_final50])
df_final = df_final.reset_index(drop=True)
df_final['Cod'] = pd.to_numeric(df_final['Cod'])

df['New Date Payment'] = df['New Date Payment'].fillna(0)

for i in df_final['Cod']:
    data_final = df_final['Data'][df_final['Cod'] == i]
    df['New Date Payment'][(df['Purchasing_Document'] == i) & (df['New Date Payment'] == 0)] = str(data_final).split()[
        1]
df['New Date Payment'] = pd.to_datetime(df['New Date Payment'])

# except:
# print('Não há novos valores sem data')

