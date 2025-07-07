from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import time

def run_test(thread_id, url):
    driver = webdriver.Chrome()
    driver.get(url)

    print(f"[Thread {thread_id}] Title: {driver.title}")
    time.sleep(2)  # simulate test steps

    driver.quit()

# List of URLs to test
urls = ["https://example.com", "https://google.com", "https://github.com"]

threads = []

# Launch a thread per URL
for i, url in enumerate(urls):
    t = threading.Thread(target=run_test, args=(i + 1, url))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("✅ All tests completed.")
