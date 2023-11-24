from BaseApp import BasePage
from selenium.webdriver.common.by import By

class SeacrhLocators:
    Locator_Email_Field = (By.ID, 'loginEmail')
    Locator_Password_Field = (By.ID, 'loginPassword')
    Locator_Authorization_Button = (By.ID, 'authButton')
    Locator_Main_Title = (By.TAG_NAME, 'h3')
    Locator_Error_Message = (By.CLASS_NAME, 'uk-alert')


class SearchHelper(BasePage):

    def enter_email(self, word):
        search_field = self.find_element(SeacrhLocators.Locator_Email_Field)
        search_field.send_keys(word)
        return search_field

    def enter_password(self, word):
        search_field = self.find_element(SeacrhLocators.Locator_Password_Field)
        search_field.send_keys(word)
        return search_field

    def click_on_the_button(self):
        return self.find_element(SeacrhLocators.Locator_Authorization_Button, time=2).click()

    def search_main_title(self):
        main_title = self.find_element(SeacrhLocators.Locator_Main_Title, time=2)
        return main_title

    def search_error_message(self):
        error_message = self.find_element(SeacrhLocators.Locator_Error_Message, time=2)
        return error_message
