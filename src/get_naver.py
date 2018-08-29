import requests
import pandas as pd


url = "http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd=035720&fin_typ=0&freq_typ=Y"

html = requests.get(url).text

html = html.replace('<th class="bg r01c02 endLine line-bottom"colspan="8">연간</th>', "")
html = html.replace("<span class='span-sub'>(IFRS연결)</span>", "")
html = html.replace("<span class='span-sub'>(IFRS별도)</span>", "")
html = html.replace("<span class='span-sub'>(GAAP개별)</span>", "")
html = html.replace("<caption class='blind'>주요재무정보</caption>", "")

html = html.replace('\t', '')
html = html.replace('\n', '')
html = html.replace('\r', '')



for year in range(2005, 2025):
    for month in range(6, 13):
        month = "/%02d" % month
        html = html.replace(str(year) + month, str(year))


    for month in range(1, 6):
        month = "/%02d" % month
        html = html.replace(str(year+1) + month, str(year))

    html = html.replace(str(year) + '(E)', str(year))




file = open("result.html",'w')
file.write(html)
file.close()

df_list = pd.read_html(html, index_col='2013')

#df_list = pd.read_html(html, index_col=5)
#print(df_list)

#df = df_list[0]


'''
df_list = pd.read_html(html, index_col='주요재무정보')
df = df_list[0]


print(html)

for year in range(2014, 2015):
    for month in range(6, 13):
        month = "/%02d" % month
        html = html.replace(str(year) + month, str(year))

    for month in range(1, 6):
        month = "/%02d" % month
        html = html.replace(str(year+1) + month, str(year))

    html = html.replace(str(year) + '(E)', str(year))

df_list = pd.read_html(html, index_col='주요재무정보')
df = df_list[0]




def get_financial_statements(code):
    url = "http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd=%s&fin_typ=0&freq_typ=Y" % (code)
    html = requests.get(url).text

    html = html.replace('<th class="bg r01c02 endLine line-bottom"colspan="8">연간</th>', "")
    html = html.replace("<span class='span-sub'>(IFRS연결)</span>", "")
    html = html.replace("<span class='span-sub'>(IFRS별도)</span>", "")
    html = html.replace("<span class='span-sub'>(GAAP개별)</span>", "")
    html = html.replace('\t', '')
    html = html.replace('\n', '')
    html = html.replace('\r', '')

	print(html)

    for year in range(2014, 2015):
        for month in range(6, 13):
            month = "/%02d" % month
            html = html.replace(str(year) + month, str(year))

        for month in range(1, 6):
            month = "/%02d" % month
            html = html.replace(str(year+1) + month, str(year))

        html = html.replace(str(year) + '(E)', str(year))

    df_list = pd.read_html(html, index_col='주요재무정보')
    df = df_list[0]

    return df


df = get_financial_statements('035720')
print(df)
'''

