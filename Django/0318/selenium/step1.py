from selenium import webdriver

# 조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다
driver = webdriver.Chrome()

# 브라우저의 위치를 조정합니다. 수업용으로 세팅해놓은 것입니다.
driver.set_window_position(2000, 0)

# webdriver가 google 페이지에 접속하도록 명령
driver.get("https://www.google.com")

# webdriver를 종료하여 창이 사라진다
driver.close()
