import os
import requests
from fpdf import FPDF
from bs4 import BeautifulSoup

chapter = input("Chapter Number: ")
url = f"https://read-one-punchman.com/comic/one-punch-man-chapter-{chapter}/"

def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        name = image['alt']
        link = image['src']
        with open(name + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)

def pdfmaker(folder):
	pdf = FPDF()
	pdf.set(auto_page_break(1))

	img_list = [x for x in os.listdir(folder)]

	for img in img_list:
		pdf.add_page()
		pdf.image(img)

	pdf.output(f" OPM Chapter {chapter}.pdf")
	print("Done Sewing")

#imagedown(url, 'OPM')
#pdfmaker('OPM')