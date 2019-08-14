import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='CppPythonSocket',  
     version='0.2.2',
    #  scripts=['CppPythonSocket', 'python/server.py'] ,
     author="OleguerCanal",
     author_email="oleguer.canal@hotmail.com",
     description="Simple TCP/IP socket comunication wrapper between c++ and Python for IPC.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/OleguerCanal/cpp_python_socket.git",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )