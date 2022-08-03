from cgitb import strong, text
from cmath import e
from numpy import source
import requests
import bs4
from bs4 import BeautifulSoup
import openpyxl

# este script mistura web scraping com planilha excel
# excel criando planilha
book = openpyxl.Workbook()
print(book.sheetnames)
sheet = book.active
# mudando o nome de sheet para 'Planilha com os dados do IMDb Top 250 Movies'
sheet.title = 'Planilha com os dados do IMDb Top 250 Movies'
sheet.append(['Movie Rank', 'Movie Name', 'Year of Relase', 'IMDB Rating'])

# web scraping


def getMoviesList():
    source = requests.get('https://www.imdb.com/chart/top')
    source.raise_for_status()
    soup = BeautifulSoup(source.text, "html.parser")
    movies = soup.find('tbody', class_='lister-list').find_all('tr')

    for i, movie in enumerate(movies, 1):

        name = movie.find('td', class_='titleColumn').a.text
        assert name != ''

        rank = i
        assert rank

        year = movie.find('td', class_='titleColumn').span.text.strip('()')
        assert year

        rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
        assert rating

        yield name, rank, year, rating
        sheet.append([rank, name, year, rating])
        book.save('IMDb Movie Ratings.xlsx')  # salvando a planilha excel


alldata = list(getMoviesList())
# print(alldata[0][3])  # selecionando apenas um
for data in alldata:
    print(data)


#book.save('IMDb Movie Ratings.xlsx')#


#movies = soup.find('tbody', class_='lister-list')
#url = requests.get('https://www.imdb.com/chart/moviemeter')
#movie = getImdb(url)

#rows = list(funcao())
# for row in rows:
# cell_name.value = row[0] #name
# cell_rank.value = row[1] #rank
# cell_rating.value = row[2] #rating
