*** Settings ***
Documentation    File which has all the login credentials data
Library    SeleniumLibrary
Test Template    LoginPage.Validate The Login
Resource    LoginPage.robot


*** Test Cases ***      username        password
TestCase1        kumar@abcd.com          Lokesh1231
TestCase2        kumar@abcde.com     Kumar123
