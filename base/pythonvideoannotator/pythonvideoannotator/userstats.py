import os, time, datetime, platform
from uuid import getnode as get_mac
from AnyQt.QtWidgets import QMessageBox

from confapp import conf
from .__init__ import __version__
from urllib.parse import urlencode
from urllib.request import Request, urlopen



def get_usage_track_conf():
    try:
        filepath = os.path.join(
            os.path.dirname(
                os.path.realpath(__file__)
            ),
            '.track.cnf'
        )

        modified = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
        now = datetime.datetime.now()

        if (now - modified).total_seconds() > conf.USERSTATS_TIMEOUT_DAYS*60*24:
            return 'ask later'

        with open(filepath, "r") as infile:
            return infile.read()
    except Exception as e:
        print(e)
        return 'ask later'

def set_usage_track_conf(config):
    """
    Configure the usage track type.
    :param str config: Configuration ( it can be 'track','ask-later' or 'no-track'.
    :return:
    """
    try:
        filepath = os.path.join(
            os.path.dirname(
                os.path.realpath(__file__)
            ),
            '.track.cnf'
        )
        with open(filepath, "w") as outfile:
            outfile.write(config)

    except:
        pass


def track_user_stats():

    reply = get_usage_track_conf()

    if reply=='ask later':

        m = QMessageBox(
            QMessageBox.Question,
            "User tracking",
            "Do you give us permission to track which country you are from and how many times you use this application? " \
            "This will contribute to the support of this software.",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.NoRole
        )
        ask_later_btn = m.addButton("Ask me later", QMessageBox.NoRole)
        m.setEscapeButton(ask_later_btn)
        reply = m.exec_()

        if reply == QMessageBox.No:
            set_usage_track_conf('no-track')

        elif reply == QMessageBox.Yes:
            set_usage_track_conf('track')
            reply = 'track'

        elif reply == QMessageBox.NoButton:
            set_usage_track_conf('ask later')

    if reply=='track':
        register_access()


def register_access():
    try:
        app_id  = conf.USERSTATS_APP_ID
        reg_id  = get_mac()
        os_name = platform.platform()
        version = __version__

        data = {'app-id': app_id, 'reg-id': reg_id, 'os-name' : os_name ,'version': version}
        url = "{}/register".format(conf.USERSTATS_URL)
        request = Request(url, urlencode(data).encode())
        urlopen(request).read().decode()
    except Exception as e:
        print("Could not register new access", e)
