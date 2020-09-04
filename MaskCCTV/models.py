from django.db import models

# Create your models here.
class UserInfo(models.Model):
    UserID= models.CharField(max_length=10,null=False)
    UserPWD= models.CharField(max_length=10,null=False)

class MaskInfo(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    set_mask = models.BooleanField()
    ADRESS_PLACE = (
        ('namchuncheon',"강원도 춘천시 효자동 남춘천역"),
        ('gangnam', "서울시 강남구 강남역"),
        ('sareung', "경기도 남양주시 사릉역"),
    )
    adress = models.CharField(
        max_length=20,
        choices=ADRESS_PLACE,
        blank=False,
        default = 'namchuncheon',
        help_text = "CCTV 주소"
    )
    class Meta:
        ordering = ["adress"]
    def __str__(self):
        return f"{self.adress},{self.date},{self.set_mask}"




