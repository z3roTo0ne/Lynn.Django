#!-*-coding:utf8-*-
from django.contrib import admin
from django_app.models import *
from django.db import models
from simple_history.admin import SimpleHistoryAdmin

# 可以重新定义整个Admin
# class MyAdminSite(admin.AdminSite):
#     site_header = "xxxxx"
#
# admin_site = MyAdminSite(name="myadmin")
# admin_site.register(Author)
#
# 在url中添加
# from django_app.admin import admin_site
# urlpatterns += [
#     url(r'^myadmin/', admin_site.urls),
# ]


# class BookAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Book, BookAdmin)


@admin.register(Book)
class BookAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_per_page = 20
    list_display = ('title', 'get_authors', 'publisher', 'publication_date', 'published')
    date_hierarchy = 'publication_date'
    search_fields = ('title', 'publication_date')
    list_filter = ('title', 'publication_date')
    filter_horizontal = ('authors',)
    actions = ['mark_unpublished', 'mark_published']    # 增加admin的action
    actions_on_top = True  # 控制action栏在页面出现的位置
    empty_value_display = "--empty--"

    # filesets分组显示
    fieldsets = (
        ('书籍信息', {
            'fields': ('title', 'publisher')
        }),
        ('其他操作', {
            'classes': ('collapse',),
            'fields': ('publication_date', 'authors', 'published', ),
        }),
    )

    # action的定义
    def mark_published(self, request, queryset):
        row_update = queryset.update(published=True)
        if row_update == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % row_update
        self.message_user(request, "%s successfully marked as published." % message_bit)

    def mark_unpublished(self, request, queryset):
        row_update = queryset.update(published=False)
        if row_update == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % row_update
        self.message_user(request, "%s successfully marked as unpublished." % message_bit)

    mark_published.short_description = u"选中的书籍标记为 '已出版'"
    mark_unpublished.short_description = u"选中的书籍标记为 '未出版'"


@admin.register(Author)
class AuthorAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('salutation', 'first_name', 'last_name', 'email')


class BookInline(admin.TabularInline):
    model = Book
    max_num = 2
    raw_id_fields = ("authors", )
    verbose_name_plural = "书籍列表"
    show_change_link = True
    radio_fields = {"publisher": admin.VERTICAL}
    extra = 0
    # raw_id_fields is a list of fields you would like to change into an Input widget for
    # either a ForeignKey or ManyToManyField


@admin.register(Publisher)
class PublisherAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')
    inlines = [BookInline, ]  # book是拥有外键的表，也就是从表，只能在主表内联显示从表


@admin.register(Notify)
class NotifyAdmin(admin.ModelAdmin):
    list_display = ('user', 'message')


