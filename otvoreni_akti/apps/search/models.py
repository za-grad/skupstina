from django.db import models


class Period(models.Model):
    period_text = models.CharField(max_length=100, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    parent_url = models.CharField(max_length=300)
    period_url = models.CharField(max_length=300)

    def __str__(self):
        return self.period_text


class Item(models.Model):
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    item_title = models.CharField(max_length=100, unique=True)
    item_number = models.IntegerField()
    item_text = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.item_title


class Subject(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    subject_title = models.CharField(max_length=1000)
    subject_url = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return self.subject_url


class Act(models.Model):
    CHOICES = [
        ('HTML', 'HTML'),
        ('docx', 'docx'),
        ('pdf', 'pdf'),
        ('unknown', 'unknown')
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content_url = models.CharField(max_length=1000, unique=True)
    content = models.TextField()
    file_type = models.CharField(
        max_length=20,
        default='HTML',
        choices=CHOICES,
    )
    city = models.CharField(max_length=100, default='Zagreb')

    def __str__(self):
        return self.title
