from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get('https://www.amazon.in/')
print('*' * 200)


# Login
# click on sign in
driver.find_element_by_css_selector('#nav-link-accountList').click()
time.sleep(1)

# Enter phone number or email input box
login_no = driver.find_element_by_id('ap_email')
login_no.send_keys(916302915887)
# Continue button
continue_button = driver.find_element_by_id('continue')
continue_button.click()


def sign_choice():
    # Login
    # click on sign in

    while True:
        print('1. Sign In Page')
        inp11 = input("Do you remember your password?\nEnter 'yes' or 'no': ").upper()
        print('*' * 200)

        if inp11 == 'YES':
            # Enter Password
            pass_input = input("Enter your amazon password: ")
            print('*' * 200)
            login_pass = driver.find_element_by_id('ap_password')
            login_pass.send_keys(pass_input)

            sign_in_submit = driver.find_element_by_id('signInSubmit')
            sign_in_submit.click()
            print('*' * 200)

            print("You have successfully logged in....hooray!!!!")

            continue_sign_in()

        elif inp11 == 'NO':
            print('*' * 200)

            forgot_password()

        else:
            print("Enter either 'Yes' or 'No'\n"
                  "Other inputs are not accepted")
            print('*' * 200)
        continue


def sign_up():
    driver.find_element_by_css_selector('#nav-link-accountList').click()
    time.sleep(1)
    # Click on Create new account
    driver.find_element_by_css_selector('#createAccountSubmit').click()
    time.sleep(1)

    name = driver.find_element_by_id('ap_customer_name')
    # name_ = input("Enter Name that is unique: ")
    name.send_keys('Alivelu_1245')
    time.sleep(1)

    for label in driver.find_elements_by_css_selector('.a-form-label'):
        if label.text == 'Mobile number or email':
            email = driver.find_element_by_id('ap_email')
            # email_ = input('Enter email: ')
            email.send_keys('upendarreddy1211@gmail.com')
            time.sleep(1)

            pass_ = driver.find_element_by_id('ap_password')
            # input('Enter password 8 characters long with a number and Capital: ')
            pass_.send_keys('Alivelu@01')
            time.sleep(1)

            pass_1 = driver.find_element_by_id('ap_password_check')
            # input('Re enter the same password: ')
            pass_1.send_keys('Alivelu@01')
            time.sleep(1)

            quit()

            # driver.find_element_by_id('continue').click()
            # time.sleep(15)
            #
            # otp1 = (driver.find_element_by_id('cvf-input-code'))
            # otp1.send_keys(int(input("Enter the otp received to your mail:")))
            # time.sleep(2)
            # driver.find_element_by_xpath('//*[@id="cvf-submit-otp-button"]/span/input').click()
            #
            #
            # # add mobile number
            # add_mobile = driver.find_element_by_xpath('//*[@id="cvf-page-content"]/div/div/div/form/div[1]/div/div[2]'
            #                              '/div/div[2]/input')
            # add_mobile.send_keys(7815833626)
            # driver.find_element_by_xpath('//*[@id="a-autoid-0"]/span/input').click()
            #
            # print("You account has been successfully created....hooray!!!!")
            # print('*' * 200)
            #
            # continue_sign_in()

        elif label.text == 'Mobile number':
            phone_no = driver.find_element_by_id('ap_phone_number')
            # int(input('Enter mobile number never used before: '))
            phone_no.send_keys(7815833626)
            time.sleep(1)

            email = driver.find_element_by_id('ap_email')
            # input('Enter email: ')
            email.send_keys('upendarreddy1211@gmail.com')
            time.sleep(1)

            pass_ = driver.find_element_by_id('ap_password')
            # input('Enter password 8 characters long with a number and Capital: ')
            pass_.send_keys('Alivelu@01')
            time.sleep(1)

            quit()

            # driver.find_element_by_id('continue').click()
            # time.sleep(15)
            #
            # otp = driver.find_element_by_xpath('//*[@id="auth-pv-enter-code"]')
            # otp_new_phone = input('Enter otp received in new mobile: ')
            # otp.send_keys(otp_new_phone)
            #
            # driver.find_element_by_xpath('//*[@id="auth-verify-button"]').click()
            #
            # print("You account has been successfully created....hooray!!!!")
            # print('*' * 200)
            #
            # continue_sign_in()


