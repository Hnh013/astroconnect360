from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static
from django.conf.urls import url
from django.contrib import admin
from django.urls import path







urlpatterns = [
    ##################
    path('chngprof',views.chngprof,name='chngprof'),
    path('chngpass',views.chngpass,name='chngpass'),
    path('dtwo',views.dtwo,name='dtwo'),
    path('ptwo',views.ptwo,name='ptwo'),
    path('mtwo',views.mtwo,name='mtwo'),
    path('deduct/',views.deduct,name='deduct'),
    path('consult/<str:astro>', views.consult, name='consult'),
    path('astrochat/<str:room_name>', views.astrochat, name='astrochat'),
    path('showchat/', views.ShowChatHome, name='showchat'),
    path('room/<str:room_name>/<str:person_name>', views.ShowChatPage, name='showchat'),
    #path('timer/', views.timer, name='timer'),
    #path('appt/', views.appt, name='appt'),
    #path('astroscreen/', views.astroscreen, name='astroscreen'),
    #path('reply/<str:id>/', views.reply, name='reply'),
    #################
     path('phoneverify', views.phoneverify, name='phoneverify'),
     path('otpverify', views.otpverify, name='otpverify'),
    path('calling/<str:caller>/<str:astro>/', views.calling, name='calling'),
    path('phonesignup', views.phonesignup, name='phonesignup'),

    path('homeview', views.homeview, name="homeview"),
    path('post/<slug:slug>/', views.detailview, name="detailview"),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),

    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
