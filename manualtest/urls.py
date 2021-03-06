from django.urls import path

from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("newuser", views.newuser_view, name="newuser"),
    path("testrun/<int:productTestcaseId>", views.testrun_view, name="testrun"),
    path("testcase/<int:productId>", views.testCase_view, name="testcase"),
    path("export/xls/<int:productId>", views.report_view, name="report")

 ]