"""
FreshCart - Selenium Automation Tests
Smart Grocery Management System

HOW TO RUN:
  1. pip install -r requirements.txt
  2. pytest tests/selenium/test_automation.py -v
  3. For HTML report:
     pytest tests/selenium/test_automation.py -v --html=report.html
"""

import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
# Change this path to your actual index.html location
APP_URL = "file:///" + os.path.abspath("index.html").replace("\\", "/")
WAIT    = 10


# --------------------------------------------------
# SETUP & TEARDOWN
# --------------------------------------------------
@pytest.fixture(scope="class")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1400,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Uncomment below line for headless (no browser window):
    # options.add_argument("--headless")

    service = Service(ChromeDriverManager().install())
    driver  = webdriver.Chrome(service=service, options=options)
    driver.get(APP_URL)
    time.sleep(2)
    yield driver
    driver.quit()


def go_to(driver, page):
    """Click sidebar nav link to go to a page."""
    link = driver.find_element(By.CSS_SELECTOR, f'[data-page="{page}"]')
    link.click()
    time.sleep(0.5)


def get_toast(driver):
    """Read toast message."""
    time.sleep(0.6)
    return driver.find_element(By.ID, "toast").text


# --------------------------------------------------
# TEST SUITE 1: Navigation
# --------------------------------------------------
class TestNavigation:

    def test_01_app_loads(self, driver):
        """App title should be FreshCart."""
        assert "FreshCart" in driver.title

    def test_02_dashboard_active_on_load(self, driver):
        """Dashboard page should be active on load."""
        page = driver.find_element(By.ID, "page-dashboard")
        assert "active" in page.get_attribute("class")

    def test_03_navigate_products(self, driver):
        go_to(driver, "products")
        page = driver.find_element(By.ID, "page-products")
        assert "active" in page.get_attribute("class")

    def test_04_navigate_inventory(self, driver):
        go_to(driver, "inventory")
        page = driver.find_element(By.ID, "page-inventory")
        assert "active" in page.get_attribute("class")

    def test_05_navigate_billing(self, driver):
        go_to(driver, "billing")
        page = driver.find_element(By.ID, "page-billing")
        assert "active" in page.get_attribute("class")

    def test_06_navigate_reports(self, driver):
        go_to(driver, "reports")
        page = driver.find_element(By.ID, "page-reports")
        assert "active" in page.get_attribute("class")


# --------------------------------------------------
# TEST SUITE 2: Product Management
# --------------------------------------------------
class TestProducts:

    def test_07_open_add_product_modal(self, driver):
        """Add Product button should open modal."""
        go_to(driver, "products")
        driver.find_element(By.ID, "openAddProduct").click()
        time.sleep(0.3)
        modal = driver.find_element(By.ID, "productModal")
        assert "open" in modal.get_attribute("class")

    def test_08_add_product_valid(self, driver):
        """Adding product with valid data should work."""
        # Fill form
        driver.find_element(By.ID, "productName").clear()
        driver.find_element(By.ID, "productName").send_keys("Selenium Apple")

        Select(driver.find_element(By.ID, "productCategory")).select_by_visible_text("Fruits & Vegetables")
        Select(driver.find_element(By.ID, "productUnit")).select_by_visible_text("kg")

        driver.find_element(By.ID, "productPrice").clear()
        driver.find_element(By.ID, "productPrice").send_keys("80")

        driver.find_element(By.ID, "productStock").clear()
        driver.find_element(By.ID, "productStock").send_keys("100")

        driver.find_element(By.ID, "saveProduct").click()
        time.sleep(0.5)

        # Modal should close
        modal = driver.find_element(By.ID, "productModal")
        assert "open" not in modal.get_attribute("class")

        # Product visible in table
        body = driver.find_element(By.ID, "productTableBody")
        assert "Selenium Apple" in body.text

    def test_09_add_product_empty_name(self, driver):
        """Empty name should show error."""
        driver.find_element(By.ID, "openAddProduct").click()
        time.sleep(0.3)

        driver.find_element(By.ID, "productName").clear()
        Select(driver.find_element(By.ID, "productCategory")).select_by_visible_text("Dairy")
        driver.find_element(By.ID, "productPrice").clear()
        driver.find_element(By.ID, "productPrice").send_keys("50")
        driver.find_element(By.ID, "productStock").clear()
        driver.find_element(By.ID, "productStock").send_keys("10")

        driver.find_element(By.ID, "saveProduct").click()
        toast = get_toast(driver)
        assert "fill" in toast.lower() or "required" in toast.lower()

        driver.find_element(By.ID, "cancelProduct").click()

    def test_10_search_works(self, driver):
        """Search should filter products."""
        search = driver.find_element(By.ID, "productSearch")
        search.clear()
        search.send_keys("Selenium Apple")
        time.sleep(0.3)
        body = driver.find_element(By.ID, "productTableBody")
        assert "Selenium Apple" in body.text
        search.clear()

    def test_11_category_filter(self, driver):
        """Category filter should filter products."""
        select = Select(driver.find_element(By.ID, "categoryFilter"))
        select.select_by_visible_text("Fruits & Vegetables")
        time.sleep(0.3)
        body = driver.find_element(By.ID, "productTableBody")
        assert body.text.strip() != ""
        select.select_by_value("")


