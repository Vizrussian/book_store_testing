# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='D:/chromedriver')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in")
#
# # My account
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# # Email
# email = driver.find_element_by_id('username')
# email.send_keys('potato@swety.com')
# # Password
# password = driver.find_element_by_id('password')
# password.send_keys('IloveNIPPON-69')
# # Register
# register_btn = driver.find_element_by_name('login')
# register_btn.click()
# # Shop
# shop_btn = driver.find_element_by_link_text('Shop')
# shop_btn.click()
# # HTML 5 Forms
# book_btn = driver.find_element_by_css_selector('.post-181 h3')
# book_btn.click()
# # Head
# name_book = driver.find_element_by_css_selector('.product_title.entry-title')
# name_book_text = name_book.text
# assert name_book_text == 'HTML5 Forms'
# # Exit
# driver.quit()
import time

# # Задача №2
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='D:/chromedriver')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in")
#
# # My account
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# # Email
# email = driver.find_element_by_id('username')
# email.send_keys('potato@swety.com')
# # Password
# password = driver.find_element_by_id('password')
# password.send_keys('IloveNIPPON-69')
# # Login
# register_btn = driver.find_element_by_name('login')
# register_btn.click()
# # Shop
# shop_btn = driver.find_element_by_link_text('Shop')
# shop_btn.click()
# # HTML
# html_btn = driver.find_element_by_link_text('HTML')
# html_btn.click()
# # 3 items on page
# items_page = driver.find_elements_by_css_selector('.product.type-product.status-publish')
# if len(items_page) == 3:
#     print("На странице 3 книги")
# else:
#     print(f'На странице {len(items_page)} книжек')
# # Exit
# driver.quit()

# # Задача №3
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome(executable_path='D:/chromedriver')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in")
#
# # My account
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# # Email
# email = driver.find_element_by_id('username')
# email.send_keys('potato@swety.com')
# # Password
# password = driver.find_element_by_id('password')
# password.send_keys('IloveNIPPON-69')
# # Login
# register_btn = driver.find_element_by_name('login')
# register_btn.click()
# # Shop
# shop_btn = driver.find_element_by_link_text('Shop')
# shop_btn.click()
# # Check selector
# default_value = driver.find_element_by_css_selector('[name = "orderby"].orderby')
# check_default_value = default_value.get_attribute('value')
# assert check_default_value == 'menu_order'
# # Our choice
# choice = driver.find_element_by_css_selector('[name = "orderby"].orderby')
# select = Select(choice)
# select.select_by_value('price-desc')
# # Locator
# choice = driver.find_element_by_css_selector('[name = "orderby"].orderby')
# # Check sorting by desc
# check_our_value = choice.get_attribute('value')
# assert check_our_value == 'price-desc'
# # Exit
# driver.quit()

# Задача №4
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome(executable_path='D:/chromedriver')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in")
#
# # My account
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# # Email
# email = driver.find_element_by_id('username')
# email.send_keys('potato@swety.com')
# # Password
# password = driver.find_element_by_id('password')
# password.send_keys('IloveNIPPON-69')
# # Login
# register_btn = driver.find_element_by_name('login')
# register_btn.click()
# # Shop
# shop_btn = driver.find_element_by_link_text('Shop')
# shop_btn.click()
# # Android book
# android_book = driver.find_element_by_css_selector('.post-169 h3')
# android_book.click()
# # Old price
# old_price = driver.find_element_by_css_selector('.price>del>.amount')
# value_old_price = old_price.text
# assert value_old_price == '₹600.00'
# # New price
# new_price = driver.find_element_by_css_selector('ins>.amount')
# value_new_price = new_price.text
# assert value_new_price == '₹450.00'
# # Click on the book
# book_btn = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")) )
# book_btn.click()
# # Close cover
# close_btn = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR,'.pp_close')) )
# close_btn.click()
# # Exit
# driver.quit()

# Задача №5
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome(executable_path='D:/chromedriver')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in")
#
# # Shop
# shop_btn = driver.find_element_by_link_text('Shop')
# shop_btn.click()
# # HTML book
# html_book = driver.find_element_by_css_selector('[data-product_id="182"]')
# html_book.click()
# # Check 1 item and price
# time.sleep(3)
# item_in_cart = driver.find_element_by_css_selector('.cartcontents')
# item_in_cart_text = item_in_cart.text
# assert item_in_cart_text == '1 Item'
# price_cart = driver.find_element_by_css_selector('.wpmenucart-contents>.amount')
# price_cart_text = price_cart.text
# assert price_cart_text == '₹180.00'
# # Get to cart
# cart = driver.find_element_by_css_selector('.wpmenucartli')
# cart.click()
# # Subtotal
# subtotal = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-title="Subtotal"]>span'), '₹180.00'))
# # Total
# total = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-title="Total"]>strong>span'), '₹183.60'))
# # Exit
# driver.quit()

