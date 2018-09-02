import requests
import pandas as pd


import csv
import os.path


f = open('./data/kospi_code.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
code_list = list(rdr)

f.close()

for i in range(len(code_list)):
    code = code_list[i][0].replace(".KS", '')
    file_name = "./data/finance/%s.csv" % (code)

    if os.path.isfile(file_name):
        print("skip " + code)
    else:
        url = "http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd=%s&fin_typ=0&freq_typ=Y" % (code)
        print(code)

        html = requests.get(url).text

        html = html.replace('\t', '')
        html = html.replace('\n', '')
        html = html.replace('\r', '')

        html = html.replace("<th class=\"bg r01c02 endLine line-bottom\"colspan=\"8\">연간</th></tr><tr>", "")
        html = html.replace("<span class='span-sub'>(IFRS연결)</span>", "")

        for year in range(2005, 2025):
            html = html.replace(str(year) + "/12", str(year))
            #html = html.replace("(E)", '')

        df_list = pd.read_html(html, header=0 , index_col=0)
        df = df_list[0]

        df.to_csv(file_name, mode='w')


