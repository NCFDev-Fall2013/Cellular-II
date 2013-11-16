import GUI, pygame

def main():
    test()
    
def test():
    a = []
    b = 500, 500
    #print b
    c = ''
    d = ''
    e = 'test window'
    testWindow = GUI.gameWindow(a,b,c,d,e)
    
    a = []
    b = 200, 100
    c = 100,50
    d = 250,0,0
    testFrame = GUI.gameFrame(a,b,c,d)
    
   # testWindow.add_frame(rect)
    testWindow.add_frame(testFrame)
    testWindow.window_start()
    #testFrame.show()
main()
