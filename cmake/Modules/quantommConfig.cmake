INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_QUANTOMM quantomm)

FIND_PATH(
    QUANTOMM_INCLUDE_DIRS
    NAMES quantomm/api.h
    HINTS $ENV{QUANTOMM_DIR}/include
        ${PC_QUANTOMM_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    QUANTOMM_LIBRARIES
    NAMES gnuradio-quantomm
    HINTS $ENV{QUANTOMM_DIR}/lib
        ${PC_QUANTOMM_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(QUANTOMM DEFAULT_MSG QUANTOMM_LIBRARIES QUANTOMM_INCLUDE_DIRS)
MARK_AS_ADVANCED(QUANTOMM_LIBRARIES QUANTOMM_INCLUDE_DIRS)

