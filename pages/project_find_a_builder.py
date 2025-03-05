
class ProjectFindFBuilder:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://dev.godev.agency/projects/find-a-builder/')

    def get_url(self):
        current_url = self.driver.current_url
        return current_url