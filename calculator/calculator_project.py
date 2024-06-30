
import inc.func
import inc.initalize
import inc.language
import inc.inital_screen
import inc.variable_global

# main function
def main():

    # inittalize project
    inc.variable_global.key = inc.initalize.init_key()
    inc.language.change_language(inc.variable_global.language)
    app = inc.inital_screen.init_screen()
    
    # mainloop
    app.mainloop()

# main process
if __name__ == "__main__":
    main()