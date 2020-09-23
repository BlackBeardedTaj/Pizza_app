#!C:\Users\Kompjuter\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi, cgitb

def chk(element):
        global form
        if element in form:
                erg = form[element].value
        else:
                erg = ""
        return erg

cgitb.enable()

form = cgi.FieldStorage()

print("Content-type: text/html")
print()
print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8'></head>")
print("<body>")

print("<p>Hello", chk("fn"), chk("ln"), "</p>")

print("<p>Your Address:", chk("st"), chk("sn"),
      "in", chk("zp"), chk("lo"), "</p>")

print("<p>You ordered: Pizza", chk("pt"))

liste_of_prices = {"Salami":6, "Di Mare":6.5,
                "Quattro Stagioni":7.5, "Diavolo":8.5}
price = liste_of_prices[form["pt"].value]

garnish_list = {"Chilli Pepper":1, "Olives":1.2,
                 "Anchovies":1.5}
if "ga" in form:
    try:
        print("with", form["ga"].value)
        price += garnish_list[form["ga"].value]
    except:
        for element in form["ga"]:
                print(", with", element.value)
                price += garnish_list[element.value]
print("</p>")

if "fd" in form:
        print("<p>With Fast Delivery</p>")
        price += 1.5

if "co" in form:
        print("<p>Comment:", form["co"].value, "</p>")

if "cp" in form:
        if form["cu"].value == "R" \
           and form["cp"].value == "Discount5":
                price = price * 0.95
                print("<p>Discount 5%</p>")

print(f"Price : {price:.2f} &euro;")

print("</body>")
print("</html>")
