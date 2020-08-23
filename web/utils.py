import re,requests,pickle
from .models import Stock,StockError,Property


def get_stock_ids():
    url = "http://tsetmc.com/tsev2/data/MarketWatchPlus.aspx"
    r = requests.get(url)
    ids = set(re.findall(r"\d{15,20}", r.text))
    #print(len(list(ids)))
    return list(ids)

def update_stock_table():
    urls=[]
    for i in get_stock_ids():
        if not Stock.objects.filter(url=i).exists():
            urls.append(i)
    for j in urls:
        url = "http://www.tsetmc.com/Loader.aspx?ParTree=151311&i={}".format(j)
        page = requests.get(url)
        try:
            name = re.findall(r"LVal18AFC=(.*)DE", page.text)[0][1:-2]
            if 'ي' in name:
                n=name.find('ي')
                name=name[:n]+'ی'+name[n+1:]
            if 'ك' in name:
                n=name.find('ك')
                name=name[:n]+'ک'+name[n+1:]
            group = re.findall(r"LSecVal=(.*)Cg", page.text)[0]
            description=re.findall(r"Title=(.*)Fa", page.text)[0][1:-2]
            Stock.objects.create(name=name,description=description,group=group,url=j)
        except:
            StockError.objects.create(url=j)


def check_stock(name):
    if Stock.objects.filter(name=name).exists():
        return True
    else:
        update_stock_table()
        if Stock.objects.filter(name=name).exists():
            return True
        else:
            return False

def check_property(stock,quantity,user):
    if Property.objects.filter(user=user,stock=stock).exists():
        p=Property.objects.get(stock=stock,user=user)
        if p.quantity>=quantity:
            return 0
        else:
            return 2
    else:
        return 1

