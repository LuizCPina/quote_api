from django.db import models

CATEGORY_CHOICES = [
    ('motivacional', 'Motivacional'),
    ('reflexiva', 'Reflexiva'),
    ('humor', 'Humor'),
    ('triste','Triste'),
    ]

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255,null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='motivacional')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.author:
            return f'"{self.text}" - {self.author} ({self.category})'
        else:
            return f'"{self.text}" - {self.category}'
