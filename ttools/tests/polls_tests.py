from django.test import TestCase
import time
from selenium.webdriver.common.keys import Keys
import pytest


# def test_selenium(browser):
#     browser.get('http://www.python.org')
#     assert 'Python' in browser.title


def test_home_page(browser):
    browser.get('http://localhost:8000')
    assert 'To-Do List' in browser.title


def test_maths_work():
    assert 2 == 1+1

# YouTube: 1:23-1:35
def test_home_page_returns_correct_html(client):
    # Edith has heard about a cool new online to-do app. She goes
    # to check out its homepage
    response = client.get('/')

    # She notices the page title and header mention to-do lists
    assert response.content.decode().strip().startswith('<html>')
    assert '<title>To-Do Lists</title>' in response.content.decode()
    assert response.content.decode().strip().endswith('</html>')



# Youtube 1:35
# https://www.obeythetestinggoat.com/book/chapter_02_unittest.html

def test_can_start_a_list_and_retrieve_it_later(browser):
    assert 'To-Do' in browser.title
    header = browser.find_element_by_tag_name('h1')
    assert 'To-Do' in header.text


class HomePageTest(TestCase):

    def test_use_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')


@pytest.mark.django_db
def test_enter_todo_list_item_to_db(browser):
    inputbox = browser.find_element_by_id('id_new_item')
    assert 'Enter a to-do item' == inputbox.get_attribute('placeholder')
    inputbox.send_keys('Buy peacock feathers')
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)


def test_can_save_a_POST_request(client):
    response = client.post('/', data={'item_text': 'A new list item'})
    assert "A new list item" in response.content.decode()