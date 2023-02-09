from conans import ConanFile, CMake, tools


class QtkeychainConan(ConanFile):
    name = "qt6keychain"
    version = "0.13.2"
    license = "BSD-3"
    author = "Edgar"
    url = "https://github.com/AnotherFoxGuy/fuel-scm"
    description = "Platform-independent Qt API for storing passwords securely"
    settings = "os", "compiler", "build_type", "arch"
    options = {"static": [True, False]}
    default_options = {"static": False}
    scm = {
        "type": "git",
        "url": "https://github.com/frankosterfeld/qtkeychain.git",
        "revision": "v0.13.2"
    }

    def build(self):
        cmake = CMake(self)
        cmake.definitions["QTKEYCHAIN_STATIC"] = self.options.static
        cmake.definitions["BUILD_WITH_QT6"] = "ON"
        cmake.definitions["BUILD_TEST_APPLICATION"] = "OFF"
        #cmake.definitions["CMAKE_PREFIX_PATH"] = "E:/Qt/6.4.0/msvc2019_64"
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_module_file_name", "Qt6Keychain")
        self.cpp_info.set_property("cmake_module_target_name", "Qt6Keychain::Qt6Keychain")
        self.cpp_info.set_property("cmake_file_name", "Qt6Keychain")
        self.cpp_info.set_property("cmake_target_name", "Qt6Keychain::Qt6Keychain")
        self.cpp_info.libs = tools.collect_libs(self)