def forgot_password():
    # Click on forget password
    driver.find_element_by_id('auth-fpp-link-bottom').click()
    driver.find_element_by_id('continue').click()

    # Enter otp
    otp = driver.find_element_by_id('cvf-input-code')
    otp.send_keys(int(input("Enter the otp received to phone: ")))
    driver.find_element_by_css_selector('.a-button-input').click()

    # Enter new password
    pass_new = driver.find_element_by_id('ap_fpp_password')
    pass_new.send_keys(input("Enter new password: "))
    # Retype the same password
    pass_new_2 = driver.find_element_by_id('ap_fpp_password_check')
    pass_new_2.send_keys(input("Enter new password again: "))
    driver.find_element_by_id('continue').click()
    print('*' * 200)

    continue_sign_in()


def continue_sign_in():
    while True:
        try:
            print("1. Search Item\n2. Your account\n3. Sign Out")
            inp2 = int(input("Enter your choice: "))
            print('*' * 200)

            if inp2 == 1:
                print('1. Search Item')
                # calling function definition for search item
                search_item()

            elif inp2 == 2:
                # click on your account
                driver.find_element_by_css_selector('.nav-a.nav-a-2'
                                                    '.nav-truncate.nav-progressive-attribute').click()

                your_account()
                time.sleep(3)

            elif inp2 == 3:
                # menu button
                driver.find_element_by_id('nav-hamburger-menu').click()
                time.sleep(2)

                # sign out
                driver.find_element_by_xpath('//*[@id="hmenu-content"]/ul[1]/li[30]/a').click()
                print("Successfully Signed Out....\nThank You...\nCome back soooon....")
                quit()

            else:
                print("Enter only the above given numbers.")
            continue

        except ValueError:
            print('Enter only integers...')
            print('*' * 200)
        continue


def search_item():
    print('*' * 200)

    search = driver.find_element_by_id('twotabsearchtextbox')
    search_submit = driver.find_element_by_id('nav-search-submit-button')
    print('*' * 200)

    search_input = input("enter any item name: ")
    print('*' * 200)

    search.send_keys(search_input)
    search_submit.click()

    lst = ''
    while True:
        for item in driver.find_elements_by_css_selector('.s-result-item.s-asin'):
            item_name = item.find_element_by_css_selector('.a-color-base.a-text-normal')
            print(item_name.text)
            item_link = item.find_element_by_tag_name("a").get_attribute('href')
            print(item_link)

            # storing link in a string
            lst = lst + item_link + ' '
            try:
                item_cost = item.find_element_by_css_selector('.a-price-whole')
                print(f'{item_cost.text}\n')
                print('*' * 200)

            except:
                print("Cost is not given\n")
                print('*' * 200)

        break

    lst_ = list(map(str, lst.split()))
    for i in range(3):
        if lst_[i] == '':
            driver.get(f'{lst_[i]}')
            driver.find_element_by_xpath('').click()
        else:
            driver.get(f'{lst_[i]}')

        add_cart = driver.find_element_by_id('add-to-cart-button')
        time.sleep(2)
        item_name_ = driver.find_element_by_id('productTitle')

        # name
        print(item_name_.text)

        # link
        print(lst_[i])

        # rating
        for j in driver.find_elements_by_css_selector('.a-section.a-spacing-none.a-spacing-top-mini'
                                                      '.cr-widget-ACR'):
            try:
                rating = j.find_element_by_css_selector('.a-size-medium.a-color-base')
                print(rating.text)
                time.sleep(2)

            except:
                print("Rating is not given for this item")

        add_cart.click()
        print("Item successfully added to cart")
        print('*' * 200)
        time.sleep(3)

    print('\nDetails successfully obtained...\n')
    driver.find_element_by_xpath('//*[@id="attach-close_sideSheet-link"]').click()


