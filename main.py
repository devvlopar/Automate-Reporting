from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

#-------------------TODAYS---ATTENDANCE-------------------------#
list1 = [15,16,17,18,19,20,21,22,23,24,29,30,14,10]


all_studets = [
    [],
    ['JENIL' , 270583],
    ['khushal' , 270291],
    ['krishil' , 269700],
    ['kiran' , 260214],
    ['jagruti' , 272328],
    ['Pratixa' , 242468],
    ['rinkal' , 273459],
    ['vijay' , 275427],
    ['Papu' , 272260],
    ['Harekrishna' , 242278],
    ['khushal' , 270291],
    ['sweta' , 268310],
    ['Dhruv' , 278735],
    ['Ankit' , 265202],
    ['Mitesh' , 280623],
    ['Ashwini' , 283803],
    ['Jogendra' , 283090],
    ['Murari' , 283804],
    ['Avinash' , 283540],
    ['Divyesh' , 279309],
    ['krrisha' , 274735],
    ['ansh' , 265856],
    ['Jay' , 281533],
    ['Meet' , 283214],
    ['Chintan' , 284214],
    ['Dhaval' , 274674],
    ['Vilas' , 283930],
    ['Umang' , 282261],
    ['Jigar' , 284579],
    ['Kartik' , 282921],
    ['Darshil' , 276173],
    ['Rajat' , 277406],
    ['Yugkumar', 260489]
]

weird_std_nums = []

for i in list1:
    weird_std_nums.append(str(all_studets[i][-1]))


fox_location = '/usr/bin/chromium'

s=Service(ChromeDriverManager().install())
op = webdriver.ChromeOptions()
op.add_argument("start-maximized")
op.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s, options= op)
driver.maximize_window()
driver.get('https://topsint.com/topserp')


#-------------------- Login Process --------------------#
dropdown = Select(driver.find_element(By.ID,'lutype'))
dropdown.select_by_value('4')

username = driver.find_element(By.ID,'l_username')
username.send_keys('devang_srt')

passwd = driver.find_element(By.NAME,'l_password')
passwd.send_keys('#Otis1509')

form = driver.find_element(By.NAME,'btn_login').click()
#----------------Successfully Logged-In-----------------#


#--------------Getting Today's Schedule-----------------#
driver.get('https://topsint.com/topserp/faculty/daily_report.php')

all_batches_names = []
for batch_num in range(2,20):
    table = driver.find_element(By.XPATH,(f"//table[@class='content']/tbody/tr[{batch_num}]/td"))
    if table.text == '':
        break
    all_batches_names.append(((table.text).split(' ',1))[1])

#--------------------Debugging Shit---------------------#
# print('total batches:',len(all_batches_names))
# print(all_batches_names)
#--------------------Debugging Shit---------------------#


for batch_name in all_batches_names:

#-------------------Selecting Batch Name----------------#
    select_batch = Select(driver.find_element(By.ID,'ddl_batch'))
    try:
        select_batch.select_by_visible_text(batch_name)
    except:
        continue


#------------------BATCHPOINT---------START---------BATCHPOINT-------------------------BATCHPOINT------------------#

    if batch_name.startswith('03Aug'):
        driver.find_element(By.CSS_SELECTOR,"input#lecture_status_taken").click()

        #---------------------Selecting Module------------------#
        select_module = Select(driver.find_element(By.ID, 'ddl_module'))
        for i in select_module.options:
            if ('DB' in i.text) and ('Python' in i.text) or ('Introduction to Python' in i.text):
                select_module.select_by_visible_text(i.text)
                break

        #---------------------Selecting Topics------------------#
        select_topics = Select(driver.find_element(By.ID, 'ddl_topic'))
        total_topics = len(select_topics.options)

        for i in (select_topics.options):
            mid_point = total_topics//2
            if (list(select_topics.options)).index(i) <= mid_point:
                select_topics.select_by_visible_text(i.text)

        #------------------Topic Completed Or Not---------------#
        topic_status = Select(driver.find_element(By.ID, 'txt_topic_status'))
        topic_status.select_by_value("No")

#------------------BATCHPOINT---------END-----------BATCHPOINT-------------------------BATCHPOINT------------------#




