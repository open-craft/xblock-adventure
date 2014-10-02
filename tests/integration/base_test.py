from xblockutils.test_base import SeleniumBaseTest


class AdventureBaseTest(SeleniumBaseTest):
    module_name = __name__
    default_css_selector = 'div.adventure'
    relative_scenario_path = 'xml'
