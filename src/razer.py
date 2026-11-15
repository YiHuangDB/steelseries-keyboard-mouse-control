import os
import ctypes

class RazerChromaLEDController:
    """Controls Razer Chroma devices using the native Razer Chroma SDK C DLL."""

    def __init__(self):
        self.chroma = None
        self.initialized = False

    def is_available(self):
        dll_paths = [
            r"C:\Program Files\Razer Chroma SDK\bin\RzChromaSDK64.dll",
            r"C:\Program Files (x86)\Razer Chroma SDK\bin\RzChromaSDK.dll"
        ]
        return any(os.path.exists(p) for p in dll_paths)

    def setup(self):
        """Initialize Chroma SDK and set devices to off."""
        dll_paths = [
            r"C:\Program Files\Razer Chroma SDK\bin\RzChromaSDK64.dll",
            r"C:\Program Files (x86)\Razer Chroma SDK\bin\RzChromaSDK.dll"
        ]
        selected_dll = None
        for p in dll_paths:
            if os.path.exists(p):
                selected_dll = p
                break

        if not selected_dll:
            return False

        try:
            self.chroma = ctypes.cdll.LoadLibrary(selected_dll)
            self.chroma.Init.restype = ctypes.c_int
            self.chroma.Init.argtypes = []
            res = self.chroma.Init()
            if res == 0:
                self.initialized = True
                self.set_off()
                return True
        except Exception:
            pass
        return False

    def set_off(self):
        """Set all Chroma devices (Keyboard, Mouse, Keypad, ChromaLink) to CHROMA_NONE (0)."""
        if not self.initialized or not self.chroma:
            return False

        try:
            # CHROMA_NONE = 0
            if hasattr(self.chroma, "CreateKeyboardEffect"):
                self.chroma.CreateKeyboardEffect.restype = ctypes.c_int
                self.chroma.CreateKeyboardEffect.argtypes = [ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
                self.chroma.CreateKeyboardEffect(0, None, None)

            if hasattr(self.chroma, "CreateMouseEffect"):
                self.chroma.CreateMouseEffect.restype = ctypes.c_int
                self.chroma.CreateMouseEffect.argtypes = [ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
                self.chroma.CreateMouseEffect(0, None, None)

            if hasattr(self.chroma, "CreateKeypadEffect"):
                self.chroma.CreateKeypadEffect.restype = ctypes.c_int
                self.chroma.CreateKeypadEffect.argtypes = [ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
                self.chroma.CreateKeypadEffect(0, None, None)

            if hasattr(self.chroma, "CreateChromaLinkEffect"):
                self.chroma.CreateChromaLinkEffect.restype = ctypes.c_int
                self.chroma.CreateChromaLinkEffect.argtypes = [ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
                self.chroma.CreateChromaLinkEffect(0, None, None)

            return True
        except Exception:
            return False

    def close(self):
        """Uninitialize Chroma SDK session to restore default Razer Synapse lighting."""
        if self.initialized and self.chroma:
            try:
                self.chroma.UnInit.restype = ctypes.c_int
                self.chroma.UnInit.argtypes = []
                self.chroma.UnInit()
            except Exception:
                pass
            finally:
                self.initialized = False
