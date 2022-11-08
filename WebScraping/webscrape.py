import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv


url = 'http://quotes.toscrape.com/'
#all_quotes = solve the problem of saving the information multiple times.

def get_page(url):
    #open the connection
    uClient = uReq(url)
    #read the connection and store it somewhere
    page_html = uClient.read()
    #Close connection
    uClient.close()
    #parse from the page content to html
    page_soup = soup(page_html,'html.parser')
    return page_soup


def get_information(page_soup):
    containers = page_soup.findAll('div',{'class':'quote'})
    quotes = []
    authors = []
    # Save all the quotes and authors found on lists
    for container in containers:
        quote = container.span.text
        print('Quote:'+ quote)
        quotes.append(quote)
        container_author = container.findAll('small',{'class':'author'})
        author = container_author[0].text
        print('Author: '+author)
        authors.append(author)   
    
    return quotes, authors
        
   
def save_information(quotes, authors):
    filename = 'quotes.csv'
    with open (filename,'a', newline= '\n') as csvfile:
        fieldnames = ['Quotes', 'Authors']
        writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
        writer.writeheader()
        for q,a in zip(quotes, authors):
            writer.writerow({'Quotes': q, 'Authors': a})
     
        
def get_next_page(page_soup):
    page = page_soup.find('ul',{'class':'pager'})
    url = 'http://quotes.toscrape.com/'+str(page.find('li',{'class':'next'}).find('a')['href'])
    return url


#Run the webscraping Script
page = get_page(url)
for i in range(len(page)):
    print(f" page: {len(page)}")
    print('inside the loop')
    quotes, authors =  get_information(page)
    save_information(quotes, authors)
    url = get_next_page(page)
    print(url)
    page = get_page(url)
    
    