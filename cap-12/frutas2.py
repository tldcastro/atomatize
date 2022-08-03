import openpyxl

book = openpyxl.load_workbook('Planilha de preços frutas.xlsx')

# selecionado pg

frutas_page = book['Frutas']

# imprimindo dados de cada linha
for rows in frutas_page.iter_rows(min_row=2, max_row=5):
    # for cell in rows:
    # print(cell.value)

    # imprimindo na mesma linha
    #print(f'{rows[0].value}, {rows[1].value}, {rows[2].value}')

    # alterando valores
    for cell in rows:
        if cell.value == 'Banana':
            cell.value = 'Banana da Terra'

# Salvando alterações

book.save("Planilha de Frutas Atualizada.xlsx")
