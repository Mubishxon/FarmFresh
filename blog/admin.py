from django.contrib import admin
from .models import Banner, About, Products, Facts, Carousel, Newsletter, Features, Team, Blog
# Register your models here.
admin.site.register(Banner)
admin.site.register(About)
admin.site.register(Products)
admin.site.register(Facts)
admin.site.register(Newsletter)
admin.site.register(Features)
admin.site.register(Team)
admin.site.register(Blog)

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

