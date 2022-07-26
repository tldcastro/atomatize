import bs4
import requests

# obs: esse codigo nem sempre funciona, pois, o site da amazon o ve como bot.


def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status
    assert 'id="price"' in res.text
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    print(res.text)

    elems = soup.select('[id="price"]')
    print(elems)
    return elems[0].text.strip()

# pegando imagem ao invés de preço//


def getAmazonImg(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status
    assert 'id="imgThumbs"' in res.text
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    print(res.text)

    elems = soup.select('[id="imgThumbs"] div img')
    print(elems)
    return elems


url = ("https://www.amazon.com.br/Mistborn-Boxed-Set-Well-Ascension/dp/125026717X/?_encoding=UTF8&pd_rd_w=dQxnq&content-id=amzn1.sym.717e1082-1b26-481d-94d5-2a1a46904215&pf_rd_p=717e1082-1b26-481d-94d5-2a1a46904215&pf_rd_r=YX1YMWEYG8W8GMSVYZA1&pd_rd_wg=QI4ox&pd_rd_r=057dc065-f509-45da-8fcf-d01ce127246f&ref_=pd_gw_ci_mcx_mr_hp_atf_m")
#price = getAmazonPrice(url)
img = getAmazonImg(url)
#print("the price is" + price)
