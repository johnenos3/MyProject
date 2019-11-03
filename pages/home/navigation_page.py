import utilitie.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _menu_gamburger = "icon-header_menu"  # class
    _banner = "//*[@id='af-smart-banner']/div[1]"  # xpath
    _menu_profile = "side-nav__header" # class
    _menu_orders = "//*[@id='menu-orders']/div[2]"  # xpath
    _menu_neworder = "//*[@id='menu-neworder']/div[2]"  # xpath
    _menu_top_writers = "//*[@id='menu-top-writers']/div[2]"  # xpath
    _menu_testimonials = "//*[@id='menu-latest-orders']/div[2]"  # xpath
    _menu_support = "//*[@id='menu-tickets']/div[2]" #xpath
    _menu_balance = "//*[@id='menu-balance']/div[2]"  # xpath


    _menu_desktop = "//*[@id='menu-desktop']/div"
    _menu_how_it_works = "//*[@id='menu-how-it-works']/div"
    _menu_blog = "//*[@id='menu-blog']/div"
    _menu_about_us ="//*[@id='menu-about-us']/div"


    # Locators under class='side-nav__header':

    _menu_terms = "//*[@id='/terms-and-conditions.html']"
    _menu_privacy = "//*[@id='/privacy-policy.html']"
    _menu_moneyback = "//*[@id='/money-back-guarantee.html']"
    _menu_faq = "//*[@id='/customer-faq.html']"

    # _menu_logout = "profile__settings-item-logout" #class


    def navigateToMainMenu(self):
        self.elementClick(locator=self._menu_gamburger, locatorType="class")

    def navigateToProfile(self):
        self.elementClick(locator=self._menu_profile, locatorType="class")

    def clickBanner(self):
        self.elementClick(locator=self._banner, locatorType="xpath")

    def navigateToOrders(self):
        self.elementClick(locator=self._menu_orders, locatorType="xpath")

    def navigateToNewOrder(self):
        self.elementClick(locator=self._menu_neworder, locatorType="xpath")

    def navigateToTopWriters(self):
        self.elementClick(locator=self._menu_top_writers, locatorType="xpath")

    def navigateToTestimonials(self):
        self.elementClick(locator=self._menu_testimonials, locatorType="xpath")

    def navigateToSupport(self):
        self.elementClick(locator=self._menu_support, locatorType="xpath")

    def navigateToBalance(self):
        self.elementClick(locator=self._menu_balance, locatorType="xpath")



    def navigateToDesktop(self):
        self.elementClick(locator=self._menu_desktop, locatorType="xpath")

    def navigateToHowItworks(self):
        self.elementClick(locator=self._menu_how_it_works, locatorType="xpath")

    def navigateToBlog(self):
        self.elementClick(locator=self._menu_blog, locatorType="xpath")

    def navigateToAboutUs(self):
        self.elementClick(locator=self._menu_about_us, locatorType="xpath")



    def navigateToTerms(self):
        self.navigateToProfile()
        self.elementClick(locator=self._menu_terms, locatorType="xpath")

    def navigateToPrivacy(self):
        self.navigateToProfile()
        self.elementClick(locator=self._menu_privacy, locatorType="xpath")

    def navigateToMoneyBack(self):
        self.navigateToProfile()
        self.elementClick(locator=self._menu_moneyback, locatorType="xpath")

    def navigateToFaq(self):
        self.navigateToProfile()
        self.elementClick(locator=self._menu_faq, locatorType="xpath")














