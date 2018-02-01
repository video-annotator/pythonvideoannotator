import pyforms, os, simplejson as json, pprint
from glob import glob
from pythonvideoannotator_models.models import Project
from pythonvideoannotator_models_gui.dialogs import Dialog
from pythonvideoannotator_module_tracking.tracking_window import TrackingWindow
pp = pprint.PrettyPrinter()


for PROJECT_CONFIG_FILE in glob("*/video-annotator-prj"):

    with open(os.path.join(PROJECT_CONFIG_FILE, 'modules', 'tracking','config.json')) as infile:
        data = json.load(infile)

    proj = Project()
    proj.load({}, PROJECT_CONFIG_FILE)
    Dialog.project = proj

    data['_input']['value']['_interval']['value']=[0, 1000000000000]
    data['_input']['value']['_panel']['value']['_videos']['selected']=[proj.videos[0].name]
    data['_filter_panel']['value']['_imgfilters']['value'][3][1]['_panel']['value']['_panel']['value']['_videos']['selected']=[proj.videos[0].name]

    data['_input']['value']['_panel']['value']['_objects']['selected']=['object-0']
    data['_input']['value']['_panel']['value']['_datasets']['selected']=['contour-0']
    data['_filter_panel']['value']['_imgfilters']['value'][3][1]['_panel']['value']['_panel']['value']['_objects']['selected']=['object-0']
    data['_filter_panel']['value']['_imgfilters']['value'][3][1]['_panel']['value']['_panel']['value']['_datasets']['selected']=['trajectory-0']
    pp.pprint(data)

    pyforms.start_app(
        TrackingWindow, 
        app_args={ 'project':proj, 'load':data }
    )
    proj.save()

    data['_input']['value']['_panel']['value']['_objects']['selected']=['object-1']
    data['_input']['value']['_panel']['value']['_datasets']['selected']=['contour-1']
    data['_filter_panel']['value']['_imgfilters']['value'][3][1]['_panel']['value']['_panel']['value']['_objects']['selected']=['object-1']
    data['_filter_panel']['value']['_imgfilters']['value'][3][1]['_panel']['value']['_panel']['value']['_datasets']['selected']=['trajectory-1']
    pp.pprint(data)

    pyforms.start_app(
        TrackingWindow, 
        app_args={ 'project':proj, 'load':data }
    )
    proj.save()