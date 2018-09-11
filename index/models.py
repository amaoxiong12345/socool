from django.db import models

# Create your models here.
class Users(models.Model):
    uphone = models.CharField(max_length=20,verbose_name='定哇号码')
    upwd = models.CharField(max_length=20,verbose_name='密码')
    uemail = models.EmailField(verbose_name='优箱')
    uname = models.CharField(max_length=20,verbose_name='名字')
    isActive = models.BooleanField(verbose_name='是否激活')

    def __str__(self):
        return self.uphone

    def to_dict(self):
        dic = {
            'uphone':self.uphone,
            'upwd':self.upwd,
            'uemail':self.uemail,
            'uname':self.uname,
            'isActive':self.isActive
        }
        return dic


# 创建商品类型的实体
class GoodsType(models.Model):
    title = models.CharField(max_length=50,verbose_name='类型名称')
    picture = models.ImageField(upload_to='static/upload/goodstype',null=True,verbose_name='类型图片')
    desc = models.TextField(verbose_name='商品描述')
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'GoodsType'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name
    def to_dict(self):
        dic = {
            'type': self.title,
            'type_picture': self.picture.__str__(),
            'type_desc': self.desc,
        }
        return dic


class Goods(models.Model):
    title = models.CharField(max_length=50,verbose_name='商品名称')
    picture = models.ImageField(upload_to='static/upload/goods',null=True,verbose_name='商品图片')
    spec = models.CharField(max_length=30,verbose_name='商品规格')
    price = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='商品价格')
    goodsType = models.ForeignKey(GoodsType,verbose_name='商品类型')
    isActive = models.BooleanField(default=True,verbose_name='是否上架')
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'Goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name
    def to_dict(self):
        dic = {
            'title': self.title,
            'picture': self.picture.__str__(),
            'price': self.price.__str__(),
            'spec': self.spec,
            'isActive': self.isActive
        }
        return dic

class CartInfo(models.Model):
    users_id = models.ForeignKey(Users,db_column='users_id',verbose_name='用户')
    goods_id = models.ForeignKey(Goods, db_column='goods_id',verbose_name='商品')
    ccount = models.IntegerField(verbose_name='数量')
    def __str__(self):
        return  str(self.ccount)
    class Meta:
        db_table = "CartInfo"
        verbose_name = '购物车'
        verbose_name_plural = verbose_name