def your_account():

    count = 0
    account_lst = ''
    for account in driver.find_elements_by_css_selector('.ya-card-cell'):
        count = count + 1

        if count <= 6:
            item_link = account.find_element_by_tag_name("a").get_attribute('href')
            account_lst = account_lst + item_link + ' '
    lst_ = list(map(str, account_lst.split()))

    while True:
        print('*' * 200)

        try:
            print('Your account Info')
            print("1. Your Orders\n2. Login and Security\n3. Amazon Prime\n4. Your Addresses\n"
                  "5. Payment Options\n6. Amazon Pay Balance\n7. Sign Out\n8. Home Page")
            inp3 = int(input('Enter any number from the list: '))
            print('*' * 200)
            if inp3 == 1:
                your_orders(lst_)

            elif inp3 == 2:
                login_and_security(lst_)

            elif inp3 == 3:
                prime(lst_)

            elif inp3 == 4:
                address(lst_)

            elif inp3 == 5:
                payment_options(lst_)

            elif inp3 == 6:
                amazon_pay_balance(lst_)

            elif inp3 == 7:
                # menu button
                driver.find_element_by_id('nav-hamburger-menu').click()
                time.sleep(8)

                # sign out
                driver.find_element_by_xpath('//*[@id="hmenu-content"]/ul[1]/li[30]/a').click()
                print("Successfully Signed Out....\nThank You...\nCome back soooon....")
                print('*' * 200)
                quit()

            elif inp3 == 8:
                # Home Page
                driver.find_element_by_xpath('//*[@id="nav-logo-sprites"]').click()
                time.sleep(10)
                print('*' * 200)
                continue_sign_in()

            else:
                print("Enter only the above given numbers.")

        except ValueError:
            print('Enter only integers...')


