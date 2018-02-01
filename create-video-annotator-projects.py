from pythonvideoannotator_models.models import Project
import os, glob

NUMBER_OF_OBJECTS = 2

BASEDIRECTORY = '/home/ricardo/Downloads/cecilia_movies/movies'
CSV_DIRECTORY = '/home/ricardo/Downloads'

videofiles = [i for i in glob.glob(os.path.join(BASEDIRECTORY, '*', '*','*.avi'))]

for n_video, video_file in enumerate(videofiles):
    video_dir = os.path.dirname(video_file)
    video_name = os.path.basename(video_file)
    print( "{0}\t\t\t{1}/{2}".format(video_name, n_video+1, len(videofiles)) )

    csv_file = os.path.join(video_dir, 'trajectories_nogaps.txt')
    if os.path.isfile(csv_file):

        p = Project()

        video = p.create_video()
        video.filepath = video_file

        for obj_n in range(NUMBER_OF_OBJECTS):
            
            obj  = video.create_object()
            obj.name = 'object-{0}'.format(obj_n)

            path = obj.create_path()
            path.import_csv(csv_file, first_row=1, col_frame=-1, col_x=0+3*obj_n, col_y=1+3*obj_n)
            path.name = 'trajectory-{0}'.format(obj_n)

            contour = obj.create_contours()
            contour.name = 'contour-{0}'.format(obj_n)

            contour = obj.create_contours()
            contour.name = 'body-{0}'.format(obj_n)


        p.save({}, os.path.join(video_dir, 'video-annotator-prj') )