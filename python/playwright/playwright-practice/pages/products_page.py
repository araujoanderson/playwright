from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")

    def get_title(self):
        return self.title.text_content()

    def get_product_count(self):
        return self.inventory_items.count()
