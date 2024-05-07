*** Settings ***
Documentation    A Generic  file with reusable keywords and variables
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/client

*** Keywords ***
DriverURLInfo.open the browser
    Create Webdriver    Firefox   executable_path="E:\\Selenium3\\geckodriver.exe"
    Go To    ${url}

DriverURLInfo.Close the Login Browser
    Close Browser