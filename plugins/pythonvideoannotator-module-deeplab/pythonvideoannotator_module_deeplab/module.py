import cv2, os, simplejson as json
from confapp import conf
from pythonvideoannotator_module_deeplab.deeplab_window import DeepLabWindow


class Module(object):

    def __init__(self):
        """
        This implements the DeepLab functionality
        """
        super(Module, self).__init__()
        self.deeplab_window = DeepLabWindow(self)

        self.mainmenu[1]['Modules'].append(
            {'DeepLab': self.deeplab_window.show },         
        )

    ######################################################################################
    #### IO FUNCTIONS ####################################################################
    ######################################################################################

    def save(self, data, project_path=None):
        data = super(Module, self).save(data, project_path)

        modules_folder = os.path.join(project_path, 'modules')
        if not os.path.exists(modules_folder): os.makedirs(modules_folder)

        deeplab_folder = os.path.join(modules_folder, 'deeplab')
        if not os.path.exists(deeplab_folder): os.makedirs(deeplab_folder)


        deeplabdata = self.deeplab_window.save_form({}, deeplab_folder)

        with open(os.path.join(deeplab_folder, 'config.json'), 'w') as outfile:
            json.dump(deeplabdata, outfile)

        return data

    def load(self, data, project_path=None):
        super(Module, self).load(data, project_path)
        
        deeplab_folder = os.path.join(project_path, 'modules', 'deeplab')
        configfile = os.path.join(deeplab_folder, 'config.json')

        if os.path.exists(configfile):

            with open(configfile) as infile:
                deeplabdata = json.load(infile)

            self.deeplab_window.load_form(deeplabdata, deeplab_folder)