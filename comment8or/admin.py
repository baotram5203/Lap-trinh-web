from django.contrib import admin
class MessageboardAdminSite(admin.AdminSite):
    title_header = 'Comment8or'
    site_header = 'Comment8or'
    index_title = 'c8admin'
    logout_template = 'comment8or/logged_out.html'