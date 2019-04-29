import os
import xmlrpc.client
from subprocess import Popen, PIPE
import shutil


pypi = xmlrpc.client.ServerProxy('https://pypi.org')

MAIN_NAME = 'pythonvideoannotator'
MAIN_PATH = os.path.join('base', MAIN_NAME)
MAIN_REPO = 'python-video-annotator'

DIRECTORIES_TO_SEARCH_FORM = [
	os.path.join('libraries'),
	os.path.join('base'),
	os.path.join('plugins'),
]

CURRENT_DIRECTORY = os.getcwd()


Popen(['pip','install','--upgrade','setuptools','wheel','twine'])


def version_compare(a, b):
	try:
		a = float(a)
		b = float(b)
	except:
		return -1
	"""
	a = a.split('.')
	b = b.split('.')
	for a_value, b_value in zip(a, b):
		a_value = int(a_value)
		b_value = int(b_value)
		
		if a_value>b_value:
			return -1
		elif a_value<b_value:
			return 1

	if len(a)>len(b):
		return -1
	elif len(a)<len(b):
		return 1

	return 0
	"""
	if a==b: return 0
	if a<b: return 1
	if a>b: return -1

def check_version_and_upload(dir_path):
	os.chdir(dir_path)

	try:
		shutil.rmtree(os.path.join(dir_path, 'build'))
	except OSError:
		pass
	except Exception as e:
		print(e)
	try:
		shutil.rmtree(os.path.join(dir_path, 'dist'))
	except OSError:
		pass
	except Exception as e:
		print(e)

	version = Popen(["python", 'setup.py', '--version'], stdout=PIPE).stdout.read()
	version = version.strip().decode()

	package_name = Popen(["python", 'setup.py', '--name'], stdout=PIPE).stdout.read()
	package_name = package_name.strip().decode().replace(' ', '-')
	package_name = package_name.replace('---', '-').lower()

	remote_version = pypi.package_releases(package_name)

	print(
		"{:<65} {:<10} {:<10}".format(package_name, version, remote_version[0])
	)

	updated = False

	if len(remote_version) == 0 or version_compare(version, remote_version[0]) < 0:
		print('----- UPLOADING PYPI -----', package_name)

		if os.path.isdir('./dist'): shutil.rmtree('./dist')
		Popen(['python', 'setup.py', 'sdist', 'bdist_wheel'], stdout=PIPE).communicate()
		Popen(['twine', 'upload', os.path.join('dist','*')]).communicate()
		updated = True

	os.chdir(CURRENT_DIRECTORY)

	return updated, package_name, version


requirements = []

should_update = False

for search_dir in DIRECTORIES_TO_SEARCH_FORM:
	for dir_name in os.listdir(search_dir):
		dir_path = os.path.abspath(os.path.join(search_dir, dir_name))


		# is not a directory or is the main repository
		if not os.path.isdir(dir_path) or MAIN_NAME==dir_name: continue

		setup_filepath = os.path.join(dir_path, 'setup.py')
		if not os.path.isfile(setup_filepath): continue

		updated, package_name, version = check_version_and_upload(dir_path)

		if updated:
			should_update = True

		if package_name != MAIN_REPO:
			requirements.append("{module}=={version}".format(module=package_name, version=version))


with open( os.path.join(MAIN_PATH, 'setup.py') ) as infile:
	text = infile.read()

begin = text.index('# REQUIREMENTS BEGIN')
end = text.index('# REQUIREMENTS END', begin)+len('# REQUIREMENTS END')
new_text = """# REQUIREMENTS BEGIN
REQUIREMENTS = [
    "{}"
]
# REQUIREMENTS END""".format('",\n\t"'.join(requirements))

text = text.replace(text[begin:end], new_text)

with open( os.path.join(MAIN_PATH, 'setup.py'), 'w' ) as outfile:
	outfile.write(text)

with open( os.path.join(MAIN_PATH, MAIN_NAME, '__init__.py') ) as infile:
	text = infile.read()

if should_update:
	os.chdir(MAIN_PATH)
	version = Popen(["python", 'setup.py', '--version'], stdout=PIPE).stdout.read()
	version = float(version.strip().decode())
	os.chdir(CURRENT_DIRECTORY)

	begin = text.index('__version__')
	end   = text.index('\n', begin)
	text  = text.replace(text[begin:end], '__version__ = "{0}"'.format(round(version + 0.001, 3)))

with open( os.path.join(MAIN_PATH, MAIN_NAME, '__init__.py'), 'w' ) as outfile:
	outfile.write(text)


updated, package_name, version = check_version_and_upload(MAIN_PATH)