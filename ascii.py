import os
import time


wordle_ascii =""" 
                           Let's Play

       ██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ███████╗
       ██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝
       ██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     █████╗  
       ██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██╔══╝  
       ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗███████╗
        ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝"""

def wordle_animation():

    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[0;33m'
    BLUE='\033[0;34m'
    PURPLE='\033[0;35m'
    NC='\033[0m' # No Color
      
    while True:
        os.system('clear')
        print(f"""{RED}{wordle_ascii}{NC}""")
        time.sleep(1)
        os.system('clear')
        print(f"""{GREEN}{wordle_ascii}{NC}""")
        time.sleep(1)
        os.system('clear')
        print(f"""{YELLOW}{wordle_ascii}{NC}""")
        time.sleep(1)
        os.system('clear')
        print(f"""{BLUE}{wordle_ascii}{NC}""")
        time.sleep(1)
        os.system('clear')
        print(f"""{PURPLE}{wordle_ascii}{NC}""")
        break
  
    
            
