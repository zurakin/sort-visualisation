import gui
import target
import constantes

def execute(*args):
    global unordered
    try:
        unordered.clear(root)
    except:
        pass
    unordered = target.Target()
    unordered.draw(root)
    for _ in range(constantes.sticknum):
        unordered.sort(root)


root = gui.Window('selection sort')
root.window.bind('<Return>',execute)
execute()

root.window.mainloop()
