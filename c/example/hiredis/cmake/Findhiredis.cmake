
find_path(HIREDIS_INCLUDE_DIR hiredis.h /usr/local/include/hiredis)
find_library(HIREDIS_LIBRARY NAMES hiredisb PATH /usr/local/lib)
 
if(HIREDIS_INCLUDE_DIR AND HIREDIS_LIBRARY)
    SET(HIREDIS_FOUND TRUE)
endif(HIREDIS_INCLUDE_DIR AND HIREDIS_LIBRARY)
 
if(HIREDIS_FOUND)
    if(NOT HIREDIS_FIND_QUIETLY)
        message(STATUS "Found Hello: ${HIREDIS_LIBRARY}")
    endif(NOT HIREDIS_FIND_QUIETLY)
else(HIREDIS_FOUND)
    if(HIREDIS_FIND_REQUIRED)
        message(FATAL_ERROR "Could not find hello library")
    endif(HIREDIS_FIND_REQUIRED)
endif(HIREDIS_FOUND)