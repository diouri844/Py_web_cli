# import all modules :
from rich.console import Console
from rich.progress import Progress
import sys
import os
import time


#define my cli class : 
class web_cli():
    def __init__(self,path_target):
        self.selected_path = path_target
        self.error_log = "[bold red]"
        self.success_log = "[bold green]"
        self.custom_log = "[bold blue]"
        # tasks format :  [tastk-name , task-stat ]
        self.task_liste = [
            ["setup Html Css Javascript ",False],
            ["setup Typscript ",False],
            ["setup Json ",False]
        ]
        self.sub_stats_liste = [
            ["  Creating Html file ","   Creating Css file ","    Creating JavaScript file "],
            ["  Creating Typscript file "],
            ["  Creating Json file "]
        ]
        self.files_to_create = [
            ["index.html","index.css","index.js"],
            ["index.ts"],
            ["app.json"],
        ]
        #detect if the folder is the current folder or a custom folder :
        if self.selected_path == " current folder ":
            self.selected_path = os.getcwd()
        self.status = self.success_log+" init@cli setup "+self.custom_log+self.selected_path
        self.console = Console()
        self.console.log(self.status)
        self.get_user_setup()
    def get_defualt_content(self,format):
        format_dispo = ['html','css','js','ts','json']
        default_cont = [
            """<!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <meta http-equiv="X-UA-Compatible" content="ie=edge">
                        <title> py_web@cli </title>
                        <link rel="stylesheet" href="index.css">
                    </head>
                    <body>
	                    <script src="index.js"></script>
                    </body>
                </html>""",
                """*{
                    margin:0;
                    padding:0;
                }
                """,
                """console.log("py_web_cli say hi ");
                """,
                """console.log("py_web_cli say hi ");
                """,
                """{
                    "expo": {
                        "name": "My app",
                        "slug": "my-app",
                        "version" : "1.0.0.1"
                    }
                }"""
        ]
        return default_cont[format_dispo.index(format)]
    def create_file(self,path,file_name):
        try:
            current_file = open(path+"/"+str(file_name), mode="w")
            to_write= self.get_defualt_content(file_name.split('.')[1])
            current_file.write(to_write)
            current_file.close()
        except Exception as e:
            self.console.log(self.error_log+str(e))
        return
    def get_user_setup(self):
        # create app folder :
        try:
            os.mkdir(path=self.selected_path+"/your_app", mode=777)
            #update path_target:
            self.selected_path = self.selected_path+"/your_app"
            #create files:
            for setup_item in self.task_liste:
                current_stat = ""
                if setup_item[1]==False:
                    current_stat = self.error_log+" [-] "
                else:
                    current_stat = self.success_log+" [+] "
                current_task = current_stat+self.custom_log+setup_item[0]
                self.console.log(current_task)
                current_index = self.task_liste.index(setup_item)
                for sub_task in self.sub_stats_liste[current_index]:
                    try:
                        with Progress() as progress:
                            task_name = self.custom_log+sub_task+" ...."
                            task1 = progress.add_task(task_name, total=100)
                            for file_target in self.files_to_create[current_index]:
                                self.create_file(self.selected_path,file_target)
                            while not progress.finished:
                                progress.update(task1, advance=0.9)
                                time.sleep(0.02)
                    except Exception as e:
                        self.console.log(self.error_log+str(e))
            #project setup ended :
            self.console.log(self.success_log+"init@cli setup successuflly ")
            self.console.log(self.custom_log+"cd "+self.custom_log+self.selected_path)
            self.console.log(self.success_log+"code . ")
        except Exception as e:
            self.console.log("[bold red][error] ==> "+str(e))
        
        return

if __name__ == '__main__':
    try:
        folder_target = sys.argv[1]
        if folder_target == ".":
            folder_target = " current folder "
        my_current_cli = web_cli(folder_target)
    except  Exception as e:
        Console.log("[bold red][error] ==> "+str(e))
