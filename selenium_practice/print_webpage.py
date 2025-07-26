from selenium import webdriver
import time
import base64

driver = webdriver.Chrome()
driver.get("https://flask.palletsprojects.com/en/stable/tutorial/layout/")

# Open print dialog
pdf = driver.execute_cdp_cmd("Page.printToPDF", {
    "landscape": False,
    "displayHeaderFooter": False,
    "printBackground": True,
    "preferCSSPageSize": True
})

# Save to file
with open("output.pdf", "wb") as f:
    f.write(base64.b64decode(pdf['data']))

print("PDF saved as output.pdf")
driver.quit()
