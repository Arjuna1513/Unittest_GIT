class ScreenShot():
    def take_screen_shot(self, methodName, driver):
        driver.save_screenshot("..\screen_shots\\"+methodName+".png")