from shop.models import Product

class MiddlewareProduct(object):

    def process_request(self, request):
        request.products = Product.objects.all()
        return None