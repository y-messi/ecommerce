from .cart import Cart

# create a context processor so that our cart can work on every page orf the site
def cart(request):
    #return the default data from our cart
    return {'cart': Cart(request)}