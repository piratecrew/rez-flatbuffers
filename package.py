name = "flatbuffers"

version = "1.11.0"

authors = [
    "Google"
]

description = \
    """
    FlatBuffers is a cross platform serialization library architected for maximum memory efficiency. It allows you to directly access serialized data without parsing/unpacking it first, while still having great forwards/backwards compatibility.
    """

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**"]
    return [expand_requires(*requires)]

tools = [
    "flatc",
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.prepend("{root}/cmake")