def your_orders(lst_):

    driver.get(f'{lst_[0]}')
    print("your Orders")
    time.sleep(2)
    while True:
        try:
            print('1. Orders\n2. Buy again\n3. Not yet shipped\n4. Cancelled Orders\n5. Go back')
            your_ord_inp = int(input('Enter any option from list: '))
            print('*' * 200)
            if your_ord_inp == 1:
                print('Orders')

                while True:
                    try:
                        print('Select previous order time scale -\n1. Past 30 days\n'
                              '2. Past 3 months\n4. 2022\n5. 2021\n6. 2020\n7. go back')
                        drop_d_past_inp = int(input('Enter any option from list: '))
                        print('*' * 200)
                        drop_d_past = Select(driver.find_element_by_css_selector('.a-native-dropdown'))
                        if drop_d_past_inp == 1:
                            drop_d_past.select_by_index(0)
                            try:
                                for items in driver.find_elements_by_css_selector(
                                        '.a-box-group.a-spacing-base.order.js-order-card'):
                                    print(items.text)
                                    time.sleep(10)
                                    print('*' * 200)
                            except:
                                print('No item to display')
                                time.sleep(10)

                        elif drop_d_past_inp == 2:
                            drop_d_past.select_by_index(1)
                            try:
                                for items in driver.find_elements_by_css_selector(
                                        '.a-box-group.a-spacing-base.order.js-order-card'):
                                    print(items.text)
                                    time.sleep(10)
                                    print('*' * 200)

                            except:
                                print('No item to display')
                                time.sleep(10)

                        elif drop_d_past_inp == 3:
                            drop_d_past.select_by_index(2)
                            try:
                                for items in driver.find_elements_by_css_selector(
                                        '.a-box-group.a-spacing-base.order.js-order-card'):
                                    print(items.text)
                                    time.sleep(10)
                                    print('*' * 200)
                            except:
                                print('No item to display')
                                time.sleep(10)

                        elif drop_d_past_inp == 4:
                            drop_d_past.select_by_index(3)
                            try:
                                for items in driver.find_elements_by_css_selector(
                                        '.a-box-group.a-spacing-base.order.js-order-card'):
                                    print(items.text)
                                    time.sleep(10)
                                    print('*' * 200)

                            except:
                                print('No item to display')
                                time.sleep(10)

                        elif drop_d_past_inp == 5:
                            drop_d_past.select_by_index(4)

                            try:

                                for items in driver.find_elements_by_css_selector(
                                        '.a-box-group.a-spacing-base.order.js-order-card'):
                                    print(items.text)
                                    time.sleep(10)
                                    print('*' * 200)

                            except:
                                print('No item to display')
                                time.sleep(10)

                        elif drop_d_past_inp == 6:
                            drop_d_past.select_by_index(5)
                            try:
                                for items in driver.find_elements_by_css_selector(
                                        '.a-box-group.a-spacing-base.order.js-order-card'):
                                    print(items.text)
                                    time.sleep(10)
                                    print('*' * 200)
                            except :
                                print('No item to display')
                                time.sleep(10)

                        elif drop_d_past_inp == 7:
                            driver.find_element_by_xpath(
                                '//*[@id="yourOrdersContent"]/div[1]/ul/li[1]/a').click()
                            time.sleep(10)
                            your_orders(lst_)
                        else:
                            print('Enter numbers only from list')
                        continue

                    except ValueError:
                        print('Enter only integers...')
                    continue
                print('*' * 200)

            elif your_ord_inp == 2:
                print('Buy Again')
                driver.find_element_by_xpath('//*[@id="orderTypeMenuContainer"]/ul/li[3]/span/a').click()
                time.sleep(10)
                # go back
                driver.find_element_by_xpath(
                    '//*[@id="nav-link-accountList"]').click()
                your_orders(lst_)
                print('*' * 200)

            elif your_ord_inp == 3:
                print('Not yet shipped')
                driver.find_element_by_xpath('//*[@id="orderTypeMenuContainer"]/ul/li[4]/span/a').click()
                time.sleep(10)
                # go back
                driver.find_element_by_xpath(
                    '//*[@id="yourOrdersContent"]/div[1]/ul/li[1]/a').click()
                your_orders(lst_)
                print('*' * 200)

            elif your_ord_inp == 4:
                print('Cancelled Orders')
                driver.find_element_by_xpath('//*[@id="orderTypeMenuContainer"]/ul/li[5]/span/a').click()
                print('*' * 200)
                time.sleep(10)
                # go back
                driver.find_element_by_xpath(
                    '//*[@id="yourOrdersContent"]/div[1]/ul/li[1]/a').click()
                your_orders(lst_)
                print('*' * 200)

            elif your_ord_inp == 5:
                print('Taking back to your account')
                print('*' * 200)
                driver.find_element_by_xpath(
                    '//*[@id="yourOrdersContent"]/div[1]/ul/li[1]/a').click()
                time.sleep(5)
                your_account()

            else:
                print('Enter numbers only from list')
            continue

        except ValueError:
            print('Enter only integers...')
            continue


