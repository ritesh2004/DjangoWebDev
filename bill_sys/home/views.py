from django.shortcuts import render
from home.models import foods,drinks,icecreams

# Create your views here.

def index(request):
    # arr = ['rice','fish','panner','chicken','biriyani','mixveg','omlet','rooti','aluparatha','chowmin','lassi','tea','coffee','lemontea','faluda','sprite','cocacola','sevenup','milk','mangojuice','chocober','snowcream','rolledicecream','softserve','frozenyogurt','venilla','sordet','sherbet','gelato','kulfi']
    foodArr = ['rice','fish','panner','chicken','biriyani','mixveg','omlet','rooti','aluparatha','chowmin']
    drinkArr = ['lassi','tea','coffee','lemontea','faluda','sprite','cocacola','sevenup','milk','mangojuice']
    iceArr = ['chocober','snowcream','rolledicecream','softserve','frozenyogurt','venilla','sordet','sherbet','gelato','kulfi']
    qty = []
    itemArr = []
    itemPrice = []
    subTotal = []
    if request.method == "POST":
        sTotal = 0
        for i in range(10):
            F = int(request.POST.get(foodArr[i]))
            if F>0:
                sTotal += F * int(foods.objects.all()[i].price)
                qty.append(F)
                itemPrice.append(foods.objects.all()[i].price)
                itemArr.append(foods.objects.all()[i].food)
        for j in range(10):
            D = int(request.POST.get(drinkArr[j]))
            if D>0:
                sTotal += int(D) * int(drinks.objects.all()[j].price)
                qty.append(D)
                itemPrice.append(drinks.objects.all()[j].price)
                itemArr.append(drinks.objects.all()[j].drink)
        for k in range(10):
            I = int(request.POST.get(iceArr[k]))
            if I>0:
                sTotal += int(I) * int(icecreams.objects.all()[k].price)
                qty.append(I)
                itemPrice.append(icecreams.objects.all()[k].price)
                itemArr.append(icecreams.objects.all()[k].icecream)
    # return render(request, 'cashier.html',{'rice': foods.objects.all()[0].price, 'fish' : foods.objects.all()[1].price, 'panner' : foods.objects.all()[2].price, 'chicken':foods.objects.all()[3].price, 'biriyani': foods.objects.all()[4].price, 'mixveg': foods.objects.all()[5].price, 'omlet':foods.objects.all()[6].price, 'rooti':foods.objects.all()[7].price, 'aluparatha':foods.objects.all()[8].price, 'chowmin': foods.objects.all()[9].price,'lassi': drinks.objects.all()[0].price, 'tea' : drinks.objects.all()[1].price, 'coffee' : drinks.objects.all()[2].price, 'lemontea':drinks.objects.all()[3].price, 'faluda': drinks.objects.all()[4].price, 'sprite': drinks.objects.all()[5].price, 'cocacola':drinks.objects.all()[6].price, 'sevenup':drinks.objects.all()[7].price, 'milk':drinks.objects.all()[8].price, 'mangojuice': drinks.objects.all()[9].price,'chocober': icecreams.objects.all()[0].price, 'snowcream' : icecreams.objects.all()[1].price, 'rolledicecream' : icecreams.objects.all()[2].price, 'softserve':icecreams.objects.all()[3].price, 'frozenyogurt': icecreams.objects.all()[4].price, 'venilla': icecreams.objects.all()[5].price, 'sordet':icecreams.objects.all()[6].price, 'sherbet':icecreams.objects.all()[7].price, 'gelato':icecreams.objects.all()[8].price, 'kulfi': icecreams.objects.all()[9].price})
        print(itemArr)
        print(qty)
        print(itemPrice)
        for m in range(len(qty)):
            subTotal.append(itemPrice[m]*qty[m])
        dis = int(request.POST.get("discount"))
        print(subTotal)
        finalArr = []
        for a in range(len(itemArr)):
            subArr = []
            subArr.append(itemArr[a])
            subArr.append(qty[a])
            subArr.append(subTotal[a])
            finalArr.append(subArr)
        print(finalArr)
        if dis>0:
            total = sTotal - (sTotal*(dis/100))
            print(total)
        return render(request, 'cashier.html', {'total':total,'dis': dis,'finalArr': finalArr,'subTotal':sTotal})
    return render(request, 'cashier.html')

