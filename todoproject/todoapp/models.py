from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    # on_delete: User削除された時、同時にTaskも削除する
    # null: User(DB)なしでもOK（誰でも作れる）
    # blank: User情報(文字列)が空欄空白でもOK
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        # 並び順を設定
        ordering = ["completed"]
