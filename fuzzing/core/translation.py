from modeltranslation.translator import translator, TranslationOptions
from .models import (
    Page, ImageLinkSection, ImageSection, BackgroundImageTextSection,
    TextSection, VideoSection
)


class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'left_text', 'right_text',)


class ImageLinkSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle',)


class ImageSectionTranslationOptions(TranslationOptions):
    fields = ('title',)


class BackgroundImageTextSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


class TextSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


class VideoSectionTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Page, PageTranslationOptions)
translator.register(ImageLinkSection, ImageLinkSectionTranslationOptions)
translator.register(ImageSection, ImageSectionTranslationOptions)
translator.register(BackgroundImageTextSection, BackgroundImageTextSectionTranslationOptions)
translator.register(TextSection, TextSectionTranslationOptions)
translator.register(VideoSection, VideoSectionTranslationOptions)
