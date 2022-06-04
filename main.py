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
            ["setup Sass/Scss ",False],
            ["setup Typscript ",False],
            ["setup Json ",False],
            ["add css framwork ",False]
        ]
        self.sub_stats_liste = [
            [" Creating Html file ","Creating Css file ","Creating JavaScript file "],
            [],
            [" Creating Typscript file "],
            [" Creating Json file "],
            [
                ["Add bootstrap to your project ",False],
                ["Add bulma to your project ",False],
                ["Add talwind css to your project",False],
                ["Add fontawesom to your project",False],
            ]
        ]
        #detect if the folder is the current folder or a custom folder :
        if self.selected_path == " current folder ":
            self.selected_path = os.getcwd()
        self.status = self.success_log+" init@cli setup "+self.custom_log+self.selected_path
        self.console = Console()
        self.console.log(self.status)
        self.get_user_setup()
    def get_user_setup(self):
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
                        while not progress.finished:
                            progress.update(task1, advance=0.9)
                            time.sleep(0.02)
                except Exception as e:
                    self.console.log(self.error_log+str(e))
        return

if __name__ == '__main__':
    try:
        folder_target = sys.argv[1]
        if folder_target == ".":
            folder_target = " current folder "
        my_current_cli = web_cli(folder_target)
    except  Exception as e:
        Console.log("[bold red][error] ==> "+str(e))
