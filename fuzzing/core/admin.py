from django.contrib import admin

import reversion

from .models import (Page, ImageSectionMixin, ImageSection, ImageLinkSection,
	TextSection)


class PageAdmin(reversion.VersionAdmin):
	pass


class ImageSectionAdmin(reversion.VersionAdmin):
	pass


class ImageLinkSectionAdmin(reversion.VersionAdmin):
	pass


class TextSectionAdmin(reversion.VersionAdmin):
	pass


admin.site.register(Page, PageAdmin)
admin.site.register(ImageSection, ImageSectionAdmin)
admin.site.register(ImageLinkSection, ImageLinkSectionAdmin)
admin.site.register(TextSection, TextSectionAdmin)