def login_and_security(lst_):

    driver.get(f'{lst_[1]}')
    time.sleep(10)

    # edit name
    while True:
        print("Login and security:\n\n1. Edit Name\n2. Edit Mail id\n3. Edit Mobile Number\n"
              "4. Password\n5. 2 Step Authentication\n6. Secure Account\n7. Exit Page")

        edit_in = int(input("Enter any option from the given list: "))
        if edit_in == 1:
            driver.find_element_by_id('auth-cnep-edit-name-button').click()
            time.sleep(5)

            # Enter new name
            new_name = driver.find_element_by_xpath('//*[@id="ap_customer_name"]')
            new_name_inp = input('Enter new name: ')
            new_name.send_keys(new_name_inp)

            # submit
            driver.find_element_by_id('cnep_1C_submit_button').click()
            print("Name successfully Updated")

        elif edit_in == 2:
            driver.find_element_by_id('auth-cnep-edit-email-button').click()
            time.sleep(5)

            # Enter new mail id
            new_email = driver.find_element_by_css_selector('.a-input-text.a-span12.cvf-widget-input')
            new_email_inp = input('Enter new email address: ')
            new_email.send_keys(new_email_inp)

            # click continue
            driver.find_element_by_id('a-autoid-0-announce').click()

            while True:
                otp_re_inp = input("Do you want another otp?\nEnter 'yes' or 'no': ").upper()
                if otp_re_inp == 'YES':
                    driver.find_element_by_css_selector('.a-link-normal.cvf-widget-btn-val'
                                                        '.cvf-widget-link-collect-resend'
                                                        '.cvf-widget-link-disable-target')
                    continue

                elif otp_re_inp == 'NO':
                    # enter otp
                    otp = driver.find_element_by_css_selector('.a-input-text.a-span12.cvf-widget-input'
                                                              '.cvf-widget-input-code')
                    otp_inp = int(input('Enter Otp'))
                    otp.send_keys(otp_inp)

                    # submit otp
                    driver.find_element_by_css_selector('.a-button-input.notranslate').click()

                    # verify
                    login_pass = driver.find_element_by_id('ap_password')
                    pass_input = input("Enter your amazon password: ")
                    login_pass.send_keys(pass_input)

                    # Click on submit after entering details
                    sign_in_submit = driver.find_element_by_id('cnep_1B_submit_button')
                    sign_in_submit.click()
                    print("Email successfully Updated")
                    quit()

                else:
                    print("Please enter only 'yes' or 'no'")
                continue

        elif edit_in == 3:
            driver.find_element_by_id('auth-cnep-edit-phone-button').click()
            time.sleep(10)

            new_phone = driver.find_element_by_id('ap_phone_number')
            new_phone_inp = input('Enter new mobile number: ')
            new_phone.send_keys(new_phone_inp)
            continue_inp = input("You want to continue:(yes or no)---> ").upper()

            if continue_inp == 'YES':

                # click continue
                driver.find_element_by_id('auth-continue').click()
                time.sleep(5)
                again_verify = input(f"you want to continue with {new_phone_inp} ? (yes or no) ---> ").upper()

                if again_verify == 'YES':
                    driver.find_element_by_id('auth-verification-ok-announce').click()

                    # confirm number is used or not
                    ask_new = input('The new number you entered is having an amazon account? (yes or no):').upper()
                    if ask_new == 'YES':
                        # enter otp
                        otp = driver.find_element_by_id('auth-pv-enter-code')
                        otp_new_phone = input('Enter otp received in new mobile: ')
                        otp.send_keys(otp_new_phone)
                        time.sleep(5)

                        driver.find_element_by_id('auth-verify-button').click()

                        time.sleep(5)
                        # verify password
                        login_pass = driver.find_element_by_id('ap_password')
                        pass_input = input("Enter your amazon password: ")
                        login_pass.send_keys(pass_input)

                        time.sleep(10)
                        # Click on submit after entering details
                        sign_in_submit = driver.find_element_by_id('auth-cnep-change-email-submit')
                        sign_in_submit.click()
                        time.sleep(10)
                        print("Phone Number successfully Updated")

                    elif ask_new == 'NO':
                        driver.find_element_by_id('auth-account-conflict-continue-verify-url').click()
                        time.sleep(5)

                        # enter otp
                        otp = driver.find_element_by_id('auth-pv-enter-code')
                        otp_new_phone = input('Enter otp received in new mobile: ')
                        otp.send_keys(otp_new_phone)

                        driver.find_element_by_id('auth-verify-button')

                        # verify password
                        login_pass = driver.find_element_by_id('ap_password')
                        pass_input = input("Enter your amazon password: ")
                        login_pass.send_keys(pass_input)

                        # Click on submit after entering details
                        sign_in_submit = driver.find_element_by_id('auth-cnep-change-email-submit')
                        sign_in_submit.click()
                        print("Phone Number successfully Updated")

                    else:
                        print('Enter only yes or no')
                    continue

                elif again_verify == 'NO':
                    driver.find_element_by_id('auth-verification-cancel').click()
                    time.sleep(5)

                else:
                    print('Enter only yes or no')
                continue

            elif continue_inp == 'NO':
                # cancel
                driver.find_element_by_id('auth-change-phone-cancel').click()
                time.sleep(5)

            else:
                print('Enter only yes or no')
            continue

        elif edit_in == 4:
            driver.find_element_by_xpath('//*[@id="auth-cnep-edit-password-button"]').click()
            time.sleep(5)
            pass_enq = input('Do you remember your current password:(yes or no)---> ').upper()

            if pass_enq == 'YES':
                # current password
                cur_pass = driver.find_element_by_xpath('//*[@id="ap_password"]')
                cur_pass_inp = input('Enter Current Password:')
                cur_pass.send_keys(cur_pass_inp)

                # New password
                new_pass = driver.find_element_by_xpath('//*[@id="ap_password_new"]')
                new_pass_inp = input('Enter New Password:')
                new_pass.send_keys(new_pass_inp)

                # Re-enter New password
                re_new_pass = driver.find_element_by_xpath('//*[@id="ap_password_new_check"]')
                re_new_pass_inp = input('Re-enter New password:')
                re_new_pass.send_keys(re_new_pass_inp)

                # save changes
                time.sleep(10)
                driver.find_element_by_xpath('//*[@id="cnep_1D_submit_button"]').click()

            elif pass_enq == 'NO':
                forgot_password()

            else:
                print('Enter only yes or no')

        elif edit_in == 5:
            driver.find_element_by_xpath('//*[@id="auth-cnep-advanced-security-settings-button"]').click()
            time.sleep(10)
            driver.find_element_by_xpath('//*[@id="ch-breadcrumb-cas"]').click()
            time.sleep(5)
            login_and_security(lst_)

        elif edit_in == 6:
            driver.find_element_by_xpath('//*[@id="auth-cnep-secure-your-account-button"]').click()
            time.sleep(10)

            # click on done
            driver.find_element_by_xpath('//*[@id="sya-done-button"]/span/a').click()
            login_and_security(lst_)

        elif edit_in == 7:
            driver.find_element_by_xpath('//*[@id="breadcrumb_CNEP"]/li[1]/span/a').click()
            time.sleep(5)
            your_account()


