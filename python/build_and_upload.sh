# Yes, I am so lazy that I wrote a bash file for this 2 commands
rm -rf build/
rm -rf CppPythonSocket.egg-info
rm -rf dist
python3 setup.py sdist bdist_wheel
twine upload dist/*