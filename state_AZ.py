# Arizona

from info import *
import cv2
import pytesseract

def state_AZ(web_accessor):
    #web_accessor.chrome.get('https://tableau.azdhs.gov/views/COVID-19Summary/Overview2?:embed=y&:showVizHome=no&:host_url=https%3A%2F%2Ftableau.azdhs.gov%2F&:embed_code_version=3&:tabs=no&:toolbar=no&:showAppBanner=false&:display_spinner=no&iframeSizedToWindow=true&:loadOrderID=0')
    #web_accessor.chrome.save_screenshot('screenshot.png')

    img = cv2.imread('screenshot.png')

    num_cases_img = img[50:190, 750:1050]
    num_cases = int(strip_commas(pytesseract.image_to_string(num_cases_img)))

    num_tests_img = img[50:190, 1550:1850]
    num_tests = int(strip_commas(pytesseract.image_to_string(num_tests_img)))

    return StateInfo('AZ', num_tests, num_tests-num_cases, num_cases)

    #cv2.imshow("num_cases", num_cases_img)
    #cv2.waitKey(0)
    #cv2.imshow("num_tests", num_tests_img)
    #cv2.waitKey(0)


