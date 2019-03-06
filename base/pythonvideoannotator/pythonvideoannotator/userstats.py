import json, urllib.request, os, AnyQt
from uuid import getnode as get_mac
from AnyQt.QtWidgets import QApplication, QFileDialog, QMessageBox

USERSTATS_URL="http://stats.cf-sw.org/userstats/"


def user_file_exists():
    return os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)),"trackingsettings.txt"))


def user_allowed_tracking():
    try:
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),"trackingsettings.txt")
        num_user = open(filename).read().splitlines()[0]

        if num_user!=str(-1):
            return True
        else:
            return False
    except:
        return False


def mac_address_matches():
    try:
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),"trackingsettings.txt")
        mac_address = open(filename).read().splitlines()[1]

        if mac_address==str(get_mac()):
            return True
        else:
            return False
    except:
        return False


def create_user_file(num_user):
    try:
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),"trackingsettings.txt")
        s=open(filename, "w")

        s.write(str(num_user)+"\n")
        s.write(str(get_mac())+"\n")

        s.close()

    except:
        return False

def get_num_user():
    try:
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),"trackingsettings.txt")
        num_user = open(filename).read().splitlines()[0]

        return num_user

    except:
        return -1


def user_stats_question():

    title = "User tracking"
    msg = "Do you give us permission to track what country you are from and how many times you use this application? This will contribute to the support of this software."
    
    btns = QMessageBox.Yes | QMessageBox.No | QMessageBox.NoRole

    m = QMessageBox(QMessageBox.Question, title, msg, btns)
    ask_later_button = m.addButton("Ask me later", QMessageBox.NoRole)
    m.setEscapeButton(ask_later_button)

    reply = m.exec_()
    
    if reply==QMessageBox.No:   
        return 'no'
    elif reply==QMessageBox.Yes:  
        return 'yes'
    elif reply==QMessageBox.NoButton:
        return 'ask later'



def track_user_stats():

    if user_file_exists():

        if mac_address_matches():

            if user_allowed_tracking():

                register_new_access()
            
            return

    answer=user_stats_question()

    if answer=='yes':
        num_user=register_new_user()
        create_user_file(num_user)

    elif answer=='no':
        create_user_file(-1)

    elif answer=='ask later':
        pass

    return
    

def register_new_user():
    try:
        num_user = json.loads(urllib.request.urlopen("{}/register".format(USERSTATS_URL)).read().decode())
        return num_user

    except:
        print("Could not register new user")

def register_new_access():
    try:
        num_user = get_num_user()

        if num_user==-1:
            raise Exception

        urllib.request.urlopen("{}/register/{}".format(USERSTATS_URL, num_user))

    except Exception as e:
        print("Could not register new access", e)
