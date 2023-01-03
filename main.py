import pyautogui as pyg

if __name__ == "__main__":
    while True:
        pyg.press('F3')
        pyg.keyDown('alt')
        pyg.press('right')
        pyg.keyUp('alt')
        pyg.PAUSE = 1
        #autopy.key.tap(autopy.key.Code.F3,None,1)
        #autopy.key.tap(autopy.key.Code.SPACE,None,1)
