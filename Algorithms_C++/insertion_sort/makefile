#
# 'make'        build executable file 'mycc'
# 'make clean'  removes all .o and executable files
#

# define the C compiler to use
CC = g++

# define any compile-time flags
CFLAGS = -std=c++11

# define any directories containing header files other than /usr/include
#
#INCLUDES = -I/Users/osmanmamun/Suncat_Code_Base/eigen 

# define library paths in addition to /usr/lib
#   if I wanted to include libraries not in /usr/lib I'd specify
#   their path using -Lpath, something like:
#LFLAGS = -L/Users/osmanmamun/Suncat_Code_Base/cnpy/build 

# define any libraries to link into executable:
#   if I want to link in libraries (libx.so or libx.a) I use the -llibname
#   option, something like (this will link in libmylib.so and libm.so:
#LIBS = -lcnpy -lz

# define the C source files
SRCS = main.cpp 

# define the C object files
#
# This uses Suffix Replacement within a macro:
#   $(name:string1=string2)
#         For each word in 'name' replace 'string1' with 'string2'
# Below we are replacing the suffix .c of all words in the macro SRCS
# with the .o suffix
#
#OBJS = $(SRCS:.c=.o)

# define the executable file
MAIN = exe_file

#
# The following part of the makefile is generic; it can be used to
# build any executable just by changing the definitions above and by
# deleting dependencies appended to the file from 'make depend'
#


all:    $(MAIN)
	@echo  main has been compiled

$(MAIN): $(SRCS)
	$(CC) $(CFLAGS) $(INCLUDES) $(SRCS) -o $(MAIN) $(LFLAGS) $(LIBS)

clean:
	$(RM)  $(MAIN)
