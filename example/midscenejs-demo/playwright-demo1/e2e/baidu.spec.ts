import { expect } from '@playwright/test';
import { test } from './fixture';

test.beforeEach(async ({ page }) => {
  page.setViewportSize({ width: 400, height: 905 });
  await page.goto('https://www.baidu.com');
  await page.waitForLoadState('networkidle');
});

test('search midscenejs on baidu', async ({
  ai,
  aiQuery,
  aiAssert,
  aiInput,
  aiTap,
  aiScroll,
  aiWaitFor,
  aiKeyboardPress,
}) => {
  // 使用 aiInput 输入搜索关键词
  await aiInput('midscenejs', '搜索框');

  // 使用 aiTap 点击百度一下按钮
  // await aiTap('百度一下');

  await aiKeyboardPress('Enter');
  await aiAssert('title包含"midscenejs"');
});