def prime(lst_):
    driver.get(f'{lst_[2]}')
    print('Prime')
    content = driver.find_element_by_css_selector('.a-alert-content')

    print(f'{content.text}\nDo you want to join prime?(yes or no)')
    prime_join = input('Enter yes or no: ').upper()
    if prime_join == 'YES':
        # join prime

        # terms and conditions
        know_terms = input("want to know terms and conditions to join prime?(yes or no)---> ").upper()

        if know_terms == "YES":

            print("Here are the terms and conditions..\nPlease read them thoroughly")
            print('Go and check the chrome tab now, it closes in 20 seconds')
            # click on terms
            term_con = driver.find_element_by_xpath('//*[@id="a-page"]/div[2]/div[2]/div[3]/div/div/a')
            term_con.click()
            time.sleep(20)

            # click on your account
            driver.find_element_by_xpath('//*[@id="nav-link-accountList"]').click()
            time.sleep(5)

            # click on prime
            driver.get(f'{lst_[2]}')
            time.sleep(5)

            # click on join prime
            driver.find_element_by_xpath('//*[@id="a-page"]/div[2]/div[2]/div[2]/div/div[2]'
                                         '/div[1]/div/div/div/div/a').click()
            time.sleep(5)

            join_prime()

        elif know_terms == "NO":
            # click on join prime
            driver.find_element_by_xpath('//*[@id="a-page"]/div[2]/div[2]/div[2]/div/div[2]'
                                         '/div[1]/div/div/div/div/a').click()
            time.sleep(5)

            join_prime()

    elif prime_join == 'NO':
        driver.find_element_by_xpath('//*[@id="nav-link-accountList"]').click()
        your_account()

    print('*' * 200)


def join_prime():
    # Packages
    select_package = int(input("1. 30 days free trial\n2. 3 months membership\n3. 1 year membership\n"
                               "Enter any number from above list:"))
    if select_package == 1:
        # click
        driver.find_element_by_xpath('//*[@id="column-container"]/div[1]/div/div/form').click()
        print('Go and check the chrome tab, it closes in 15 seconds')

    elif select_package == 2:
        driver.find_element_by_xpath('//*[@id="prime-header-quarterly-CTA"]/span/input').click()
        print('Go and check the chrome tab, it closes in 15 seconds')

    elif select_package == 3:
        driver.find_element_by_xpath('//*[@id="prime-header-annual-CTA"]/span/input').click()
        print('Go and check the chrome tab, it closes in 15 seconds')


