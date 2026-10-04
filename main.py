import time
import pyautogui
import keyboard


def show_mouse_position():
    print("Di chuyển chuột đến vị trí bạn muốn, rồi nhấn Ctrl+C để dừng theo dõi.")
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Mouse position: X={x}, Y={y}", end="\r")
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nĐã dừng theo dõi vị trí chuột.")


def demo_move_and_click():
    width, height = pyautogui.size()
    center_x, center_y = width // 2, height // 2
    pyautogui.moveTo(center_x, center_y, duration=0.5)
    time.sleep(0.5)
    pyautogui.click(center_x, center_y)
    print(f"Đã di chuyển tới vị trí trung tâm màn hình: ({center_x}, {center_y}) và click.")


def demo_keyboard():
    print("Bắt đầu demo nhập phím trong 3 giây...")
    time.sleep(3)
    pyautogui.typewrite("Hello from Python automation demo!", interval=0.1)
    print("Đã gõ chữ thử nghiệm.")


def demo_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("automation_demo.png")
    print("Đã lưu ảnh chụp màn hình vào automation_demo.png")


def menu():
    print("=" * 50)
    print("PYTHON AUTOMATION DEMO")
    print("=" * 50)
    print("1. Xem vị trí chuột")
    print("2. Di chuyển chuột và click")
    print("3. Demo nhập phím")
    print("4. Chụp màn hình")
    print("5. Thoát")
    print("=" * 50)


if __name__ == "__main__":
    while True:
        menu()
        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            show_mouse_position()
        elif choice == "2":
            demo_move_and_click()
        elif choice == "3":
            demo_keyboard()
        elif choice == "4":
            demo_screenshot()
        elif choice == "5":
            print("Thoát demo automation.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn 1-5.")

        print("\nNhấn Enter để quay lại menu...")
        input()
