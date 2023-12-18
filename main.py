# heroku profitcentr
from apscheduler.schedulers.background import BackgroundScheduler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from github import Github
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
from bs4 import BeautifulSoup
import os
from flask import Flask
import threading
import random
import re
account_number = 5
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, I'm your Flask app!"

port = int(os.environ.get("PORT", 5000))

def flask_thread():
    app.run(host="0.0.0.0", port=port)

def running():
    if os.path.exists("dsds.txt"):
        # Delete the file
            os.remove("dsds.txt")
    # your existing running() function
    # Use ChromeOptions directly
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    
    #options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Use context manager to handle the WebDriver instance
    with webdriver.Chrome(options=chrome_options) as driver1:
        #driver1.set_window_size(800, 600)
        #driver1.minimize_window()
        driver1.get("https://profitcentr.com/")
        new_window_size = {'width': 1552, 'height': 840}
        driver1.set_window_size(new_window_size['width'], new_window_size['height'])
        print("Please wait...")
        
        # Load cookies from file
        with open(f'account_{str(account_number)}.json', 'r') as f:
            cookies = json.load(f)
        #time.sleep(2)
        # Add cookies to the browser session
        for cookie in cookies:
            driver1.add_cookie(cookie)
        #time.sleep(2)
        # Refresh the page to apply cookies
        driver1.refresh()

       

        driver1.execute_script("window.scrollBy(0, 300);")
        time.sleep(1)


        

        links = driver1.find_elements(By.TAG_NAME,"a")

        target_part = "https://profitcentr.com/work-youtube?"

        # Check each link and print those that contain the target part
        for link in links:
            href = link.get_attribute("href")
            if href and target_part in href:
                urrl = str(href)
                #print(href)

        driver1.get(urrl)

        money = fgfg = WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.ID, "new-money-ballans"))).text

        print(money)
        rating = WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.ID, "reyt-user-block"))).text
        print(f"your rating: {rating}") 
     
            
        while True:
            try:
                elements = driver1.find_elements(By.CLASS_NAME, "out-capcha-lab")
               
                elements[2].click()
                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="maincolumn"]/div/div/div[2]/form/button'))).click()
                time.sleep(0.9)
                print("captcha solving..")
                  
            except:
                break
        
        try:
            WebDriverWait(driver1, 1).until(              
                        EC.presence_of_element_located((By.ID, "load-pages"))).click()
        except:
            pass
        v=20
        d=1
        while d < v:
            driver1.execute_script("window.scrollBy(0, 50);")
            time.sleep(0.2)
            d=d+1

        html_content = driver1.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        elements_with_id = soup.find_all(lambda tag: tag.has_attr('id'))
        for element in elements_with_id:
            with open("dsds.txt", 'a') as file:
                file.write(f"ID: {element['id']}\n")
        with open("dsds.txt", 'r') as file:
            content = file.read()
        matches = re.findall(r'ID: (start-ads-\d+)', content)
        if os.path.exists("dsds.txt"):
            os.remove("dsds.txt")
        random_number = random.randint(0, 10)
        dfgfg = matches[random_number]
        digits_only = re.findall(r'\d', dfgfg)
        result = ''.join(digits_only)
        print(result)      


        WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//*[@id='start-ads-{result}']/span[1]"))).click()
       
        time.sleep(1)

        
        element = driver1.find_element(By.ID, f"ads-lk-{result}")

        # Get and print the HTML code of the element
        html_code = element.get_attribute("outerHTML")
    


        match = re.search(r'id="check-task-(\d+)"', html_code)

        id_value1 = match.group(1)
     

        window_before = driver1.window_handles[0]

        time.sleep(1)

        WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.ID, f"check-task-{id_value1}"))).click()

        time.sleep(0.5)


        window_after = driver1.window_handles[1]
        driver1.switch_to.window(window_after)

        

        time.sleep(3)
       

        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(0.5)

        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(0.5)
      
        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(0.5)

        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(0.5)
        
        WebDriverWait(driver1, 70).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="succes-error"]/table/tbody/tr/td[2]/button'))).click()
        time.sleep(3)
        
          
        driver1.close()
        driver1.switch_to.window(window_before)

	#rating
        if int(rating) < 11:
            WebDriverWait(driver1, 70).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="maincolumn"]/div/div[1]/div[2]/a[4]'))).click()
            dvfdfg = WebDriverWait(driver1, 70).until(
                        EC.element_to_be_clickable((By.XPATH, ' //*[@id="maincolumn"]/div/div[1]/center/span[1]'))).text
            number_match = re.search(r'\d+', dvfdfg)
            extracted_number = int(number_match.group())
            print(f"today total views: {extracted_number}")
            if int(extracted_number) > 100:
                WebDriverWait(driver1, 70).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="maincolumn"]/div/div[1]/center/span[2]'))).click()
                time.sleep(1)
                WebDriverWait(driver1, 70).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="js-popup"]/form/div/input[1]'))).click()
              

        driver1.get("https://profitcentr.com/members")
                # Save cookies to a new file
        file_path = f'account_{str(account_number)}.json'
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} deleted successfully..")

        cookies = driver1.get_cookies()
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']

        new = f'account_{str(account_number)}.json'
        with open(new, 'w') as f:
            json.dump(cookies, f)

        print("Cookies copied successfully..")
        driver1.quit()

        time.sleep(7)

def sdsf():
    while True:
	    try:
  	 	    running()
	    except:
   		    continue


def updatee():
    owner = "ahmad344646"
    repo_name = "mycookies"
    file_path = f'account_{str(account_number)}.json'
    commit_message = 'Update file content'
    github_token = os.getenv("GITHUB_TOKEN")
    g = Github(github_token)
    repo = g.get_repo(f"{owner}/{repo_name}")
    # Get the current content of the file you want to update
    file = repo.get_contents(file_path)
    existing_file_content = file.decoded_content.decode('utf-8')
    with open(file_path, 'rb') as f1:
        new_content = f1.read()
    # Update the file on GitHub
    repo.update_file(
        path=file_path,
        message=commit_message,
        content=new_content,
        sha=file.sha,
        branch='main'  # Replace with your branch name
    )


# Start Flask in a separate thread
flask_thread = threading.Thread(target=flask_thread)
flask_thread.start()




scheduler1 = BackgroundScheduler()
scheduler1.add_job(updatee, 'interval', seconds=600)  # run every 5 minutes
scheduler1.start()

flask_thread1 = threading.Thread(target=sdsf)
flask_thread1.start()






if __name__ == '__main__':
    # This block will only be executed when the script is run directly, not when imported
    try:
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        scheduler.shutdown()