def address(lst_):
    driver.get(f'{lst_[3]}')
    print('1. Add new address\n2. Edit existing address\n3. Remove existing address')
    add_ = int(input('Enter any number from above given list: '))
    print('*' * 200)
    if add_ == 1:

        # 1. add new address
        driver.find_element_by_xpath('//*[@id="ya-myab-address-add-link"]/div/div').click()

        # Full name
        name = driver.find_element_by_xpath('//*[@id="address-ui-widgets-enterAddressFullName"]')
        name_inp = input('Enter you name: ')
        time.sleep(1)
        name.send_keys(name_inp)

        # Mobile Number
        mob_no = driver.find_element_by_xpath('//*[@id="address-ui-widgets-enterAddressPhoneNumber"]')
        time.sleep(1)
        mob_no_inp = int(input('Enter your mobile number:'))
        mob_no.send_keys(mob_no_inp)

        # Pin code
        pin_code = driver.find_element_by_xpath('//*[@id="address-ui-widgets-enterAddressPostalCode"]')
        time.sleep(1)
        pin_code_inp = int(input('Enter Pin code: '))
        pin_code.send_keys(pin_code_inp)

        # Flat, House no., Building, Company, Apartment
        flat = driver.find_element_by_xpath('//*[@id="address-ui-widgets-enterAddressLine1"]')
        time.sleep(1)
        flat_inp = input('Enter Flat, House no., Building, Company, Apartment: ')
        flat.send_keys(flat_inp)

        # Area, Street, Sector, Village
        area = driver.find_element_by_xpath('//*[@id="address-ui-widgets-enterAddressLine2"]')
        time.sleep(1)
        area_inp = input('Enter Area, Street, Sector, Village: ')
        area.send_keys(area_inp)

        # landmark
        land_mark = driver.find_element_by_xpath('//*[@id="address-ui-widgets-landmark"]')
        time.sleep(1)
        land_mark_inp = input('Enter land mark: ')
        land_mark.send_keys(land_mark_inp)

        # Town/City
        # town = driver.find_element_by_xpath('//*[@id="address-ui-widgets-enterAddressCity"]')
        # town_inp = input('Enter Town/City: ')
        # town.send_keys(town_inp)

        # make default
        def_enq_inp = input('Want to make this address default:(yes or no)----> ').upper()
        while True:
            if def_enq_inp == 'YES':
                driver.find_element_by_xpath('//*[@id="address-ui-widgets-use-as-my-default"]').click()
                print("This address is selected as default address....")
                break

            elif def_enq_inp == 'NO':
                print('Default not opted....')
                break

            else:
                print('Enter yes or no')

        # Address Type
        drop_d_add_type = Select(driver.find_element_by_css_selector('.a-native-dropdown'))

        while True:
            try:
                add_type_inp = int(input('Select\n1. Home Timing\n2. Office Timing'))
                if add_type_inp == 1:
                    drop_d_add_type.select_by_index(1)
                    print('Selected address type as Home')

                    # add address
                    ad_cl = driver.find_element_by_xpath(
                        '//*[@id="address-ui-widgets-form-submit-button"]/span')
                    ad_cl.click()
                    join_prime()

                elif add_type_inp == 2:
                    drop_d_add_type.select_by_index(2)
                    print('Selected address type as Office')

                    # add address
                    ad_cl = driver.find_element_by_xpath(
                        '//*[@id="address-ui-widgets-form-submit-button"]/span')
                    ad_cl.click()
                    join_prime()

                else:
                    print('Enter number from above list')
                continue
            except ValueError:
                print('Enter only integers..')
            continue

    # edit  existing address:
    # h_no_1 = driver.find_element_by_xpath('//*[@id="address-ui-widgets-AddressLineOne"]')
    # print(h_no_1.text)
    #
    # driver.find_element_by_xpath('// *[ @ id = "ya-myab-address-edit-btn-0"]').click()
    # driver.find_element_by_xpath('// *[ @ id = "ya-myab-address-edit-btn-1"]').click()
    # print('*' * 200)


