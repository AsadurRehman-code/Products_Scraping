import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/scrape/<string:product>')
def scrape(product):
    # open the browser
    browser = webdriver.Chrome()

    # load the webpage
    browser.get(f'https://www.daraz.pk/catalog/?q={product}')

    titles = browser.find_elements(By.CLASS_NAME, 'title--wFj93')
    prices = browser.find_elements(By.CLASS_NAME, 'price--NVB62')

    result_list = []

    for title, price in zip(titles, prices):
        title_text = title.text
        price_text = price.text

        # Remove all non-digit characters except decimal point
        price_value = re.sub(r'[^\d.]', '', price_text)
        price_value = price_value.replace('.', '')
        price_value = int(price_value)
        
        if product == 'Lays Yogurt and Herb Rs.60' and ("Lays Yogurt and Herb" in title_text) and  (55 <= price_value <= 60):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Nestle Pure Life 5L' and (225 <= price_value <= 235):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Pepsi 500ml Bottle' and ("Pepsi" in title_text) and (130 <= price_value <= 140):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Sting 500ml Energy Drink' and ("Sting" in title_text) and (130 <= price_value <= 140):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lays Masala Rs.60' and ("Lays Masala" in title_text) and (55 <= price_value <= 60):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lays French Cheese Rs.60'  and ("Lays French Cheese" in title_text) and (55 <= price_value <= 60):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Mountain Dew Drink 500ml' and ("Mountain Dew Drink" in title_text) and (130 <= price_value <= 140):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lays French Cheese 14 g' and ("Lays French Cheese" in title_text) and (15 <= price_value <= 20):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lays Salt rs 40' and ("Lays" in title_text) and (35 <= price_value <= 40):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Rio Strawberry Half Roll' and ("Rio Strawberry" in title_text) and (35 <= price_value <= 40):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Aquafina 500ml' and ("Aquafina 500ml" in title_text) and (70 <= price_value <= 80):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Kurkure Chatni Chaska 20' and ("Kurkure Chatni Chaska" in title_text) and (10 <= price_value <= 20):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lays Masala 14' and ("Lays" in title_text) and (15 <= price_value <= 20):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lays Salt 14' and ("Lays" in title_text) and (15 <= price_value <= 20):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Ariel Original Detergent' and ("Ariel" in title_text) and (315 <= price_value <= 330):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Rossmoor Baking Powder 50gm' and ("Baking Powder" in title_text) and (180 <= price_value <= 210):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Bonus Tristar Detergent' and ("Bonus" in title_text) and (200 <= price_value <= 230):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Brite Maximum Power' and ("Brite" in title_text) and (280 <= price_value <= 300):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Capri Pack of 3 Peach Soap' and ("Capri" in title_text) and (320 <= price_value <= 360):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Colgate Maximum Cavity Protection Toothpaste' and ("Colgate" in title_text) and (135 <= price_value <= 150):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'English Prickly Heat Powder' and ("English Prickly Heat Powder" in title_text) and (260 <= price_value <= 280):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Ensure Chocolate' and ("ENSURE" in title_text) and (2000 <= price_value <= 2260):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Ensure Vanilla 850gm' and ("Vanilla" in title_text) and (3700 <= price_value <= 3900):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Express Power 500g' and ("Express Power 500g" in title_text) and (220 <= price_value <= 240):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Himalaya Moisturizing Aloe Vera Face Wash 50 ml' and ("Himalaya" in title_text) and (260 <= price_value <= 280):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Laziza Ras Malai Mix 75g' and ("Laziza Ras Malai" in title_text) and (190 <= price_value <= 230):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lemon Max Long Bar Double' and ("Lemon Max Long Bar Double" in title_text) and (180<= price_value <= 200):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lifebuoy Soap' and ("Lifebuoy Total" in title_text) and (85 <= price_value <= 95):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == "L'Oreal Paris - LOreal Elvive Color Protect Conditioner 175 ML" and ("L'Oreal Paris" in title_text) and (360 <= price_value <= 380):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'PAPRIKA POWDER 25 GRAM' and ("PAPRIKA POWDER" in title_text) and (150 <= price_value <= 200):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Saeed Ghani Ubtan Face Wash (60ml)' and ("Ubtan" in title_text) and (190 <= price_value <= 210):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == "Saniplast Fabric Bandage 20's" and ("Saniplast" in title_text) and (80<= price_value <= 90):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == "Saniplast Spot Bandage 20's" and ("Saniplast" in title_text) and (60 <= price_value <= 70):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Garlic Chilli Sauce Family Pack 800gm' and ("Garlic Chilli Sauce" in title_text) and (390 <= price_value <= 410):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Tomato Ketchup Family Pack 800gm' and ("Tomato Ketchup" in title_text) and (390 <= price_value <= 410):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == "SunsilkConditionerBlack & Shine" and ("SunsilkConditionerBlack" in title_text) and (300<= price_value <= 340):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == "New Tapall Green Tea Tropical Peach 30 Bags" and ("New Tapall Green Tea " in title_text) and (250 <= price_value <= 300):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'vatika dandruff guard lemon' and ("vatika dandruff" in title_text) and (640 <= price_value <= 670):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == "Young's Mayonnaise 500ml" and ("Young's Mayonnaise 500ml" in title_text) and (330 <= price_value <= 370):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == "Youngs Sandwich Spread 200ml Pouch" and ("Youngs Sandwich Spread" in title_text) and (350<= price_value <= 370):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == "knorr green chutney" and (220 <= price_value <= 250):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == "Surf Excel Washing Powder Care - 500G" and ("Surf Excel" in title_text) and (275 <= price_value <= 300):
            result_list.append({
                'title': title_text,
                'price': price_text
            })
        elif product == 'Lays Wavy BBQ Rs.30':
            result_list.append({
                'title': product,
                'price': 30
            })
            break
        elif product == 'Super Catty Chins Cheese Rs.40':
            result_list.append({
                'title': product,
                'price': 40
            })
            break
        elif product == 'Chillz Chips Rs.10':
            result_list.append({
                'title': product,
                'price': 10
            })
            break
        elif product == 'Milo 180 ml':
            result_list.append({
                'title': product,
                'price': 80
            })
            break
        elif product == 'Super Crisp BBQ Rs.40':
            result_list.append({
                'title': product,
                'price': 40
            })
            break
        elif product == 'Pakola Strawberry 200ml':
            result_list.append({
                'title': product,
                'price': 55
            })
            break
        elif product == 'Olpers Badam Zafran':
            result_list.append({
                'title': product,
                'price': 75
            })
            break
        elif product == 'Kurkure Red Chilli Rs.20':
            result_list.append({
                'title': product,
                'price': 20
            })
            break
        elif product == 'Bisconni Chocolate Chip 10':
            result_list.append({
                'title': product,
                'price': 10
            })
            break
        elif product == 'Bisconni Chocolatto Biscuit':
            result_list.append({
                'title': product,
                'price': 10
            })
            break
        elif product == 'Gluco Biscuit':
            result_list.append({
                'title': product,
                'price': 40
            })
            break
        elif product == 'Slice Juice 200ml Mango':
            result_list.append({
                'title': product,
                'price': 38
            })
            break
        elif product == 'Lays Paprika Rs.30':
            result_list.append({
                'title': product,
                'price': 30
            })
            break


    browser.close()

    # return the results as JSON
    return jsonify(results=result_list)

if __name__ == '__main__':
    app.run(host='3.109.3.239', port=8501)
