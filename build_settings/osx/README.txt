# run this from project folder
python2 build_settings/osx/create-osx-app.py py2app
hdiutil create dist/pythonVideoAnnotator-v1.0.3.dmg -srcfolder dist/pythonVideoAnnotator.app/