# --------------------------------------------------
# TEST SUITE 3: Inventory
# --------------------------------------------------
class TestInventory:

    def test_12_inventory_stats_visible(self, driver):
        """Inventory stat numbers should be digits."""
        go_to(driver, "inventory")
        assert driver.find_element(By.ID, "inv-instock").text.isdigit()
        assert driver.find_element(By.ID, "inv-low").text.isdigit()
        assert driver.find_element(By.ID, "inv-out").text.isdigit()

    def test_13_inventory_table_visible(self, driver):
        """Inventory table should have rows."""
        body = driver.find_element(By.ID, "inventoryTableBody")
        assert body.text.strip() != ""

    def test_14_refresh_button(self, driver):
        """Refresh button should not crash."""
        driver.find_element(By.ID, "refreshInventory").click()
        time.sleep(0.3)
        body = driver.find_element(By.ID, "inventoryTableBody")
        assert body is not None


# --------------------------------------------------
# TEST SUITE 4: Billing
# --------------------------------------------------
class TestBilling:

    def test_15_billing_form_elements(self, driver):
        """Billing page should have required fields."""
        go_to(driver, "billing")
        assert driver.find_element(By.ID, "customerName")  is not None
        assert driver.find_element(By.ID, "billProduct")    is not None
        assert driver.find_element(By.ID, "billQty")        is not None
        assert driver.find_element(By.ID, "generateBill")   is not None

    def test_16_add_item_to_bill(self, driver):
        """Adding an item should show it in the bill table."""
        options = driver.find_element(By.ID, "billProduct").find_elements(By.TAG_NAME, "option")
        if len(options) <= 1:
            pytest.skip("No products available")

        Select(driver.find_element(By.ID, "billProduct")).select_by_index(1)
        driver.find_element(By.ID, "billQty").clear()
        driver.find_element(By.ID, "billQty").send_keys("1")
        driver.find_element(By.ID, "addBillItem").click()
        time.sleep(0.3)

        body = driver.find_element(By.ID, "billItemsBody")
        rows = body.find_elements(By.TAG_NAME, "tr")
        assert len(rows) >= 1

    def test_17_generate_bill_no_customer(self, driver):
        """Generating bill without customer name should error."""
        driver.find_element(By.ID, "customerName").clear()
        driver.find_element(By.ID, "generateBill").click()
        toast = get_toast(driver)
        assert "customer" in toast.lower() or "name" in toast.lower()

    def test_18_clear_bill(self, driver):
        """Clear button should empty the bill."""
        driver.find_element(By.ID, "clearBill").click()
        time.sleep(0.3)
        body = driver.find_element(By.ID, "billItemsBody")
        assert "No items" in body.text or len(body.find_elements(By.TAG_NAME, "tr")) == 1

    def test_19_subtotal_updates(self, driver):
        """Subtotal should update when item added."""
        options = driver.find_element(By.ID, "billProduct").find_elements(By.TAG_NAME, "option")
        if len(options) <= 1:
            pytest.skip("No products available")

        Select(driver.find_element(By.ID, "billProduct")).select_by_index(1)
        driver.find_element(By.ID, "billQty").clear()
        driver.find_element(By.ID, "billQty").send_keys("2")
        driver.find_element(By.ID, "addBillItem").click()
        time.sleep(0.3)

        subtotal = driver.find_element(By.ID, "subtotal").text
        assert subtotal != "₹0.00"


# --------------------------------------------------
# TEST SUITE 5: Dashboard
# --------------------------------------------------
class TestDashboard:

    def test_20_stat_cards_show_numbers(self, driver):
        """Dashboard stat cards should show numeric values."""
        go_to(driver, "dashboard")
        time.sleep(0.3)
        assert driver.find_element(By.ID, "stat-products").text.isdigit()
        assert driver.find_element(By.ID, "stat-bills").text.isdigit()

    def test_21_low_stock_section(self, driver):
        """Low stock section should render."""
        section = driver.find_element(By.ID, "lowStockList")
        assert section is not None
        assert section.text.strip() != ""

    def test_22_recent_bills_section(self, driver):
        """Recent bills section should render."""
        section = driver.find_element(By.ID, "recentBills")
        assert section is not None


# --------------------------------------------------
# TEST SUITE 6: Reports
# --------------------------------------------------
class TestReports:

    def test_23_test_case_table_visible(self, driver):
        """Reports page test case table should have rows."""
        go_to(driver, "reports")
        time.sleep(0.3)
        body = driver.find_element(By.ID, "testCaseBody")
        rows = body.find_elements(By.TAG_NAME, "tr")
        assert len(rows) > 0

    def test_24_export_button_exists(self, driver):
        """Export CSV button should be present."""
        btn = driver.find_element(By.ID, "exportReport")
        assert btn is not None


# --------------------------------------------------
# RUN DIRECTLY
# --------------------------------------------------
if __name__ == "__main__":
    import subprocess
    subprocess.run([
        "pytest", __file__,
        "-v",
        "--html=tests/selenium/automation_report.html",
        "--self-contained-html"
    ])
