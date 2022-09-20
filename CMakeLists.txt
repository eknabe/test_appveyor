project (hello_world)

set (TARGET hello_world)

set ( SOURCES main.cpp )

set ( CMAKE_OSX_ARCHITECTURES "arm64;x86_64" )

add_executable ( ${TARGET} ${SOURCES} )
