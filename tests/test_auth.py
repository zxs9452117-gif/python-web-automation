from pages.login_page import LoginPage

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 斷言：檢查是否登入成功（網址是否包含 inventory）
    assert "inventory.html" in page.url