#------------------BATCHPOINT--------START----------BATCHPOINT-------------------------BATCHPOINT------------------#

    if batch_name.startswith('26Aug') or batch_name.startswith('10Oct'):
        driver.find_element(By.CSS_SELECTOR,"input#lecture_status_taken").click()

        #---------------------Selecting Module------------------#
        select_module = Select(driver.find_element(By.ID, 'ddl_module'))
        for i in select_module.options:
            if ('Advance' in i.text) and ('Python' in i.text) or ('Introduction to Python' in i.text):
                select_module.select_by_visible_text(i.text)
                break

        #---------------------Selecting Topics------------------#
        select_topics = Select(driver.find_element(By.ID, 'ddl_topic'))
        total_topics = len(select_topics.options)

        for i in (select_topics.options):
            mid_point = total_topics//2
            if (list(select_topics.options)).index(i) > mid_point:
                select_topics.select_by_visible_text(i.text)

        #------------------Topic Completed Or Not---------------#
        topic_status = Select(driver.find_element(By.ID, 'txt_topic_status'))
        topic_status.select_by_value("No")

#------------------BATCHPOINT----------END----------BATCHPOINT-------------------------BATCHPOINT------------------#




#------------------BATCHPOINT--------START----------BATCHPOINT-------------------------BATCHPOINT------------------#

    if batch_name.startswith('23Sep'):
        driver.find_element(By.CSS_SELECTOR,"input#lecture_status_taken").click()

        #---------------------Selecting Module------------------#
        select_module = Select(driver.find_element(By.ID, 'ddl_module'))
        
        for i in select_module.options:
            if (('Advance' in i.text) and ('Python' in i.text)) or ('Introduction to Python' in i.text):
                select_module.select_by_visible_text(i.text)
                break
        
        #---------------------Selecting Topics------------------#
        select_topics = Select(driver.find_element(By.ID, 'ddl_topic'))
        total_topics = len(select_topics.options)

        for i in (select_topics.options):
            mid_point = total_topics//2
            if (list(select_topics.options)).index(i) > mid_point:
                select_topics.select_by_visible_text(i.text)
    
        #------------------Topic Completed Or Not---------------#
        topic_status = Select(driver.find_element(By.ID, 'txt_topic_status'))
        if 'Data' in batch_name:
            topic_status.select_by_value("No")
        else:
            topic_status.select_by_value("No")

#------------------BATCHPOINT---------END-----------BATCHPOINT-------------------------BATCHPOINT------------------#




#------------------BATCHPOINT--------START----------BATCHPOINT-------------------------BATCHPOINT------------------#

    if batch_name.startswith('03Dec') or batch_name.startswith('17Nov'):
        driver.find_element(By.CSS_SELECTOR,"input#lecture_status_taken").click()

        #---------------------Selecting Module------------------#
        select_module = Select(driver.find_element(By.ID, 'ddl_module'))
        
        for i in select_module.options:
            if (('Fundamentals' in i.text) and ('Python' in i.text)) or ('Introduction to Python' in i.text):
                select_module.select_by_visible_text(i.text)
                break

        #---------------------Selecting Topics------------------#
        select_topics = Select(driver.find_element(By.ID, 'ddl_topic'))
        total_topics = len(select_topics.options)

        for i in (select_topics.options):
            mid_point = total_topics//2
            if (list(select_topics.options)).index(i) > mid_point:
                select_topics.select_by_visible_text(i.text)

        #------------------Topic Completed Or Not---------------#
        topic_status = Select(driver.find_element(By.ID, 'txt_topic_status'))
        if 'Data' in batch_name:
            topic_status.select_by_value("No")
        else:
            topic_status.select_by_value("Yes")

#------------------BATCHPOINT----------END----------BATCHPOINT-------------------------BATCHPOINT------------------#




