from django.db import models

class WordlistE(models.Model):
    num = models.IntegerField(default=0)
    vocab = models.CharField("英単語", max_length=200)
    mean = models.CharField("意味", max_length=200)
    phrase = models.CharField("MINIMAL PHRASES", max_length=300, default=" ")
    yaku = models.CharField("日本語訳", max_length=200, default=" ")
    CHOICES = (
        ("動詞","動詞"),
        ("名詞","名詞"),
        ("形容詞","形容詞"),
        ("副詞","副詞"),
        ("その他","その他"),
        ("熟語","熟語")
    )
    cata = models.CharField("品詞", max_length=100, choices=CHOICES)
    CHOICE = (
        ("赤","赤"),
        ("黄","黄"),
        ("青","青")
    )
    color = models.CharField("色", max_length=20, default="赤", choices=CHOICE)

# verb,nouns,adjective,adverb,others,phrase