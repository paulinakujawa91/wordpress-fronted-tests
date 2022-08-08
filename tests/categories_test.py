import random
import pytest
from pages.categories_page import CategoriesPage
from tests import const


@pytest.mark.usefixtures('setup')
class TestCategories:
    slug = 'New slug xyz'
    parent_category = 'Uncategorized'

    def test_create_new_category(self):
        category = 'New category number ' + str(random.randint(0, 1000))
        categories_page = CategoriesPage(self.driver)

        categories_page.log_in(const.login, const.password)
        categories_page.open_category_view()
        categories_page.add_new_category(category, self.slug, self.parent_category)

        assert categories_page.is_category_exists(category)

    def test_edit_category(self):
        old_category_name = "Old category"
        new_category_name = "New category"
        categories_page = CategoriesPage(self.driver)

        categories_page.log_in(const.login, const.password)
        categories_page.open_category_view()
        categories_page.add_new_category(old_category_name, self.slug, self.parent_category)
        categories_page.edit_category_name(old_category_name, new_category_name)

        assert categories_page.is_category_updated()

    def test_delete_category(self):
        category_name = 'Category to delete'
        categories_page = CategoriesPage(self.driver)

        categories_page.log_in(const.login, const.password)
        categories_page.open_category_view()
        categories_page.add_new_category(category_name, self.slug, self.parent_category)
        categories_page.delete_category(category_name)

        assert categories_page.is_category_deleted(category_name)