#------------------BATCHPOINT--------START----------BATCHPOINT-------------------------BATCHPOINT------------------#

    if batch_name.startswith('12Dec'):
        driver.find_element(By.CSS_SELECTOR,"input#lecture_status_taken").click()

        #---------------------Selecting Module------------------#
        select_module = Select(driver.find_element(By.ID, 'ddl_module'))
        
        for i in select_module.options:
            if (('Fundamentals' in i.text) and ('Python' in i.text)) or ('Introduction to Python' in i.text):
                select_module.select_by_visible_text(i.text)
                break

        #---------------------Selecting Topics------------------#
        select_topics = Select(driver.find_element(By.ID, 'ddl_topic'))
        total_topics = len(select_topics.options)

        for i in (select_topics.options):
            mid_point = total_topics//2
            if (list(select_topics.options)).index(i) <= mid_point:
                select_topics.select_by_visible_text(i.text)
        
        #------------------Topic Completed Or Not---------------#
        topic_status = Select(driver.find_element(By.ID, 'txt_topic_status'))
        topic_status.select_by_value("No")
            
#------------------BATCHPOINT---------END-----------BATCHPOINT-------------------------BATCHPOINT------------------#




#------------------BATCHPOINT---------START---------BATCHPOINT-------------------------BATCHPOINT------------------#

    if batch_name.startswith('26Dec'):
        driver.find_element(By.CSS_SELECTOR,"input#lecture_status_taken").click()
    
        #---------------------Selecting Module------------------#
        select_module = Select(driver.find_element(By.ID, 'ddl_module'))
        
        for i in select_module.options:
            if (('Fundamentals' in i.text) and ('Python' in i.text)) or ('Introduction to Python' in i.text):
                select_module.select_by_visible_text(i.text)
                break

        #---------------------Selecting Topics------------------#
        select_topics = Select(driver.find_element(By.ID, 'ddl_topic'))
        total_topics = len(select_topics.options)

        for i in (select_topics.options):
            mid_point = total_topics//2
            if (list(select_topics.options)).index(i) <= mid_point:
                select_topics.select_by_visible_text(i.text)

        #------------------Topic Completed Or Not---------------#
        topic_status = Select(driver.find_element(By.ID, 'txt_topic_status'))
        topic_status.select_by_value("No")

#------------------BATCHPOINT---------END-----------BATCHPOINT-------------------------BATCHPOINT------------------#




#------------------BATCHPOINT---------START---------BATCHPOINT-------------------------BATCHPOINT------------------#

    if batch_name.startswith('26Sep'):
        driver.find_element(By.CSS_SELECTOR,"input#lecture_status_cancel").click()
    
        #---------------------Selecting Module------------------#
        select_module = Select(driver.find_element(By.ID, 'ddl_reason'))
        select_module.select_by_value("Lecture completed, Assignments pending")
        
        #----------------------Text Box Reason------------------#
        select_topics = driver.find_element(By.NAME, 'txta_reason').send_keys('Need to transfer this student.')


        #------------------Submitting One Batch-----------------#
        submit_batch = driver.find_element(By.ID, 'btn_submit').click()
        time.sleep(3)
        continue

#------------------BATCHPOINT---------END-----------BATCHPOINT-------------------------BATCHPOINT------------------#


    

#---------------GENERAL STUFF STARTED--------------GENERAL STUFF STARTED-------------------------------------------#

#-----------------------Total Hours---------------------#
    sel_hour = Select(driver.find_element(By.ID, 'ddl_hour'))
    sel_hour.select_by_value("01")
    sel_min = Select(driver.find_element(By.ID, 'ddl_minute'))
    sel_min.select_by_value("30")

#--------------Checking Present Students----------------#
    all_chks = driver.find_elements(By.NAME, 'chk_std[]')
    time.sleep(2)

    for single_chk in all_chks:
        single_chk_val = single_chk.get_attribute("value")
        if single_chk_val in weird_std_nums:
            single_chk.click()

#------------------Submitting One Batch-----------------#
    submit_batch = driver.find_element(By.ID, 'btn_submit').click()
    time.sleep(3)



#----------------------READY TO SEND-----READY TO SEND-----READY TO SEND--------------------------#


sent = driver.find_element(By.NAME, 'btn_send').click()
time.sleep(5)

try:
    mail_sent = driver.find_element(By.NAME, "btn_sendmaildaily_t").click()
except:
    mail_sent = driver.find_element(By.ID, "btn_sendmaildaily_t").click()

