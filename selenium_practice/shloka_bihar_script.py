













def bihar_auto(district,anchal,mauja,halka,khata_number,jamabandi_sankhya,fname,lname,user_id,u_date,epp_user_id,bhag_vartman,pusht_sankhya_number):
    try:
        pa_th = os.path.join(script_dir, u_date+'_'+'bihar'+'_'+'0', fname+'_'+lname+'_'+str(user_id))
        os.makedirs(pa_th, exist_ok=True)    
        #Set up driver
        driver = webdriver.Chrome()
        driver.get('https://parimarjan.bihar.gov.in/BiharBhumiReport/ViewJamabandi')
        logger.info("DRIVER OPEN")
        time.sleep(1)
 
        pid = driver.service.process.pid
        #Explicit wait Object
        wait=WebDriverWait(driver, 180)
 
        #Select district
        logger.info(f"District->{district}")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ddlDistrict"]/option[2]')))
        dis = select_dropdown_option(driver, '//*[@id="MainContent_ddlDistrict"]', district, pid)
        if not dis:
            return [f'District-{district} not found']
           
        #Select anchal
        logger.info(f"Anchal->{anchal}")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ddlCircle"]/option[2]')))
        anch = select_dropdown_option(driver, '//*[@id="MainContent_ddlCircle"]',anchal, pid)
        if not anch:
            return [f'Anchal-{anchal} not found']
 
        time.sleep(1)
        #Click on proceed button
        logger.info("Proceed")
        driver.find_element(By.XPATH,'//*[@id="MainContent_btnproceed"]').click()
 
        #Select halka
        logger.info(f"Halka->{halka}")
        halka=str(halka).strip()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ddlHalka"]/option[2]')))
        # time.sleep(3)
        hal = select_dropdown_option(driver, '//*[@id="MainContent_ddlHalka"]',halka, pid)
        if not hal:
            return [f'Halka-{halka} not found']
 
        #Select Mauja
        logger.info(f"Mauja->{mauja}")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_ddlMauja"]/option[2]')))
        # time.sleep(3)
        mau = select_dropdown_option(driver, '//*[@id="MainContent_ddlMauja"]',mauja, pid)
        if not mau:
            return [f'Mauja-{mauja} not found']
       
        logger.info(f'{jamabandi_sankhya}--jamabandi sankhya')
        time.sleep(1)
 
        if bhag_vartman is not None and pusht_sankhya_number is not None:
            try:
                def select_bhag():
                    logger.info('Bhag vartman')
                    time.sleep(2)
                    driver.find_element(By.XPATH,'//*[@id="MainContent_rdo_Volume"]').click()
                    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_txt_Volume"]'))).click()
                    time.sleep(2)
                    driver.find_element(By.XPATH,'//*[@id="MainContent_txt_Volume"]').send_keys(bhag_vartman)
                    time.sleep(3)
                    logger.info('Bhag vartman selectedddddddd')
                    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MainContent_txt_PageNo"]'))).click()
                    time.sleep(2)
                    driver.find_element(By.XPATH,'//*[@id="MainContent_txt_PageNo"]').send_keys(pusht_sankhya_number)
                    time.sleep(2)
                    logger.info('Pusht Sankhya selectedddddddd')
                select_bhag()
            except Exception as e:
                select_bhag()
 
            #Captchaaaaaaa
            time.sleep(2)
            captcha_1 = driver.find_element(By.XPATH,'//*[@id="MainContent_TextBox1"]').get_attribute('value')
            captcha_2 = str(captcha_1).split(' + ')
            captchasol = int(captcha_2[0]) + int(captcha_2[1])
            time.sleep(1)
            #Sending solved captcho
            driver.find_element(By.ID,'MainContent_TextBox2').send_keys(captchasol)
            time.sleep(2)
 
            #Submit Button
            submit = driver.find_element(By.XPATH,'//*[@id="MainContent_btnSearch"]')
            driver.execute_script("arguments[0].click();", submit)
 
        else:
            driver.quit()
            logger.info('CLOSED DRIVER')
            return [f'Bhag Vartman--{bhag_vartman} or Pusht Sankhya--{pusht_sankhya_number} Number Not Found!!!']
            
 
 
    except (NoSuchElementException,Exception,OSError,SyntaxError,TypeError,KeyError,NameError,ValueError) as e:
        logger.error(f"ERROR---{e}")
        # kill_process_and_children(pid)
        driver.quit()
        logger.info('CLOSED DRIVER')
        return ['Error In Automation']
   
    #DOCUMENT EXTRACTION---
    extraction=bihar_extraction(district,anchal,mauja,halka,khata_number,jamabandi_sankhya,fname,lname,user_id,u_date,epp_user_id,driver,pid,wait,bhag_vartman,pusht_sankhya_number)
    return extraction
       
