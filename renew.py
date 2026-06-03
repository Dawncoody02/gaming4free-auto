import os, sys, time, urllib.request, json
from seleniumbase import SB

# ==========================================
# 💡 核心配置 (G4F.GG 终极物理外挂版)
# ==========================================
TARGET_URL = "https://g4f.gg/renqi" 
MC_USERNAME = "renqi"

TG_TOKEN = os.getenv("TG_TOKEN", "")
TG_CHAT = os.getenv("TG_CHAT_ID", "")

def send_tg(msg):
    if TG_TOKEN and TG_CHAT:
        try:
            url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
            data = json.dumps({"chat_id": TG_CHAT, "text": f"🤖 G4F 自动续期:\n{msg}"}).encode('utf-8')
            req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
            urllib.request.urlopen(req, timeout=10)
        except:
            pass

print(f"\n===== 🚀 开始执行极速续期 (终极物理盲狙版) =====")

proxy_str = "socks5://127.0.0.1:40000"

# 🌟 核心修复：直接在启动时强行锁死 1920x1080 分辨率，绝对不调用会导致崩溃的 maximize_window！
with SB(uc=True, proxy=proxy_str, headless=False, window_size="1920,1080") as sb:
    try:
        print("⏳ 正在为虚拟显示器安装 xdotool 物理鼠标引擎...")
        os.system("sudo apt-get update > /dev/null 2>&1")
        os.system("sudo apt-get install -y xdotool > /dev/null 2>&1")

        print(f"🌐 正在通过 WARP 访问新版目标网址: {TARGET_URL}")
        sb.open(TARGET_URL)
        sb.sleep(6) 
        
        os.makedirs("screenshots", exist_ok=True)
        sb.save_screenshot("screenshots/1_page_loaded.png")

        print("✍️ 尝试填入游戏ID (OPTIONAL)...")
        try:
            sb.type('input[placeholder*="Steve"], input[placeholder*="Player"]', MC_USERNAME, timeout=4)
            print("✅ ID 填入成功！")
        except:
            print("ℹ️ 未找到输入框或无需填入，继续下一步。")

        print("🚀 触发 [+ ADD 90 MIN] 核心按钮...")
        js_click_code = """
        let clicked = false;
        let els = document.querySelectorAll('button, a, input, div, span');
        for (let i = els.length - 1; i >= 0; i--) {
            let el = els[i];
            let text = (el.innerText || el.value || '').toUpperCase();
            if (text.includes('ADD 90')) {
                el.click();
                clicked = true;
                break;
            }
        }
        return clicked;
        """
        is_clicked = sb.execute_script(js_click_code)
        if not is_clicked:
            sb.click('xpath=//*[contains(translate(., "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "add 90")]')

        print("⏳ 盲等 6 秒钟，等待 CF 盾在屏幕正中央展开...")
        print("⚠️ [系统警告] 已切断所有 WebDriver 探针，开启静默隐身模式！")
        time.sleep(6) 
        
        print("🛡️ 启动【全盲物理狙击】模块，准备跨维度开火！")
        
        # 🌟 既然分辨率锁死了 1920x1080，直接计算物理坐标，免去复杂的探测！
        w, h = 1920, 1080
        target_x = (w // 2) - 80   # 弹窗居中，复选框偏左
        target_y = (h // 2) + 30   # 抵消浏览器顶部导航栏的偏移
        
        print(f"🎯 锁定屏幕绝对坐标: ({target_x}, {target_y})")
        print("🖱️ 物理鼠标按下扳机！")
        
        # 调用原生 Linux xdotool 发送真正的硬件级鼠标点击
        os.system(f"xdotool mousemove {target_x} {target_y} click 1")
        
        print("⏳ 射击完毕！静默等待 8 秒，让子弹飞一会儿 (等待盾转圈通过)...")
        time.sleep(8)
        
        try:
            sb.save_screenshot("screenshots/2_result.png")
            print("📸 最终战况截图已保存。")
        except:
            print("⚠️ 截图保存失败。")

        print("✅ 流程执行完毕！")
        send_tg(f"✅ 服务器 [{MC_USERNAME}] 续期脚本运行完毕！\n【破盾方式: 物理盲狙】请查阅 GitHub 最新截图确认 CF 盾是否通过。")

    except Exception as e:
        print(f"❌ 发生致命错误: {e}")
        try:
            os.makedirs("screenshots", exist_ok=True)
            sb.save_screenshot("screenshots/error.png")
        except:
            pass
        send_tg(f"❌ 自动续期崩溃: {e}")
