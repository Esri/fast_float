from conans import ConanFile


class FastFloatConan(ConanFile):
    name = "fast_float"
    version = "8.0.2"
    url = "https://github.com/Esri/fast_float/tree/runtimecore"
    license = "https://github.com/Esri/fast_float?tab=License-1-ov-file"
    description = "Fast and exact implementation of the C++ from_chars functions for number types"

    # Use the OS default to get the right line endings
    settings = "os"

    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/fast_float/"

        # headers
        self.copy("*", src=base + "include/fast_float", dst=relative + "include/fast_float")
