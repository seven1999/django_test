# coding:utf-8

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# python_2_unicode_compatible 会自动做一些处理去适应python不同的版本，本例中的 unicode_literals 可以让python2.x 也像 python3 那个处理 unicode 字符


# Create user table
@python_2_unicode_compatible
class UserTab(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(u'姓名', max_length=50)
    user_idno = models.CharField(max_length=20)
    user_mobile = models.CharField(max_length=20)
    user_sex = models.CharField(max_length=2)
    user_age = models.IntegerField()
    remark = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.user_name

    class Meta:
        db_table = 'user_tab'


class ShopTab(models.Model):
    id = models.AutoField(primary_key=True)
    shop_id = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    item_id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    stock = models.IntegerField()
    status = models.IntegerField()
    description = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def my_property(self):
        return self.shop_id + ' ' + self.name

    my_property.short_description = "Full name of the Shop"

    full_name = property(my_property)

    class Meta:
        db_table = 'shop_tab'