# #Задача №6
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='D:/chromedriver')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in")
#
# # Shop
# shop_btn = driver.find_element_by_link_text('Shop')
# shop_btn.click()
# # Add two books
# driver.execute_script('window.scrollBy(0,300);')
# html_book = driver.find_element_by_css_selector('[data-product_id="182"]')
# html_book.click()
# time.sleep(3)
# jsdata_book = driver.find_element_by_css_selector('[data-product_id="180"]')
# jsdata_book.click()
# # Get to cart
# cart = driver.find_element_by_css_selector('.wpmenucartli')
# cart.click()
# # Delete first book
# time.sleep(3)
# delete_first = driver.find_element_by_css_selector('tbody>tr:nth-child(1) .remove')
# delete_first.click()
# # Undo
# time.sleep(3)
# undo_btn = driver.find_element_by_link_text('Undo?')
# undo_btn.click()
# # Quantity = 3
# quantity = driver.find_element_by_css_selector('.cart_item:nth-child(1) input')
# quantity.clear()
# quantity.send_keys(3)
# # Update cart
# time.sleep(3)
# upd_cart = driver.find_element_by_css_selector('[name="update_cart"]')
# upd_cart.click()
# # Check value
# value_cart = quantity.get_attribute('value')
# assert value_cart == "3"
# # Apply coupon
# time.sleep(3)
# apply_coupon = driver.find_element_by_css_selector('[name="apply_coupon"]')
# apply_coupon.click()
# # Check coupon code
# time.sleep(3)
# coupon_code = driver.find_element_by_css_selector('.woocommerce-error li')
# coupon_code_text = coupon_code.text
# assert coupon_code_text == 'Please enter a coupon code.'
# # Exit
# driver.quit()

# Задача №7from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.support.wait import WebDriverWait
# #
# # driver = webdriver.Chrome(executable_path='D:/chromedriver')
# # driver.maximize_window()
# # driver.get("https://practice.automationtesting.in")
# #
# # # Shop
# # shop_btn = driver.find_element_by_link_text('Shop')
# # shop_btn.click()
# # # Add book
# # driver.execute_script('window.scrollBy(0,300);')
# # html_book = driver.find_element_by_css_selector('[data-product_id="182"]')
# # html_book.click()
# # # Get to cart
# # time.sleep(3)
# # cart = driver.find_element_by_css_selector('.wpmenucartli')
# # cart.click()
# # # Checkout
# # checkout = WebDriverWait(driver, 10).until(
# #     EC.element_to_be_clickable((By.CSS_SELECTOR, '.wc-forward')))
# # checkout.click()
# # # Enter data
# # first_name = WebDriverWait(driver, 10).until(
# #     EC.visibility_of_element_located((By.ID, 'billing_first_name')))
# # first_name = driver.find_element_by_id('billing_first_name')
# # first_name.send_keys('Potato')
# # last_name = driver.find_element_by_id('billing_last_name')
# # last_name.send_keys('Swety')
# # email = driver.find_element_by_id('billing_email')
# # email.send_keys('potato@swety.com')
# # phone = driver.find_element_by_id('billing_phone')
# # phone.send_keys('88005553535')
# # country = driver.find_element_by_id('s2id_billing_country')
# # country.click()
# # country = driver.find_element_by_id('s2id_autogen1_search')
# # country.send_keys('United States\n')
# # adress = driver.find_element_by_id('billing_address_1')
# # adress.send_keys('Pyshkina street')
# # town = driver.find_element_by_id('billing_city')
# # town.send_keys('Moskow')
# # state = driver.find_element_by_id('select2-chosen-2').click()
# # state = driver.find_element_by_id('s2id_autogen2_search')
# # state.send_keys('Idaho\n')
# # post_code = driver.find_element_by_id('billing_postcode')
# # post_code.send_keys('83843')
# # # Payments
# # driver.execute_script('window.scrollBy(0,600);')
# # time.sleep(3)
# # payments = driver.find_element_by_id('payment_method_cheque')
# # payments.click()
# # # Order
# # order_btn = driver.find_element_by_id('place_order')
# # order_btn.click()
# # # 1
# # pacage = WebDriverWait(driver, 10).until(
# #      EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-thankyou-order-received'),
# #                                       'Thank you. Your order has been received.'))
# # # 2
# # method = WebDriverWait(driver, 10).until(
# #      EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.method strong'), 'Check Payments'))
# # # Exit
# # driver.quit()
#
