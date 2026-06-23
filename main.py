try:
    import os  
except Exception:
    import uos as os
    

while True:
    cmd = input(str(os.getcwd())+">>>")
    if cmd == "":
        pass
    else:
        try:
            cmd = cmd.split()
            
            if cmd[0] == "ls":
                print(os.listdir())
           
            elif cmd[0] == "cd":
                os.chdir(cmd[1])
        
            elif cmd[0] == "mkdir":
                os.mkdir(cmd[1])
                print("dir made")
            
            elif cmd[0] == "make" or cmd[0] == "touch":
                with open (cmd[1],"w",encoding="utf-8") as f:
                    print("file:"+cmd[1]+" was made.")
            
            elif cmd[0] == "rmdir":
                os.rmdir(cmd[1])
                print("dir:"+cmd[1]+" was removed.")
                
            elif cmd[0] == "rmfile":
                os.remove(cmd[1])
                print("file:"+cmd[1]+" was removed.")
                
            elif cmd[0] == "show" or cmd[0] == "cat":
                with open (cmd[1],"r",encoding="utf-8") as f:
                    data = f.readlines()
                    for i in data:
                        print(i)
                    
            elif cmd[0] == "chfile":
                for i in range(int(cmd[2])):
                    with open (cmd[1],"a",encoding="utf-8") as f:
                        num = input()
                        f.write(num+"\n")
                        
            elif cmd[0] == "python":
                print("welcome th the ide!q to exit h for help.")
                while True:
                    ide = input("py:")
                    if ide == "q":
                        break
                    elif ide == "h":
                        print("welcome th the ide!q to exit h for help.")
                    
                    else:
                        try:
                            print(eval(ide))
                        except Exception:
                            try:
                                exec(ide)
                            except Exception as e:
                                print(e)
                                
            elif cmd[0] == "execfile":
                with open (cmd[1],"r",encoding = "utf-8") as f:
                    data = f.read()
                    try:
                        exec(data)
                    except Exception as e:
                        print("SYNTAX ERROR")
                        print(e)
                        
            elif cmd[0] == "rename":
                os.rename(cmd[1],cmd[2])
                
            elif cmd[0] == "break":
                break
            
            elif cmd[0] == "help":
                print("ls,cd,mkdir,touch,rmdir,rmfile,cat,chfile,python,execfile,rename,break")
            
        except KeyboardInterrupt:
            pass
        
        except Exception:
            pass