"""Module that adds translation fields to the models"""

from modeltranslation.translator import translator, TranslationOptions
from .models import *


class PageTrans(TranslationOptions):
    fields = ('title', 'slug')


class TextSectionTrans(TranslationOptions):
    fields = ('title', 'text', )


class ImageSectionTrans(TranslationOptions):
    fields = ('title', )


translator.register(Page, PageTrans)
translator.register(TextSection, TextSectionTrans)
translator.register(ImageSection, ImageSectionTrans)
