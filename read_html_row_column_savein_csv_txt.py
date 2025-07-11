from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(4)

# Get column headers and row data
no_of_col = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th')
no_rows = driver.find_elements(By.XPATH, "//table[@name = 'BookTable']//tr")

# Open a file to write (text file)
with open("web_table_data.txt", "w", encoding="utf-8") as f:
    f.write("Column Headers:\n")
    for col in no_of_col:
        f.write(col.text + "\t")
    f.write("\n\nRows:\n")

    for row in no_rows:
        f.write(row.text + "\n")

print("Data written to web_table_data.txt")

print(f"Columns count: {len(no_of_col)}")
print(f"Rows count: {len(no_rows)}")

import csv

# Open a CSV file to write
with open("web_table_data.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write column headers
    headers = [col.text for col in no_of_col]
    writer.writerow(headers)
    
    # Write rows (skip header row to avoid duplication)
    for row in no_rows[1:]:  # skipping first row (already in headers)
        cells = row.find_elements(By.TAG_NAME, "td")
        writer.writerow([cell.text for cell in cells])

print("Data written to web_table_data.csv")

driver.quit()
