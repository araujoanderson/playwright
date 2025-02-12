package com.saucedemo.tests;

import com.saucedemo.pages.LoginPage;
import org.testng.annotations.Test;
import org.testng.Assert;

public class LoginTest extends BaseTest {
    @Test
    public void testValidLogin() {
        LoginPage loginPage = new LoginPage(page);
        loginPage.navigate();
        loginPage.login("standard_user", "secret_sauce");
        Assert.assertTrue(page.locator(".inventory_list").isVisible(), "Login failed");
    }
}
