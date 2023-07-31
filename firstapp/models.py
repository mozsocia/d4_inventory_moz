from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True)
    parent = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='media/Category_image', blank=True, default='default_category.jpg')

    class Meta:
        
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        
        return self.category_name

class Brand(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    discription = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='media/Brand_image',  blank=True, default='default_brand.jpg')

    class Meta:
        
        verbose_name = 'Brand'
        verbose_name_plural = 'Brand'

    def __str__(self):
        
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'

    def __str__(self):
        
        return self.name
    
    

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    supplier_type = models.CharField(max_length=100)
    supplier_ID = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    start_date = models.DateField(max_length=50)
    amount = models.FloatField(max_length=30)
    guarantor_name = models.CharField(max_length=100)
    guarantor_phone = models.IntegerField()
    image = models.ImageField(upload_to ='media/supplier_image', default="no_img.png" ,blank=True)
    Created_at = models.DateTimeField(max_length=100, blank=True, null=True)
    Updated_at = models.DateTimeField(max_length=100, blank=True, null=True)

    def __str__(self):

        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    customer_ID = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    start_date = models.DateField(max_length=50)
    image = models.ImageField(upload_to ='media/supplier_image',default="no_img.png" , blank=True)
    Created_at = models.DateTimeField(max_length=100, blank=True, null=True)
    Updated_at = models.DateTimeField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Product (models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 100,blank=True, null=True,unique=True)  
    image = models.ImageField(upload_to='ProductImg',default='ProductImg/noimg.jpg', blank=True)
    hover_image = models.ImageField(upload_to='ProductImg',default='noimg.jpg', blank=True, null=True)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    product_purchase_price = models.IntegerField()
    sort_discription = models.TextField(blank=True, null=True)
    discription = models.TextField()
    aditional_discription = models.TextField(blank=True, null=True)
    stock_quantity = models.PositiveIntegerField()
    show_status  = models.BooleanField(default=False)
    flash_sale_add_and_expire_date = models.DateTimeField(blank=True, null=True)
    meta_title = models.CharField(blank=True, null=True,max_length=100)
    meta_keyword = models.CharField(blank=True, null=True,max_length=100)
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    # price_range =models.ForeignKey(store_models.PriceRange, on_delete=models.CASCADE, blank=True, null=True)
    categoris = models.ForeignKey(Category, verbose_name='Product Category', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    
    
    def saving_price(self):
        return self.price  - self.discount_price

    def saving_percent(self):
        return self.saving_price() / self.price  * 100
        
    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['-id']
        
        




class Purchase(models.Model):
    phone = models.IntegerField(blank=True, null=True)
    date = models.DateField()

    status = models.IntegerField()
    payment_status = models.IntegerField()
    total_quantity = models.IntegerField()
    total = models.FloatField()
    discount= models.FloatField(blank=True, null=True)
    shipping_cost = models.FloatField(null=True, blank=True)
    grand_total = models.FloatField()
    
    paid = models.FloatField()
    due = models.FloatField( blank=True, null=True)
    note = models.TextField(null=True, blank=True)

    supplier = models.ForeignKey(Supplier,  blank=True, null=True, on_delete=models.CASCADE)
 

    def __str__(self):
            
        return self.product_name
    
    
class Purchase_order_product(models.Model):
    sub_total = models.FloatField()
    quantity = models.IntegerField()
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    
    



class Sale(models.Model):
    phone = models.IntegerField(blank=True, null=True)
    date = models.DateField()

    status = models.IntegerField()
    payment_status = models.IntegerField()
    total_quantity = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    discount= models.FloatField(blank=True, null=True)
    shipping_cost = models.FloatField(null=True, blank=True)
    grand_total = models.FloatField()
    
    paid = models.FloatField()
    due = models.FloatField( blank=True, null=True)
    note = models.TextField(null=True, blank=True)

    customer = models.ForeignKey(Customer,  blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
            
        return self.product_name
    
class Sale_order_product(models.Model):
    sub_total = models.FloatField()
    quantity = models.IntegerField()
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    