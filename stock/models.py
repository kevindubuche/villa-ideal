from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 200, verbose_name="Nom",null=True, help_text="Entrez le nom du produit (Max: 200 caractères)")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    created_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Catégorie de produit"

    def __str__(self):
        return self.name

class Product(models.Model):
    item= models.CharField(max_length=200, verbose_name="Nom du produit*", help_text="Entrez le nom du produit (Max: 200 caractères)")
    category = models.ForeignKey(Category, verbose_name='Catégorie',blank=False, null=True, on_delete=models.SET_NULL)
    unit_price= models.DecimalField(blank=False, null=False, max_digits=10,verbose_name="Prix du produit*", decimal_places=3, default=0.000, help_text="Entrez le prix du produit (sensible au millième)")
    description = models.TextField(max_length=500, verbose_name='Description du produit', null=True, blank=True, help_text="Entrez la description du produit (Max: 500 caractères)")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    created_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-date_added']
        verbose_name = "Produit"
    def __str__(self):
        return str(self.item) + " : " + str(self.unit_price) 

class Stock(models.Model):
    item = models.ForeignKey(Product, verbose_name='Produit', null=True, on_delete=models.SET_NULL)
    quatity= models.PositiveIntegerField(blank=False, null=False, verbose_name="Quantité*", default=0, help_text="Entrez la quantité du produit")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    created_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-date_added']
        verbose_name = "Stock"
    def __str__(self):
        return str(self.item) + " : " + str(self.quatity) 

class Sale(models.Model):
    item = models.ForeignKey(Product, verbose_name='Produit', null=True, on_delete=models.SET_NULL)
    quatity= models.PositiveIntegerField(blank=False, null=False, verbose_name="Quantité*", default=0, help_text="Entrez la quantité du produit")
    cost= models.DecimalField(blank=False, null=False, max_digits=10,verbose_name="Prix de vente du produit*", decimal_places=3, default=0.000, help_text="Entrez le prix de vente du produit (sensible au millième)")
    buyer = models.CharField(blank=False, max_length = 200, verbose_name="Nom de l'acheteur",null=True, help_text="Entrez le nom de l'acheteur (Max: 200 caractères)")
    seller = models.CharField(blank=False, max_length = 200, verbose_name="Nom du vendeur",null=True, help_text="Entrez le nom du vendeur (Max: 200 caractères)")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    created_by = models.ForeignKey(User,editable=False,null=True,blank=True, on_delete=models.SET_NULL)
  
    class Meta:
        ordering = ['-date_added']
        verbose_name = "Vente"
    def __str__(self):
        return str(self.item) + " : " + str(self.quatity) 



# class Post(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Titre', help_text='Maximum: 255 caractères')
#     author = models.CharField(max_length=255, verbose_name='Auteur', help_text='Maximum: 255 caractères')
#     category = models.ForeignKey(Category, verbose_name='Catégorie', null=True, on_delete=models.SET_NULL)
#     thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image')
#     slug = models.SlugField()
#     intro = models.TextField()
#     keywords = models.TextField(verbose_name='Mots clés', null=True)
#     content = models.TextField(verbose_name='Contenu')
#     date_added = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')

#     class Meta:
#         ordering = ['-date_added']
#         verbose_name = "Article"
    
#     def save(self, *args, **kwargs):
#         original_slug = slugify(self.title)
#         queryset = Post.objects.all().filter(slug__iexact=original_slug).count()

#         count = 1
#         slug = original_slug
#         while(queryset):
#             slug = original_slug + '-' + str(count)
#             count += 1
#             queryset = Post.objects.all().filter(slug__iexact=slug).count()

#         self.slug = slug

#         super(Post, self).save(*args, **kwargs)

#     # def __str__(self):
#     #     return self.title

# class Pub(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Titre', help_text='Maximum: 255 caractères')
#     link = models.CharField(max_length=500, verbose_name='Lien', help_text='Maximum: 500 caractères')
#     thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image')


# class Team(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Poste', help_text='Maximum: 255 caractères')
#     name = models.CharField(max_length=255, verbose_name='Nom et prénom', help_text='Maximum: 255 caractères')
#     description = models.TextField(verbose_name='Description', null=True)
#     thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image')
