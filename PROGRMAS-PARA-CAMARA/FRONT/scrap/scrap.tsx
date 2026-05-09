import { chromium } from "npm:playwright";

export const get_html_content = async (url: string) => {   

    const browser = await chromium.launch({
    headless: true,
    args: [
    "--disable-blink-features=AutomationControlled",
  ],
   
    });

    const context = await browser.newContext({
    userAgent:
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    viewport: { width: 1920, height: 1080 },
    locale: "es-ES",
    });

    const page = await context.newPage();

    // Intentar ocultar que es automatizado
    await page.addInitScript(() => {
    Object.defineProperty(navigator, "webdriver", {
        get: () => false,
        
    });
    

  Object.defineProperty(navigator, "platform", {
    get: () => "Win32",
  });

  Object.defineProperty(navigator, "hardwareConcurrency", {
    get: () => 8,
  });

  Object.defineProperty(navigator, "deviceMemory", {
    get: () => 8,
  });
    // @ts-ignore
    window.chrome = {
        runtime: {},
    };
    Object.defineProperty(navigator, "languages", {
        get: () => ["es-ES", "es"],
    });
    Object.defineProperty(navigator, "plugins", {
        get: () => [1, 2, 3, 4, 5],
    });
    });
    await page.goto(
        url,
        { waitUntil: "domcontentloaded", timeout: 10000 }
    );

    // Esperar un poco
    await page.waitForTimeout(10000);

    console.log(page.url());
    console.log(await page.content());
    const valores = await page.locator("dl.labeled dd").allTextContents();
    console.log(valores);
   
    await browser.close();
     return valores;
};