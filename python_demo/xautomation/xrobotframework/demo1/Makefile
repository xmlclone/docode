# libdoc ExampleLibrary ExampleLibrary.html
# python -m robot.libdoc ExampleLibrary ExampleLibrary.html

build_doc:
	libdoc lib1.py lib1.html
	libdoc lib2.py lib2.html
	libdoc lib3 lib3.html
	libdoc lib3/lib4.py lib4.html

run:
	robot -P . .