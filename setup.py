import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='cpp_python_socket',  
     version='0.1',
     scripts=['cpp_python_socket'] ,
     author="Oleguer Canal Anton",
     author_email="oleguer.canal@hotmail.com",
     description="Simple TCP/IP socket comunication wrapper between c++ and Python for IPC.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: Linux",
     ],
 )