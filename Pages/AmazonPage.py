class AmazonPage():

    # Locators of all the element

    def __init__(self,driver):
        self.driver = driver

        self.textbox_username_id = "twotabsearchtextbox"
        self.button_search_id = "nav-search-submit-button"
        self.button_analog_id = "p_n_feature_seven_browse-bin/1480900031"
        self.button_leather_id = "p_n_material_browse/1480907031"
        self.button_titan_id = "p_89/Titan"
        self.button_discount_id = "p_n_pct-off-with-tax/2665400031"
        self.button_fifth_xpath = "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[5]"

    def enter_username(self,username):
        self.driver.find_element_by_id("self.textbox_username_id").send_keys("username")

    def click_search(self):
        self.driver.find_element_by_id("self.button_search_id").click()

    def click_analog(self):
        self.driver.find_element_by_id("self.button_analog_id").click()

    def click_leather(self):
        self.driver.find_element_by_id("self.button_leather_id").click()

    def click_titan(self):
        self.driver.find_element_by_id("self.button_titan_id").click()

    def click_discount(self):
        self.driver.find_element_by_id("self.button_discount_id").click()

    def click_fifth(self):
        self.driver.find_element_by_id("self.button_fifth_xpath").click()





