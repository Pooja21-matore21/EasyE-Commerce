from django.contrib import admin
from .models import Product,Category,Recommendation


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','cat_name')


class ProductAdmin(admin.ModelAdmin):
        list_display = ('id','shape','size','location','price','Img','category')

class RecommendationAdmin(admin.ModelAdmin):
        list_display = ('prod_id','user_id','category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Recommendation, RecommendationAdmin)


