from app import app, db
from flask import redirect
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from app.models import Category, Product, User, UserRole
from flask_login import current_user, logout_user


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRole.ADMIN)


class ProductView(AuthenticatedView):
    column_list = ['id', 'name', 'price', 'active', 'created_date']
    column_searchable_list = ['name']
    column_filters = ['id', 'name', 'price']
    column_editable_list = ['name']
    page_size = 8
    can_export = True


class AuthenticatedBaseView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(AuthenticatedBaseView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect("/admin")

class StatsView(AuthenticatedBaseView):
    @expose("/")
    def index(self):
        #...
        return self.render("admin/stats.html")

class CategoryView(AuthenticatedView):
    column_list = ['name', 'products']


admin = Admin(app=app, name='eCommerceApp', template_mode='bootstrap4')
admin.add_view(CategoryView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(AuthenticatedView(User, db.session))
admin.add_view(StatsView(name='Thống kê'))
admin.add_view(LogoutView(name="Đăng xuất"))
