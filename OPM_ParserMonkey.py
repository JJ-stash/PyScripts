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

    page = 0
    for image in images:
    	page += 1
        name = f'Page {page}'
        link = image['src']
        with open(name + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)



def pdfmaker(folder):
	pdf = FPDF(unit='mm')
	pdf.set_auto_page_break(0)

	os.chdir(os.path.join(os.getcwd(), folder))
	all_files = os.listdir()
	all_images = [f for f in all_files if not f.endswith('.pdf')]
	
	all_images = sorted(all_images, key=lambda x: float(x[4:-4]))
	print(all_images)

	for img in all_images:
		pdf.add_page()
		pdf.image(img, 0, 0, w=210, h=297)

	pdf.output(f" OPM Chapter {chapter}.pdf")
	print("Done Sewing")



#imagedown(url, 'OPM')
#pdfmaker('OPM')
