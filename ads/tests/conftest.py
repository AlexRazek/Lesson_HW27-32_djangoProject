from pytest_factoryboy import register

from ads.tests.factories import UserFactory, CategoryFactory, AdFactory

pytest_plugins = "ads.tests.fixtures"


#Factories
register(UserFactory)
register(CategoryFactory)
register(AdFactory)