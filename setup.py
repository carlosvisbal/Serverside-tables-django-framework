import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='Serverside-tables-django-framework',
      version='0.0.2',
      description="Vista de procesamiento de tabla de datos del lado del servidor simple para Django-framework",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/carlosvisbal/Serverside-tables-django-framework",
      license="MIT",
      author="Carlos Visbal",
      author_email='carlosvisbal66@gmail.com',
      install_requires=['Django>=1.8'],
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
)
