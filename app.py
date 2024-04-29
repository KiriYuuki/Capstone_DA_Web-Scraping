from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.exchange-rates.org/exchange-rate-history/usd-idr')
soup = BeautifulSoup(url_get.content,"html.parser")

#find your right key here
table = soup.find('table', attrs={'class': 'history-rates-data'})

table.find_all("tr")[:5]

rows = table.find_all('a', class_='w')
row_length = len(rows)

table.find_all('a', class_='w')
table.find_all("span", class_='w')

temp = [] #initiating a list 

for i in range(0, row_length):
#insert the scrapping process here
    date = table.find_all('a', class_='w')[i].text.strip()
    rate = table.find_all("span", class_='w')[i].text.strip()
    temp.append((date, rate)) 

temp = temp[::-1]

#change into dataframe
exchange_rate = pd.DataFrame(temp, columns = ("Date", "Exchange Rate"))

#insert data wrangling here
exchange_rate = pd.DataFrame(temp, columns=("Date", "Exchange Rate"))
exchange_rate['Date'] = pd.to_datetime(exchange_rate['Date'])
exchange_rate['Exchange Rate'] = exchange_rate['Exchange Rate'].str.replace('$1 = Rp', '').str.replace(',', '').astype(float)
exchange_rate.set_index('Date', inplace=True)

#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'{exchange_rate["Exchange Rate"].mean().round(2)}' #be careful with the " and ' 

	# generate plot
	ax = exchange_rate.plot(figsize = (11,6)) 
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)