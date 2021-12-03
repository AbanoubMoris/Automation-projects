from GetProductsImg.GetImage import ImageUrl

with ImageUrl() as bot:
    #bot.land_first_page()

    #print()
    from pandas import read_excel

    my_sheet = 'General'  # change it to your sheet name, you can find your sheet name at the bottom left of your excel file
    file_name = 'products.xlsx'  # change it to the name of your excel file
    df = read_excel(file_name, sheet_name=my_sheet)


    my_sheet = 'Data'  # change it to your sheet name, you can find your sheet name at the bottom left of your excel file
    file_name = 'products.xlsx'  # change it to the name of your excel file
    df2 = read_excel(file_name, sheet_name=my_sheet)
    i=0
    for productName in df['name']:
        img = bot.fetch_image_urls(str(productName), 1)
        df2.loc[i, 'image'] = img.pop()
        i+=1
        if i>100:
            break

    df2.to_csv("AllDetails.csv", index=False)
    print(df2['image'][0])