def payment_options(lst_):
    driver.get(f'{lst_[4]}')

    print('Payments Management Page')
    print('1. Default Purchase Settings\n2. Manage kindle Payment Settings\n3. Edit payment method for current order'
          '\n4. Manage Bank Accounts')
    pay_inp = int(input('Enter options from list given above: '))
    while True:
        try:
            if pay_inp == 1:
                driver.find_element_by_xpath('//*[@id="leftNavbarPane"]/div/div/div/a[1]').click()
                print('Default Purchase Settings Page')
                print('Go and check the chrome tab, it closes in 15 seconds')
                time.sleep(15)

                # go to your account
                driver.find_element_by_xpath('//*[@id="headerCol"]/h1/a').click()

                your_account()

            elif pay_inp == 2:
                driver.find_element_by_xpath('//*[@id="leftNavbarPane"]/div/div/div/a[2]').click()
                print('Manage kindle Payment Settings Page')
                print('Go and check the chrome tab, it closes in 15 seconds')
                time.sleep(15)

                # go to your account
                driver.find_element_by_xpath('//*[@id="nav-link-accountList"]').click()

                your_account()

            elif pay_inp == 3:
                driver.find_element_by_xpath('//*[@id="leftNavbarPane"]/div/div/div/a[3]').click()
                print('Edit payment method for current order Page')
                print('Go and check the chrome tab, it closes in 15 seconds')
                time.sleep(15)

                # go to your account
                driver.find_element_by_xpath('//*[@id="yourOrdersContent"]/div[1]/ul/li[1]/a').click()

                your_account()

            elif pay_inp == 4:
                driver.find_element_by_xpath('//*[@id="leftNavbarPane"]/div/div/div/a[4]').click()
                print('Manage Bank Accounts Page')
                print('Go and check the chrome tab, it closes in 15 seconds')
                time.sleep(15)

                # go to your account
                driver.find_element_by_xpath('//*[@id="breadcrumb-row"]/div/ul/li[1]/span/a').click()

                your_account()

            else:
                print('Enter values from the list only')
            continue

        except ValueError:
            print('Enter only integers')
        continue


def amazon_pay_balance(lst_):
    driver.get(f'{lst_[5]}')
    print('*' * 200)

    while True:
        print('Amazon Pay Balance\n\n1. Check current balance\n2. Add money to balance\n3. Your Account')
        pay_task = int(input('Enter any option you want to perform: '))

        try:
            if pay_task == 1:
                current_balance = driver.find_element_by_xpath('//*[@id="add-money-form"]/div[1]/div[1]/div[1]')
                print(current_balance.text)

                driver.find_element_by_xpath('//*[@id="adm-breadcrumb-row"]/div/div[1]/ul/li[1]/span/a/span').click()
                amazon_pay_balance(lst_)

            elif pay_task == 2:
                driver.find_element_by_xpath('//*[@id="a-autoid-4"]/span').click()
                print('Go and check the chrome tab\n'
                      'Note: After opening the tab please click on previous page option to let the program run smoothly'
                      '\nSorry for the inconveniences, it is a beta version we will resolve this issue soon...')
                time.sleep(30)
                driver.find_element_by_xpath('//*[@id="adm-breadcrumb-row"]/div/div[1]/ul/li[1]/span/a/span').click()
                time.sleep(10)

                amazon_pay_balance(lst_)

            elif pay_task == 3:
                driver.find_element_by_xpath('//*[@id="adm-breadcrumb-row"]/div/div[1]/ul/li[1]/span/a/span').click()
                your_account()

            else:
                print('Enter values from the list')
        except ValueError:
            print('Enter only integers..')


print(f"{'*' * 75} Welcome to Amazon {'*' * 75}\n")

while True:

    try:
        print("1. Sign In\n"
              "2. Sign Up\n")
        Inp1 = int(input("Enter your Choice: "))
        print('*' * 200)
        if Inp1 == 1:

            sign_choice()

        elif Inp1 == 2:
            print('2. Sign Up Page')
            print('*' * 200)

            sign_up()

        else:
            print("Please enter only integers from the list mentioned above......")
            print('*' * 200)

    except ValueError:
        print('Enter only integers...')
        print('*' * 200)