def bihar_extraction(district,anchal,mauja,halka,khata_number,jamabandi_sankhya,fname,lname,user_id,u_date,epp_user_id,driver,pid,wait,bhag_vartman,pusht_sankhya_number):
    try:
        logger.info(f"Khata Number--{khata_number},Bhag Vartman--{bhag_vartman},Pusht_sankhya---{pusht_sankhya_number}")
        time.sleep(4)
        no_data = ''
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="MainContent_Updatepanel1"]/div/div/div[2]/div[6]')))
            no_data = driver.find_element(By.XPATH, '//*[@id="MainContent_Updatepanel1"]/div/div/div[2]/div[6]').text.strip()
            logger.info(f'Extracted no_data text: "{no_data}"')  # Debugging line
        except Exception as e:
            logger.error(f'getting error in no data present try except {e}')
   
        if no_data in ['डेटा उपलब्ध नहीं है।']:
            logger.info(f'DATA IS NOT AVAILABLE - {no_data}')
            driver.quit()
            logger.info('CLOSED DRIVER')
            return ['DATA IS NOT AVAILABLE']
        else:
            logger.info(f'Data is available, starting extraction--{no_data}')
 
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="MainContent_ddl_view"]')))
        logger.info('SELECTING VIEWWWWWWWWWW 500 from dropdown')
        view = select_dropdown_option(driver, '//*[@id="MainContent_ddl_view"]',"500", pid)
        # if not view:
        #     print("Can't viiew till 500")
        logger.info('SELECTed VIEWWWWWWWWWW 500 from dropdown')
 
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div[5]/div[3]/div/div/div/div/div/div[3]/div[2]/table/tbody/tr/td[3]')))
        time.sleep(2)
        khata_numbers=driver.find_elements(By.XPATH,'/html/body/form/div[5]/div[3]/div/div/div/div/div/div[3]/div[2]/table/tbody/tr/td[3]')
        logger.info(f"Khata numbers--------{len(khata_numbers)}")
 
        khata_number_check=str(khata_number).split(',')
        summary="DONE"
        khata,bhag_vartman_site,pusht_sankhya_number_site=0,0,0
        for i in range(len(khata_numbers)):
            khata_element=driver.find_element(By.XPATH,f'/html/body/form/div[5]/div[3]/div/div/div/div/div/div[3]/div[2]/table/tbody/tr[{i+2}]/td[3]/span')
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", khata_element)
            time.sleep(3)
            khata=khata_element.text
            logger.info(f"Khata number--------{(khata)}")
            time.sleep(1)
            bhag_vartman_site=driver.find_element(By.XPATH,f'/html/body/form/div[5]/div[3]/div/div/div/div/div/div[3]/div[2]/table/tbody/tr[{i+2}]/td[4]/span').text
            pusht_sankhya_number_site=driver.find_element(By.XPATH,f'/html/body/form/div[5]/div[3]/div/div/div/div/div/div[3]/div[2]/table/tbody/tr[{i+2}]/td[5]/span').text
 
            logger.info(f"Khata Number--{khata},Bhag Vartman--{bhag_vartman_site},Pusht_sankhya---{pusht_sankhya_number_site}")
            time.sleep(2)
            khata=khata.split(',')
            logger.info(f"Khata number of the loop is ----{khata}")
            if not isinstance(khata, list):
                logger.info("Inside of is instance!!")
                khata = [khata]
            time.sleep(3)
            print("=======================////////??????",khata, khata_number_check)
            if all(elem in khata_number_check for elem in khata) and (bhag_vartman_site.strip()==bhag_vartman.strip()) and (pusht_sankhya_number_site.strip()==pusht_sankhya_number.strip()):
            
                logger.info(f'Khata number matched--{khata} , Bhag vartam matched--{bhag_vartman_site} or Pusht sankhya number matched--{pusht_sankhya_number_site}')
                time.sleep(3)
                logger.info("FOUND KHATA NUMBERR")
                wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/form/div[5]/div[3]/div/div/div/div/div/div[3]/div[2]/table/tbody/tr[{i+2}]/td[8]/a/img')))
                time.sleep(3)
                search_button = driver.find_element(By.XPATH,f'/html/body/form/div[5]/div[3]/div/div/div/div/div/div[3]/div[2]/table/tbody/tr[{i+2}]/td[8]/a/img')
                driver.execute_script("arguments[0].click()", search_button)
                time.sleep(4)
                logger.info('CLICKED ON EYE ICON')
                alert_count = 0
                while alert_count < 3:
                    try:
                        alert = driver.switch_to.alert
                        logger.info(f"Alert detected: {alert.text}")
                        alert.accept()
                        logger.info("Alert accepted.")
                        time.sleep(2)  # Allow time for page to reload after accepting alert\
                        wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/form/div[5]/div[3]/div/div/div/div/div/div[3]/div[2]/table/tbody/tr[{i+2}]/td[8]/a/img')))
                        search_button = driver.find_element(By.XPATH,f'/html/body/form/div[5]/div[3]/div/div/div/div/div/div[3]/div[2]/table/tbody/tr[{i+2}]/td[8]/a/img')
                        driver.execute_script("arguments[0].click()", search_button)
                        time.sleep(4)
                        alert_count+=1
                    except:
                        logger.info('NO ALERT!!!!')
                        break  
 
               
                a = driver.current_window_handle
                a1 = driver.window_handles
 
               
                for i in a1:
                    if i != a:
                        driver.switch_to.window(i)
                        # driver.maximize_window()
 
                        print_options = {
                                "landscape": False,  # Portrait mode
                                "displayHeaderFooter": False,  # No header/footer
                                "printBackground": True,  # Include background graphics
                                "preferCSSPageSize": True,  # Use CSS-defined page size
                            }
                        pdf_data = driver.execute_cdp_cmd("Page.printToPDF", print_options)
 
                        try:
                            logger.info("------------------DATA------------------")
                    
                            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="lblOwnerName"]')))
                            time.sleep(3)
                            owner_name=driver.find_element(By.XPATH,'//*[@id="lblOwnerName"]').text
                            logger.info(f"OWNER NAME ->{owner_name}")
    
    
                            all_khata_numbers_in_document=driver.find_elements(By.XPATH,'/html/body/form/div[3]/div[2]/div/div/div[6]/div/table/tbody/tr/td[1]/a')
                            khata_numbers_in_document=[]
                            for i in range(len(all_khata_numbers_in_document)):
                                khat=driver.find_element(By.XPATH,f'/html/body/form/div[3]/div[2]/div/div/div[6]/div/table/tbody/tr[{i+2}]/td[1]/a').text
                                khata_numbers_in_document.append(khat)
    
                            logger.info(f"Khata Numbers Fetched from document are--{khata_numbers_in_document}")
    
                            all_plot_numbers_in_document=driver.find_elements(By.XPATH,'/html/body/form/div[3]/div[2]/div/div/div[6]/div/table/tbody/tr/td[2]/a')
                            plot_numbers_in_document=[]
    
                            for i in range(len(all_plot_numbers_in_document)):
                                plot=driver.find_element(By.XPATH,f'/html/body/form/div[3]/div[2]/div/div/div[6]/div/table/tbody/tr[{i+2}]/td[2]/a').text
                                plot_numbers_in_document.append(plot)
    
                            logger.info(f"Plot Numbers Fetched from document are--{plot_numbers_in_document}")
    
                            total_area=driver.find_element(By.XPATH,f'/html/body/form/div[3]/div[2]/div/div/div[6]/div/table/tbody/tr[{len(all_plot_numbers_in_document)+2}]/td[3]').text
                            logger.info(f"TOTAL AREA ->{total_area}")
    
                            change_in_assessment=driver.find_element(By.XPATH,'//*[@id="divMain"]/div[7]/div').text
                            logger.info("OTHER PROPERTY-SPECIFIC DETAILS ->")
                            change_in_assessment_from_doc=change_in_assessment.split('\n')
    
                            change_in_assessment=[]
                            for i in change_in_assessment_from_doc[1:]:
                                # i=remove_blank_strings(i)
                                i=tuple(i.split())
                                change_in_assessment.append(i)
    
                            change_in_assessment=f"{change_in_assessment}"
                            logger.info(f'{change_in_assessment}')
    
                            mutation=driver.find_element(By.XPATH,'//*[@id="divHeader12"]/table/tbody/tr').text
                            case_entry=[]
                            if "not" in mutation.lower():
                                mutation="Mutation Cases Not Found !!"
                                logger.info("Mutation Cases Not Found !!")
                            else:
                                mutation="Mutation Cases Found !!"
                                logger.info("Mutation Cases Found !!")
                                i=2
                                while True:
                                    try:
                                        case=driver.find_element(By.XPATH,f'/html/body/form/div[3]/div[2]/div/div/div[9]/div[2]/div/div/table/tbody/tr[{i}]/td[2]').text
                                        case_entry.append(case)
                                        i=i+1
                                    except Exception as e:
                                        break
 
                                logger.info(f'CASES FOUND ARE----{case_entry}')
                                        
 
 
                            logger.info("------------------X------------------")
                        except:
                            driver.quit()
                            logger.info('CLOSED DRIVER')
                            return['Error In Extraction']
 
 
                        pa_th = os.path.join(script_dir, u_date+'_'+'bihar'+'_'+'0', fname+'_'+lname+'_'+str(user_id))
                        os.makedirs(pa_th, exist_ok=True)
 
                        mauja_name=mauja.replace('/','_')
                        halka_name=halka.replace('/','_')
                        anchal_name=anchal.replace('/','_')
                        district_name=district.replace('/','_')
 
                        with open(f'{pa_th}/{district_name}_{anchal_name}_{halka_name}_{mauja_name}_{bhag_vartman}_{pusht_sankhya_number}_712.pdf', "wb") as pdf_file:
                            pdf_file.write(base64.b64decode(pdf_data["data"]))
                        #------S3 BUCKET CODE HERE-----
                        pdf_name = 'Congress_Committee_1' + '/' + district_name + '_' + anchal_name + '_' + halka_name + '_' +mauja_name + '_' + bhag_vartman + '_' +pusht_sankhya_number + '_712.pdf'
                        local_file_path=os.path.join(script_dir,u_date+'_'+'bihar'+'_'+'0',pdf_name)
                        logger.info(f'{pdf_name}--pdf name')
                        logger.info(f'{local_file_path}---localfile path')
                        url  = upload_to_s3(u_date+'_'+'bihar'+'_'+'0',pdf_name,local_file_path)
                        logger.info(f'{url}---url')
                        logger.info(url[0])
                        url=url[0]
                   
                        logger.info(f"Webpage saved as PDF at : {district_name}_{anchal_name}_{halka_name}_{mauja_name}_{bhag_vartman}_{pusht_sankhya_number}_712.pdf ")
                        driver.close()
                    time.sleep(2)
               
                driver.switch_to.window(a)
                driver.quit()
                logger.info('CLOSED DRIVER')
                logger.info('EXTRACTION DONE !!')
                
                return[u_date,owner_name,khata_numbers_in_document,plot_numbers_in_document,total_area,change_in_assessment,mutation,url,pusht_sankhya_number_site,bhag_vartman_site,case_entry]
            else:
                logger.info(f'Khata number not matched--{khata} , Bhag vartam not matched--{bhag_vartman_site} or Pusht sankhya number--{pusht_sankhya_number_site}')
       
        if khata==0 or bhag_vartman_site==0 or pusht_sankhya_number_site==0:
            return['Error In Extraction']
        driver.quit()
        logger.info('CLOSED DRIVER')
        return[u_date,owner_name,khata_numbers_in_document,plot_numbers_in_document,total_area,change_in_assessment,mutation,url,pusht_sankhya_number_site,bhag_vartman_site,case_entry]
       
   
    except (NoSuchElementException,Exception,OSError,SyntaxError,TypeError,KeyError,NameError,ValueError) as e:
        traceback_details = ''.join(traceback.format_exception(*sys.exc_info()))
        logger.error(f"Error occured: {traceback_details}")
        logger.error(f"ERROR---{e}")
        # kill_process_and_children(pid)
        driver.quit()
        logger.info('CLOSED DRIVER')
        return ['Error In Extraction']
 