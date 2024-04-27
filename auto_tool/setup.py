import setuptools

setuptools.setup(
    name="auto_tool",
    version="0.0.1",
    author = "Henry Walker", 
    author_email= "davisdavis448@gmail.com",
    description= "A tool for automating test cases",
    packages=setuptools.find_packages(),
    install_requires = [
        'pandas',
        'openpyxl',
        'xlsxwriter',
        'selenium',
    ],
    
)