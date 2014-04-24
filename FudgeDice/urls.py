from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from FudgeDice import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FudgeDice.views.home', name='home'),
    # url(r'^FudgeDice/', include('FudgeDice.foo.urls')),

    # http://ethanfudgedice.appspot.com/
    url(r'^$', 'ethanfudgedice.views.main', name='main'),

    #http://ethanfudgedice.appspot.com/5
    url(r'^(?P<diceAmt>\d+)/$', 'ethanfudgedice.views.rollDice', name='rollDice'),

    #http://ethanfudgedice.appspot.com/diceAmtForm
    url(r'^diceAmtForm/$', 'ethanfudgedice.views.diceAmtForm', name='diceAmtForm'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
