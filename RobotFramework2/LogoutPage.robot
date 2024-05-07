*** Settings ***
Documentation   To validate the Login form
Library     SeleniumLibrary
Resource    PathInfo.robot

*** Keywords ***
LogoutPage.Logout from WebPage
    Click Button    ${sign_out}

LogoutPage.Verify if logout Completed
    ${logouttext}    Get Text    ${logout_confirmation}
    Log    ${logouttext}
    Should Be Equal As Strings     ${logouttext}     Log in