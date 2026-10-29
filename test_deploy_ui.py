import subprocess
import time
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="module", autouse=True)
def start_local_server():
    # 在背景啟動本地 HTTP Server 監聽 8000 Port
    server_process = subprocess.Popen(["python", "-m", "http.server", "8000"])
    time.sleep(1)  # 等待 Server 啟動完成
    yield
    server_process.terminate()  # 測試結束後關閉 Server

def test_homepage_content(page: Page):
    # 前往本地伺服器
    page.goto("http://127.0.0.1:8000")

    # 1. 驗證網頁 Title
    expect(page).to_have_title("My CI/CD Website")

    # 2. 驗證 H1 標題元件
    title_element = page.locator("#welcome-title")
    expect(title_element).to_contain_text("Welcome to My Automated Website!")

    # 3. 驗證部署狀態區塊標籤
    status_element = page.locator("#deploy-status")
    expect(status_element).to_be_visible()
    print("test")