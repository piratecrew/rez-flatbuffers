CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(flatbuffers_version $ENV{REZ_BUILD_PROJECT_VERSION})
rez_set_archive(flatbuffers_path flatbuffers/flatbuffers-v${flatbuffers_version}.tar.gz https://github.com/google/flatbuffers/archive/v${flatbuffers_version}.tar.gz)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    flatbuffers
    URL ${flatbuffers_path}
    PREFIX flatbuffers
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
)

ExternalProject_Get_Property(flatbuffers source_dir)

install(
    FILES 
        ${source_dir}/CMake/FindFlatBuffers.cmake
        ${source_dir}/CMake/BuildFlatBuffers.cmake
        cmake/flatbuffers.cmake
    DESTINATION cmake
)