######## Added on 10jul2020
    ## register login paths, login path provided by default 
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    ## profile edit paths
    path('completeprofile', views.completeprofile, name='completeprofile'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('updateprofilepic', views.updateprofilepic, name='updateprofilepic'),
    ## astroprofile creation and update paths
    path('createastroprofile', views.createastroprofile, name='createastroprofile'),
    path('updateastroprofile', views.updateastroprofile, name='updateastroprofile'),
    ## Wallet paths
    url(r'^recharge/$', views.recharge, name='recharge'),
    url(r'^charge/$', views.charge, name='charge'),
    ## password reset paths , default paths with no view only templates
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"), name='password_reset_complete'),
    path('astrosearch/', views.astrosearch, name='astrosearch'),
    path('astrodetail<str:id>', views.astrodetail, name='astrodetail'),


    ## Horoscopes urls
    path('viewdailyhoroscopelist', views.viewdailyhoroscopelist, name='viewdailyhoroscopelist'),
    path('viewweeklyhoroscopelist', views.viewweeklyhoroscopelist, name='viewweeklyhoroscopelist'),
    path('viewmonthlyhoroscopelist', views.viewmonthlyhoroscopelist, name='viewmonthlyhoroscopelist'),
    path('viewyearlyhoroscopelist', views.viewyearlyhoroscopelist, name='viewyearlyhoroscopelist'),
    path('horoscope', views.horoscope, name='horoscope'),
    path('lovehoroscope', views.lovehoroscope, name='lovehoroscope'),
    path('healthhoroscope', views.healthhoroscope, name='healthhoroscope'),
    path('viewtodayhoroscope<str:zodiac>', views.viewtodayhoroscope, name='viewtodayhoroscope'),
    path('viewdailyhoroscope<str:id>', views.viewdailyhoroscope, name='viewdailyhoroscope'),
    path('viewweeklyhoroscope<str:id>', views.viewweeklyhoroscope, name='viewweeklyhoroscope'),
    path('viewmonthlyhoroscope<str:id>', views.viewmonthlyhoroscope, name='viewmonthlyhoroscope'),
    path('viewyearlyhoroscope<str:id>', views.viewyearlyhoroscope, name='viewyearlyhoroscope'),
    
    path('createdailyhoroscope', views.createdailyhoroscope, name='createdailyhoroscope'),
    path('editdailyhoroscope<str:id>', views.editdailyhoroscope, name='editdailyhoroscope'),
    path('deletedailyhoroscope<str:id>', views.deletedailyhoroscope, name='deletedailyhoroscope'),
    path('createweeklyhoroscope', views.createweeklyhoroscope, name='createweeklyhoroscope'),
    path('editweeklyhoroscope<str:id>', views.editweeklyhoroscope, name='editweeklyhoroscope'),
    path('deleteweeklyhoroscope<str:id>', views.deleteweeklyhoroscope, name='deleteweeklyhoroscope'),
    path('createmonthlyhoroscope', views.createmonthlyhoroscope, name='createmonthlyhoroscope'),
    path('editmonthlyhoroscope<str:id>', views.editmonthlyhoroscope, name='editmonthlyhoroscope'),
    path('deletemonthlyhoroscope<str:id>', views.deletemonthlyhoroscope, name='deletemonthlyhoroscope'),
    path('createyearlyhoroscope', views.createyearlyhoroscope, name='createyearlyhoroscope'),
    path('edityearlyhoroscope<str:id>', views.edityearlyhoroscope, name='edityearlyhoroscope'),
    path('deleteyearlyhoroscope<str:id>', views.deleteyearlyhoroscope, name='deleteyearlyhoroscope'),
    ## Panchang urls
    path('viewpanchang', views.viewpanchang, name='viewpanchang'),
    path('viewdailysolarcyclelist', views.viewdailysolarcyclelist, name='viewdailysolarcyclelist'),
    path('viewhindumonthyearlist', views.viewhindumonthyearlist, name='viewhindumonthyearlist'),
    path('viewdailytimingslist', views.viewdailytimingslist, name='viewdailytimingslist'), 
    path('viewdailypanchanglist', views.viewdailypanchanglist, name='viewdailypanchanglist'),
    path('createdailypanchang', views.createdailypanchang, name='createdailypanchang'),
    path('editdailypanchang<str:id>', views.editdailypanchang, name='editdailypanchang'),
    path('deletedailypanchang<str:id>', views.deletedailypanchang, name='deletedailypanchang'),
    path('createdailysolarcycle', views.createdailysolarcycle, name='createdailysolarcycle'),
    path('editdailysolarcycle<str:id>', views.editdailysolarcycle, name='editdailysolarcycle'),
    path('deletedailysolarcycle<str:id>', views.deletedailysolarcycle, name='deletedailysolarcycle'),
    path('createhindumonthyear', views.createhindumonthyear, name='createhindumonthyear'),
    path('edithindumonthyear<str:id>', views.edithindumonthyear, name='edithindumonthyear'),
    path('deletehindumonthyear<str:id>', views.deletehindumonthyear, name='deletehindumonthyear'),
    path('createdailytimings', views.createdailytimings, name='createdailytimings'),
    path('editdailytimings<str:id>', views.editdailytimings, name='editdailytimings'),
    path('deletedailytimings<str:id>', views.deletedailytimings, name='deletedailytimings'),
    ## Kundli urls
    path('createkundli', views.createkundli, name='createkundli'),
    path('viewkundli', views.viewkundli, name='viewkundli'),
    ## Numerology urls
    path('dailynumerologylist', views.dailynumerologylist, name='dailynumerologylist'),
    path('weeklynumerologylist', views.weeklynumerologylist, name='weeklynumerologylist'),
    path('monthlynumerologylist', views.monthlynumerologylist, name='monthlynumerologylist'),
    path('yearlynumerologylist', views.yearlynumerologylist, name='yearlynumerologylist'),
    path('createdailynumerology', views.createdailynumerology, name='createdailynumerology'),
    path('editdailynumerology<str:id>', views.editdailynumerology, name='editdailynumerology'),
    path('deletedailynumerology<str:id>', views.deletedailynumerology, name='deletedailynumerology'),
    path('createweeklynumerology', views.createweeklynumerology, name='createweeklynumerology'),
    path('editweeklynumerology<str:id>', views.editweeklynumerology, name='editweeklynumerology'),
    path('deleteweeklynumerology<str:id>', views.deleteweeklynumerology, name='deleteweeklynumerology'),
    path('createmonthlynumerology', views.createmonthlynumerology, name='createmonthlynumerology'),
    path('editmonthlynumerology<str:id>', views.editmonthlynumerology, name='editmonthlynumerology'),
    path('deletemonthlynumerology<str:id>', views.deletemonthlynumerology, name='deletemonthlynumerology'),
    path('createyearlynumerology', views.createyearlynumerology, name='createyearlynumerology'),
    path('edityearlynumerology<str:id>', views.edityearlynumerology, name='edityearlynumerology'),
    path('deleteyearlynumerology<str:id>', views.deleteyearlynumerology, name='deleteyearlynumerology'),
    ## Tarot urls
    path('yearlytarotlist', views.yearlytarotlist, name='yearlytarotlist'),
    #path('tarotarticlelist', views.tarotarticlelist, name='tarotarticlelist'),
    path('createyearlytarot', views.createyearlytarot, name='createyearlytarot'),
    path('edityearlytarot<str:id>', views.edityearlytarot, name='edityearlytarot'),
    path('deleteyearlytarot<str:id>', views.deleteyearlytarot, name='deleteyearlytarot'),
    path('createtarotarticle', views.createtarotarticle, name='createtarotarticle'),
    path('edittarotarticle<str:id>', views.edittarotarticle, name='edittarotarticle'),
    path('deletetarotarticle<str:id>', views.deletetarotarticle, name='deletetarotarticle'),
    path('viewtarot', views.viewtarot, name='viewtarot'),
    path('viewtarotarticle<str:id>', views.viewtarotarticle, name='viewtarotarticle'),
    path('viewyearlytarot', views.viewyearlytarot, name='viewyearlytarot'),
    ## Love urls
    path('checklove', views.checklove, name='checklove'),
    path('viewlove', views.viewlove, name='viewlove'),
    ##
    path('viewpalmreading', views.viewpalmreading, name='viewpalmreading'),    





   


    
]